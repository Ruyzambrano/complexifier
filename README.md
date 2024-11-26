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

**Parameters**:
- `word` (str): The original word to potentially alter.

Introduces a 10% chance of a random spelling error in a given word. This function is useful for simulating typos and spelling mistakes in text data.

### `introduce_spag_error(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Applies the create_spag_error function to each string entry in specified columns of a DataFrame, introducing random spelling errors with a 10% probability.

**Parameters**:
- `df` (pd.DataFrame): The DataFrame to alter.
- `columns` (list or str): Column names to apply errors to. Defaults to all string columns.

### `add_or_subtract_outliers(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Randomly adds or subtracts values in specified numeric columns at random indices, simulating outliers between 1% and 10% of the rows.

**Parameters**:
- `df` (pd.DataFrame): The DataFrame to modify.
- `columns` (list or str): Column names to adjust. Defaults to all numeric columns if not specified.

### `add_standard_deviations(df: pd.DataFrame, columns=None, min_std=1, max_std=5) -> pd.DataFrame`

Adds between 1 to 5 standard deviations to random entries in specified numeric columns to simulate data anomalies.

**Parameters**:
- `df` (pd.DataFrame): The DataFrame to manipulate.
- `columns` (list or str): Column names to modify. Defaults to numeric columns if not specified.
- `min_std` (int): Minimum number of standard deviations to add. Defaults to 1
- `max_std` (int): Maximum number of standard deviations to add. Defaults to 5

### `duplicate_rows(df: pd.DataFrame, sample_size=None) -> pd.DataFrame`

Introduces duplicate rows into a DataFrame. This function is useful for testing deduplication processes.

**Parameters**:
- `df` (pd.DataFrame): DataFrame to which duplicates will be added.
- `sample_size` (int): number of rows to duplicate. A random percentage between 1% and 10% if not specified.

### `add_nulls(df: pd.DataFrame, columns=None, min_percent=1, max_percent=10) -> pd.DataFrame`

Inserts null values into specified DataFrame columns. This simulates missing data conditions.

**Parameters**:
- `df` (pd.DataFrame): The DataFrame to modify.
- `columns` (list or str, optional): Specific columns to add nulls to. Defaults to all columns if not specified.
- `min_percent` (int): Minimum percentage of null values to insert. Defaults to 1%
- `max_percent` (int): Maximum percentage of null values to insert. Defaults to 10%

### `mess_it_up(df: pd.DataFrame, columns=None, min_std=1, max_std=5, sample_size=None,min_percent=1, max_percent=10, introduce_spag=True, add_outliers=True, add_std=True, duplicate=True, add_null=True) -> pd.DataFrame`

Adds all (or some) of the above methods. Really messes it up.

**Parameters**:
- `df` (pd.DataFrame): The DataFrame to modify.
- `columns` (list or str, optional): Specific columns to add nulls to. Defaults to all columns if not specified.
- `min_std` (int): Minimum number of standard deviations to add. Defaults to 1
- `max_std` (int): Maximum number of standard deviations to add. Defaults to 5
- `sample_size` (int, optional): Number of rows to duplicate. Randomly selected if not specified.
- `min_percent` (int): Minimum percentage of null values to insert. Defaults to 1%
- `max_percent` (int): Maximum percentage of null values to insert. Defaults to 10%
- `introduce_spag` (bool): Adds spelling and grammar errors into string data. Defaults to True
- `add_outliers` (bool): Adds outliers to numerical data. Defaults to True
- `add_std` (bool): Adds standard deviations to the data. Defaults to True
- `duplicate` (bool): Adds duplicate rows to the data. Defaults to True
- `add_null` (bool): Adds null values to the dataset. Defaults to True
