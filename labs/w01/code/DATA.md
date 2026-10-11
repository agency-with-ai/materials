# Data used by the car classifier

`cars.tsv` contains 392 historical vehicle records, with 196 labeled 1 and 196 labeled 0.[^auto-mpg]

## Fields

| Field | Meaning |
|---|---|
| `row_id` | Record identifier. Use it to trace predictions and training neighbors to this table. |
| `label` | 1 when the car's gas use per mile is at or above a fixed threshold, 0 when it is below. The exact threshold is undocumented. |
| `weight` | Vehicle weight in pounds (lb). |
| `cylinders` | Number of engine cylinders. |
| `model_year` | Model year, from 1970 to 1982. |
| `car_name` | Vehicle name. |

## Later-years cars

`new-cars.tsv` holds 214 records for model years 1982 to 2015, with the same columns and row IDs starting at 401. These are constructed records, not measured ones, made for the closing question. A car there is labeled 1 when it uses at least as much gas per mile as the average new vehicle sold that model year, measured against the EPA's reported real-world fuel economy for that year.[^epa-trends]

[^epa-trends]: Estimated real-world fuel economy by model year, Table 2.1 of the [2025 EPA Automotive Trends Report](https://www.epa.gov/automotive-trends), EPA-420-R-26-001. The series runs from 21.1 mpg in 1982 to 24.6 mpg in 2015.

[^auto-mpg]: Adapted from [Auto MPG, R. Quinlan, UCI Machine Learning Repository](https://doi.org/10.24432/C5859H), distributed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This lab uses a classification derivative with binary fuel-economy labels in place of numeric MPG.
