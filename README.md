# Complexifier

This makes your pandas dataframe even worse

## Dependencies

- `pandas`
- `typo`
- `random`

## Installation

`complexifier` can be installed using `pip`

```sh
pip install complexifier
```

## Usage

Once installed you can use `complexifier` to add mistakes and outliers to your data

This library has several methods available:

### `create_spag_error(word: str) -> str`

Introduces a 10% chance of a random spelling error in a given word. This function is useful for simulating typos and spelling mistakes in text data.

### `introduce_spag_error(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Applies the create_spag_error function to each string entry in specified columns of a DataFrame, introducing random spelling errors with a 10% probability.

**Parameters**:
- `df`: The DataFrame to be altered.
- `columns`: Optional; specify column names to apply errors to. If not provided, it defaults to all string columns.

### `add_or_subtract_outliers(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Randomly adds or subtracts values in specified numeric columns at random indices, simulating outliers between 1% and 10% of the rows.

**Parameters**:
- `df`: DataFrame to be modified.
- `columns`: Optional; specify columns to adjust. 

### `add_standard_deviations(df: pd.DataFrame, columns=None, min_std=1, max_std=5) -> pd.DataFrame`

Adds between 1 to 5 standard deviations to random entries in specified numeric columns to simulate data anomalies.

**Parameters**:
- `df`: The DataFrame to manipulate.
- `columns`: Optional; specify columns to modify.
- `min_std`: Minimum number of standard deviations to add.
- `max_std`: Maximum number of standard deviations to add.

### `duplicate_rows(df: pd.DataFrame, sample_size=None) -> pd.DataFrame`

Introduces duplicate rows into a DataFrame. This function is useful for testing deduplication processes.

**Parameters**:
- `df`: DataFrame where duplicates will be introduced.
- `sample_size`: Optional; number of rows to duplicate. A random percentage between 1% and 10% if not specified.

### `add_nulls(df: pd.DataFrame, columns=None, min_percent=1, max_percent=10) -> pd.DataFrame`

Inserts null values into specified DataFrame columns. This simulates missing data conditions.

**Parameters**:
- `df`: The DataFrame to modify.
- `columns`: Optional; specific columns to add `nulls` to.
- `min_percent`: Minimum percentage of `null` values to insert.
- `max_percent`: Maximum percentage of `null` values to insert.
