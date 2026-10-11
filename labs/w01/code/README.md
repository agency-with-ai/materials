# Car classification code

## Specification

Implement `fit_scaling` and `nearest_neighbors` in `code/baseline.py`. The runner supplies data loading, the split, label voting, and output files. Use Python 3.10 or later and only the standard library.

The first run uses weight and cylinder count, k = 1, and the training and validation IDs in `code/provided-results/reference-metrics.json`. The functions also accept the features and odd neighbor counts passed by the runner.

- `fit_scaling(train, features)` returns `{feature: {"mean": ..., "std": ...}}`. Fit each feature's mean and population standard deviation using only the training rows. Use 1.0 for a zero standard deviation.
- `nearest_neighbors(row, train, scaling, count)` returns `count` training-row dictionaries, ordered by squared Euclidean distance after scaling, then by ascending `row_id` for ties. For each feature, divide the difference between the query and training values by its fitted standard deviation. Use only the features in `scaling`.

Leave the input rows unchanged. The runner predicts the majority label among the returned neighbors and records their IDs in that order.

## What a passing run prints

A matching implementation reports

```
Train 294; validation 98
Correct 86/98; accuracy 0.878
Majority baseline 0.500
```

The checker ends with `PASS: small examples and reference metrics match.` Staff compare individual predictions at Checkoff 1. Before you implement the functions, an error naming the missing function is expected.

## Predict new cars

From the downloaded `lab1` folder, run

```sh
python3 code/baseline.py --predict-data code/new-cars.tsv --out code/runs/new-cars
```

`--predict-data` applies the model to every row in the given file. It keeps the selected training rows and fits scaling on them. This command uses the same training cars, features, and k as Step 2, saving `predictions.tsv` and `metrics.json` in `code/runs/new-cars/`.

## Run experiments

Run these from the `lab1` folder as well. `python3 code/baseline.py --help` lists the options.

`--data` takes one or more record files, defaulting to `code/cars.tsv`. Give it several to draw training and validation rows from more than one file, as in `--data code/cars.tsv code/new-cars.tsv`. Row IDs must stay unique across them.

`--split` takes a JSON file with `train_ids` and `validation_ids`. Each field must contain a nonempty list of unique integer `row_id` values from the input files. The two lists must be disjoint. You may leave some cars unused. Other fields are ignored, so an existing `metrics.json` also works as a split file. With `--predict-data`, the runner uses the split's training rows and predicts the rows in the new file instead of the split's validation rows. Prediction row IDs must not overlap training row IDs.

A script in the `code` folder can import the data loader and split function. This example saves the default split. To apply your own selection rule, change how the script constructs the `train` and `validation` row lists.

```python
import json
from pathlib import Path
from baseline import ROOT, load_rows, split_rows

rows = load_rows(ROOT / "cars.tsv")
train, validation = split_rows(rows)
Path(ROOT / "split.json").write_text(json.dumps({
    "train_ids": [row["row_id"] for row in train],
    "validation_ids": [row["row_id"] for row in validation],
}, indent=2) + "\n")
```

Run a model on those rows with

```sh
python3 code/baseline.py --split code/split.json --out code/runs/chosen-split
```

Combine `--split` with `--features` and `--neighbors`. The output file `metrics.json` records the split-file path and both ID lists, along with the model settings and results.
