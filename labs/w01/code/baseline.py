"""Run car-classifier experiments after implementing the two missing functions."""

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FEATURES = ("weight", "cylinders", "model_year")


def load_rows(path):
    with path.open(newline="") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    for row in rows:
        for field in ("row_id", "label", "cylinders", "model_year"):
            row[field] = int(row[field])
        row["weight"] = float(row["weight"])
    if len({row["row_id"] for row in rows}) != len(rows):
        raise ValueError("row_id must be unique")
    if any(row["label"] not in (0, 1) for row in rows):
        raise ValueError("labels must be 0 or 1")
    return rows


def split_rows(rows):
    """Keep one quarter of each class for validation; row order has no effect."""
    train, validation = [], []
    for label in (0, 1):
        group = sorted(
            (row for row in rows if row["label"] == label),
            key=lambda row: hashlib.sha256(
                f"agency-lab1/{row['row_id']}".encode()
            ).hexdigest(),
        )
        count = len(group) // 4
        validation.extend(group[:count])
        train.extend(group[count:])
    return sorted(train, key=lambda row: row["row_id"]), sorted(
        validation, key=lambda row: row["row_id"]
    )


def load_split(rows, path):
    """Read explicit row IDs and return both groups in source ID order."""
    specification = json.loads(path.read_text())
    if not isinstance(specification, dict):
        raise ValueError("split must be a JSON object")
    by_id = {row["row_id"]: row for row in rows}
    groups = []
    for name in ("train_ids", "validation_ids"):
        ids = specification.get(name)
        if not isinstance(ids, list) or not ids or any(type(row_id) is not int for row_id in ids):
            raise ValueError(f"{name} must be a nonempty list of integer row_ids")
        if len(set(ids)) != len(ids):
            raise ValueError(f"{name} must contain unique row_ids")
        if any(row_id not in by_id for row_id in ids):
            raise ValueError(f"{name} contains an unknown row_id")
        groups.append([by_id[row_id] for row_id in sorted(ids)])
    if set(specification["train_ids"]) & set(specification["validation_ids"]):
        raise ValueError("train_ids and validation_ids must be disjoint")
    return groups[0], groups[1]


def fit_scaling(train, features):
    """Return {feature: {"mean": float, "std": float}} using training rows.

    Use population standard deviation, with 1.0 for a constant feature.
    """
    raise NotImplementedError("Implement fit_scaling using the specification in README.md.")


def nearest_neighbors(row, train, scaling, count):
    """Return count training rows ordered by squared scaled distance, then row_id."""
    raise NotImplementedError("Implement nearest_neighbors using the specification in README.md.")


def evaluate(train, validation, features, neighbors):
    scaling = fit_scaling(train, features)
    predictions = []
    for row in validation:
        nearest = nearest_neighbors(row, train, scaling, neighbors)
        predicted = 1 if 2 * sum(other["label"] for other in nearest) > len(nearest) else 0
        predictions.append(
            {
                **row,
                "predicted": predicted,
                "correct": int(predicted == row["label"]),
                "neighbor_ids": ",".join(str(other["row_id"]) for other in nearest),
            }
        )
    return predictions, scaling


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--features", nargs="+", choices=FEATURES, default=["weight", "cylinders"],
                        help="features used in the distance (default: weight cylinders)")
    parser.add_argument("--neighbors", type=int, default=1,
                        help="positive odd count, no larger than the training set (default: 1)")
    parser.add_argument("--data", nargs="+", type=Path, default=[ROOT / "cars.tsv"],
                        help="TSV files of car records (default: cars.tsv)")
    parser.add_argument("--split", type=Path,
                        help="JSON file containing train_ids and validation_ids (default: the supplied split)")
    parser.add_argument("--predict-data", type=Path,
                        help="predict every row in this TSV using the selected training rows")
    parser.add_argument("--out", type=Path, default=ROOT / "runs" / "baseline",
                        help="directory for metrics.json and predictions.tsv (default: runs/baseline)")
    args = parser.parse_args()
    rows = []
    for path in args.data:
        rows.extend(load_rows(path))
    if len({row["row_id"] for row in rows}) != len(rows):
        parser.error("--data files must not repeat a row_id")
    split = "SHA-256 of agency-lab1/row_id; first quarter of each class is validation"
    if args.split is None:
        train, validation = split_rows(rows)
    else:
        try:
            train, validation = load_split(rows, args.split)
        except (OSError, ValueError) as error:
            parser.error(f"--split: {error}")
        split = f"Explicit row IDs from {args.split}"
    if args.predict_data is not None:
        try:
            validation = load_rows(args.predict_data)
            if not validation:
                raise ValueError("prediction file must contain at least one row")
            if {row["row_id"] for row in train} & {row["row_id"] for row in validation}:
                raise ValueError("prediction rows must not share row IDs with training rows")
        except (OSError, ValueError) as error:
            parser.error(f"--predict-data: {error}")
        split = f"Training rows from {split}; prediction rows from {args.predict_data}"
    if args.neighbors < 1 or args.neighbors % 2 == 0 or args.neighbors > len(train):
        parser.error("--neighbors must be a positive odd number no larger than the training set")
    if len(set(args.features)) != len(args.features):
        parser.error("--features must not repeat a feature")
    predictions, scaling = evaluate(train, validation, args.features, args.neighbors)
    correct = sum(row["correct"] for row in predictions)
    majority_label = 1 if 2 * sum(row["label"] for row in train) > len(train) else 0
    counts = {
        f"actual_{actual}_predicted_{predicted}": sum(
            row["label"] == actual and row["predicted"] == predicted for row in predictions
        )
        for actual in (0, 1)
        for predicted in (0, 1)
    }
    data_paths = args.data + ([args.predict_data] if args.predict_data is not None else [])
    metrics = {
        "data_sha256": hashlib.sha256(b"".join(path.read_bytes() for path in data_paths)).hexdigest(),
        "split": split,
        "train_count": len(train),
        "validation_count": len(validation),
        "features": args.features,
        "neighbors": args.neighbors,
        "scaling_fit_on": "training rows only",
        "scaling": scaling,
        "correct": correct,
        "accuracy": correct / len(validation),
        "confusion_counts": counts,
        "majority_label": majority_label,
        "majority_accuracy": sum(row["label"] == majority_label for row in validation) / len(validation),
        "train_ids": [row["row_id"] for row in train],
        "validation_ids": [row["row_id"] for row in validation],
    }
    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out / "predictions.tsv").open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(predictions[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(predictions)
    (args.out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(f"Train {len(train)}; validation {len(validation)}")
    print(f"Correct {correct}/{len(validation)}; accuracy {correct / len(validation):.3f}")
    print(f"Majority baseline {metrics['majority_accuracy']:.3f}")
    print(f"Results in {args.out}")


if __name__ == "__main__":
    main()
