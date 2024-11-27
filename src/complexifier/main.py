import random
from typo import StrErrer
import pandas as pd

def create_spag_error(word: str) -> str:
    """
    Gives a 10% chance to introduce a spelling error to a word.

    :param word: The original word to potentially alter.
    :type word: str
    :return: The original word or a word with a random spelling error.
    :rtype: str
    """
    if len(word) < 3:
        return word
    error_object = StrErrer(word)
    weight = random.randint(1, 100)
    match weight:
        case 1:
            return error_object.missing_char().result
        case 2:
            return error_object.char_swap().result
        case 3:
            return error_object.extra_char().result
        case 4:
            return error_object.nearby_char().result
        case 5:
            return error_object.similar_char().result
        case 6:
            return error_object.random_space().result
        case 7:
            return error_object.repeated_char().result
        case 8:
            return word.lower()
        case 9:
            return word.upper()
        case 10:
            return "".join(
                [char.upper() if random.randint(0, 100) < 10 else char for char in word]
            )
        case _:
            return word

def introduce_spag_error(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Applies random spelling errors to specified columns in a DataFrame.

    :param df: The DataFrame to alter.
    :type df: pd.DataFrame
    :param columns: Column names to apply errors to. Defaults to all string columns.
    :type columns: list or str, optional
    :return: The DataFrame with potential spelling errors introduced.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if not columns:
        columns = df.select_dtypes(include=["string", "object"]).columns
    elif isinstance(columns, str):
        columns = [columns]
    elif not isinstance(columns, list):
        raise TypeError(f"Columns is type {type(columns)} but expected str or list")

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"{col} not in DataFrame")
        if not pd.api.types.is_string_dtype(df[col]):
            raise TypeError(f"{col} is {df[col].dtype}, not a string type")
        df[col] = df[col].apply(create_spag_error)
    return df

def add_or_subtract_outliers(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """
    Adds or subtracts a random integer in columns of between 1% and 10% of the rows.

    :param df: The DataFrame to modify.
    :type df: pd.DataFrame
    :param columns: Column names to adjust. Defaults to all numeric columns if not specified.
    :type columns: list or str, optional
    :return: The DataFrame with outliers added.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if not columns:
        columns = df.select_dtypes(include="number").columns
    elif isinstance(columns, str):
        columns = [columns]
    elif not isinstance(columns, list):
        raise TypeError(f"Columns is type {type(columns)} but expected str or list")

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"{col} is not a column.")
        data_range = round(df[col].max() - df[col].min())
        random_indices = df.sample(
            random.randint(len(df[col] // 100), len(df[col] // 10))
        ).index
        df.loc[random_indices, col] = df.loc[random_indices, col].apply(
            lambda row: row + random.randint(-2 * data_range, 2 * data_range)
        )
    return df

def add_standard_deviations(df: pd.DataFrame, columns=None, min_std=1, max_std=5) -> pd.DataFrame:
    """
    Adds random deviations to entries in specified numeric columns to simulate data anomalies.

    :param df: The DataFrame to manipulate.
    :type df: pd.DataFrame
    :param columns: Column names to modify. Defaults to numeric columns if not specified.
    :type columns: list or str, optional
    :param min_std: Minimum number of standard deviations to add. Defaults to 1
    :type min_std: int, optional
    :param max_std: Maximum number of standard deviations to add. Defaults to 5
    :type max_std: int, optional
    :return: The DataFrame with deviations added.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if not columns:
        columns = df.select_dtypes(include="number").columns
    elif isinstance(columns, str):
        columns = [columns]
    elif not isinstance(columns, list):
        raise TypeError(f"Columns is type {type(columns)} but expected str or list")

    for col in columns:
        if col not in df.columns:
            raise ValueError(f"{col} is not a column.")
        sample_size = random.randint(len(df[col]) // 100, len(df[col]) // 10)
        standard_deviation = df[col].std()
        random_indices = df.sample(sample_size).index
        df.loc[random_indices, col] = df.loc[random_indices, col].apply(
            lambda row: row
            + random.randint(min_std, max_std)
            * standard_deviation
            * random.choice([1, -1])
        )
    return df

def duplicate_rows(df: pd.DataFrame, sample_size=None) -> pd.DataFrame:
    """
    Adds duplicate rows to a DataFrame.

    :param df: DataFrame to which duplicates will be added.
    :type df: pd.DataFrame
    :param sample_size: Number of rows to duplicate. A random percentage between 1% and 10% if not specified.
    :type sample_size: int, optional
    :return: The DataFrame with duplicate rows added.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if not sample_size:
        sample_size = random.randint(len(df) // 100, len(df) // 10)
    new_rows = df.sample(sample_size)
    return pd.concat([df, new_rows])

def add_nulls(df: pd.DataFrame, columns=None, min_percent=1, max_percent=10) -> pd.DataFrame:
    """
    Inserts null values into specified DataFrame columns.

    :param df: The DataFrame to modify.
    :type df: pd.DataFrame
    :param columns: Specific columns to add nulls to. Defaults to all columns if not specified.
    :type columns: list or str, optional
    :param min_percent: Minimum percentage of null values to insert. Defaults to 1%
    :type min_percent: int, optional
    :param max_percent: Maximum percentage of null values to insert. Defaults to 10%
    :type max_percent: int, optional
    :return: The DataFrame with null values inserted.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if columns == []:
        columns = df.columns.to_list()
    if not columns:
        columns = df.columns
    elif isinstance(columns, str):
        columns = [columns]
    elif not isinstance(columns, list):
        raise TypeError(f"Columns is type {type(columns)} but expected str or list")

    for col in columns:
        chosen_percent = random.randint(min_percent, max_percent) / 100
        sample_size = round(len(df) * chosen_percent)
        if sample_size == 0:
            sample_size = 1
        indices_to_none = df.sample(sample_size).index
        df.loc[indices_to_none, col] = None
    return df

def mess_it_up(df: pd.DataFrame, columns=None, min_std=1, max_std=5, sample_size=None,
               min_percent=1, max_percent=10, introduce_spag=True, add_outliers=True,
               add_std=True, duplicate=True, add_null=True) -> pd.DataFrame:
    """
    Applies several functions to add outliers, spelling errors and null values

    :param df: The DataFrame to modify.
    :type df: pd.DataFrame
    :param columns: Specific columns to modify. Defaults to all columns if not specified.
    :type columns: list or str, optional
    :param min_std: Minimum number of standard deviations to add. Defaults to 1
    :type min_std: int, optional
    :param max_std: Maximum number of standard deviations to add. Defaults to 5
    :type max_std: int, optional
    :param sample_size: Number of rows to duplicate. Randomly selected if not specified.
    :type sample_size: int, optional
    :param min_percent: Minimum percentage of null values to insert. Defaults to 1%
    :type min_percent: int, optional
    :param max_percent: Maximum percentage of null values to insert. Defaults to 10%
    :type max_percent: int, optional
    :param introduce_spag: Adds spelling and grammar errors into string data. Defaults to True
    :type introduce_spag: bool, optional
    :param add_outliers: Adds outliers to numerical data. Defaults to True
    :type add_outliers: bool, optional
    :param add_std: Adds standard deviations to the data. Defaults to True
    :type add_std: bool, optional
    :param duplicate: Adds duplicate rows to the data. Defaults to True
    :type duplicate: bool, optional
    :param add_null: Adds null values to the dataset. Defaults to True
    :type add_null: bool, optional
    :return: The modified DataFrame.
    :rtype: pd.DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Must be a pandas")
    if df.empty:
        return df
    if columns == []:
        columns = df.columns.to_list()
    if not columns:
        columns = df.columns.to_list()
    elif isinstance(columns, str):
        columns = [columns]
    elif not isinstance(columns, list):
        raise TypeError(f"Columns is type {type(columns)} but expected str or list")

    string_cols = df[columns].select_dtypes(include="string").columns.to_list()
    numeric_cols = df[columns].select_dtypes(include="number").columns.to_list()
    if string_cols:
        if introduce_spag:
            df = introduce_spag_error(df, string_cols)
    if numeric_cols:
        if add_outliers:
            df = add_or_subtract_outliers(df, numeric_cols)
        if add_std:
            df = add_standard_deviations(df, numeric_cols, min_std, max_std)
    if duplicate:
        df = duplicate_rows(df, sample_size)
    if add_null:
        df = add_nulls(df, columns, min_percent, max_percent)
    return df
