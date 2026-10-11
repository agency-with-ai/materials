"""Check the student's classifier on small examples and reference metrics."""

import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def matches(actual, expected):
    """Allow small floating-point differences across Python versions."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and actual.keys() == expected.keys() and all(
            matches(actual[name], value) for name, value in expected.items()
        )
    if isinstance(expected, float):
        return isinstance(actual, (float, int)) and math.isclose(
            actual, expected, rel_tol=1e-12, abs_tol=1e-12
        )
    return actual == expected


def check_small_cases():
    import baseline

    # One constant feature and a distance tie in an unsorted training list.
    train = [
        {"row_id": 3, "weight": 3000.0, "cylinders": 4, "label": 0},
        {"row_id": 1, "weight": 1000.0, "cylinders": 4, "label": 0},
        {"row_id": 2, "weight": 2000.0, "cylinders": 4, "label": 1},
    ]
    before = [dict(row) for row in train]
    features = ("weight", "cylinders")
    scaling = baseline.fit_scaling(train, features)
    expected = {
        "weight": {"mean": 2000.0, "std": math.sqrt(2000000 / 3)},
        "cylinders": {"mean": 4.0, "std": 1.0},
    }
    if not matches(scaling, expected):
        raise SystemExit("Small example failed: check training means and population standard deviations.")
    query = {"row_id": 4, "weight": 2500.0, "cylinders": 4, "label": 1}
    for count, expected_ids in ((1, [2]), (3, [2, 3, 1])):
        nearest = baseline.nearest_neighbors(query, train, scaling, count)
        if [row["row_id"] for row in nearest] != expected_ids:
            raise SystemExit("Small example failed: check neighbor order and row_id ties.")
        predictions, fitted = baseline.evaluate(train, [query], features, count)
        expected_label = 1 if count == 1 else 0
        if predictions[0]["predicted"] != expected_label or not matches(fitted, expected):
            raise SystemExit("Small example failed: check voting and fit scaling on training rows only.")
    if train != before:
        raise SystemExit("Small example failed: leave input rows unchanged.")

    # Scaling changes the nearest neighbor compared with using raw pounds.
    train[0]["label"] = train[1]["label"] = 1
    train[2]["cylinders"] = 8
    train[2]["label"] = 0
    scaling = baseline.fit_scaling(train, features)
    query = {"row_id": 5, "weight": 1900.0, "cylinders": 4, "label": -1}
    nearest = baseline.nearest_neighbors(query, train, scaling, 1)
    if [row["row_id"] for row in nearest] != [1]:
        raise SystemExit("Small example failed: scale both features before comparing distances.")
    print("PASS: small classifier examples.")


def main():
    if sys.version_info < (3, 10):
        raise SystemExit("Setup needs Python 3.10 or later.")
    provided = ROOT / "provided-results"
    expected = json.loads((provided / "reference-metrics.json").read_text())
    digest = hashlib.sha256((ROOT / "cars.tsv").read_bytes()).hexdigest()
    if digest != expected["data_sha256"]:
        raise SystemExit("cars.tsv differs from the supplied data. Restore it from the download.")
    check_small_cases()
    output = ROOT / "runs" / "setup"
    result = subprocess.run(
        [sys.executable, str(ROOT / "baseline.py"), "--out", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    print(result.stdout, end="")
    if result.returncode:
        print(result.stderr, file=sys.stderr, end="")
        raise SystemExit(result.returncode)
    actual = json.loads((output / "metrics.json").read_text())
    if not matches(actual, expected):
        raise SystemExit("Generated metrics differ from provided-results/reference-metrics.json.")
    print("PASS: small examples and reference metrics match.")


if __name__ == "__main__":
    main()
