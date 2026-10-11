# Lab 1 materials

Start with the [lab instructions](lab.md).

## Student pages and download

| File | Purpose |
|---|---|
| [prelab.md](prelab.md) | Claude Code and Python setup before class. |
| [check_environment.py](check_environment.py) | Checks Python, file access, and launching another Python process. |
| [lab1-setup.zip](https://agencyai.mit.edu/lab1/lab1-setup.zip) | Pre-lab download containing `check_environment.py` under `lab1-setup/`. |
| [lab.md](lab.md) | Four steps with checkoffs after the FastFurious comparison and after the new-car predictions, plus paper exploration for Lecture 2. |
| [student-note-template.md](student-note-template.md) | Initial predictions, implementation checks, the FastFurious comparison, new-car results, peer comparison, and look-ahead. |
| [LICENSE](LICENSE) | Terms for the course-authored files and for the car data. |
| [lab1.zip](https://agencyai.mit.edu/lab1/lab1.zip) | In-class download containing 12 project files under `lab1/`. |

## Code and data

| File | Purpose |
|---|---|
| [code/README.md](code/README.md) | Implementation specification, commands, and expected output. |
| [code/DATA.md](code/DATA.md) | Data fields and attribution. |
| [code/cars.tsv](code/cars.tsv) | 392 car records, supplied labels, and source row IDs. |
| [code/baseline.py](code/baseline.py) | Split, evaluation, and output code with scaling and neighbor selection to implement. |
| [code/check_setup.py](code/check_setup.py) | Checks small examples and compares the default run with the reference metrics. |
| [code/new-cars.tsv](code/new-cars.tsv) | Constructed later-years cars, 1982 to 2015, for the closing question. |
| [code/provided-results/reference-metrics.json](code/provided-results/reference-metrics.json) | Reference settings, split IDs, and aggregate results. |
| [code/provided-results/fastfurious-predictions.tsv](code/provided-results/fastfurious-predictions.tsv) | The merger partner's predictions for the Step 3 comparison. |
| [code/.gitignore](code/.gitignore) | Keeps generated runs and Python cache files out of Git. |

## Student outputs

Paths below are relative to the downloaded `lab1/` folder.

| Path | Contents |
|---|---|
| `student-note-template.md` | Completed student notes for the in-class lab. |
| `work/` | Supporting evidence and saved Claude exchanges. |
| `code/runs/` | Generated classifier results. |

The pre-lab writes `setup-result.txt` and `setup-check/input.json` in the separate `lab1-setup/` folder.
