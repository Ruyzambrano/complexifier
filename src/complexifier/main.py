import random

from typo import StrErrer
import pandas as pd

def create_spag_error(word: str) -> str:
    """Gives a 10% chance to introduce a spelling error to a word.

    Args:
        word (str): The original word to potentially alter.

    Returns:
        str: The original word or a word with a random spelling error.
    """
    if len(word) < 3:
        return word
    error_object = StrErrer(word)
    weight = random.randint(1, 100)
    match weight:
        case 1:
            return error_object.missing_char()
        case 2:
            return error_object.char_swap()
        case 3:
            return error_object.extra_char()
        case 4:
            return error_object.nearby_char()
        case 5:
            return error_object.similar_char()
        case 6:
            return error_object.random_space()
        case 7:
            return error_object.repeated_char()
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
    """Applies random spelling errors to specified columns in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to alter.
        columns (list or str, optional): Column names to apply errors to. If not provided, defaults to all string columns.

    Returns:
        pd.DataFrame: The DataFrame with potential spelling errors introduced.
    """
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
    """Adds or subtracts a random integer in columns of between 1% and 10% of the rows.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        columns (list or str, optional): Column names to adjust. Defaults to numeric columns if not specified.

    Returns:
        pd.DataFrame: The DataFrame with outliers added.
    """
    if not columns:
        columns = df.select_dtypes(include="number").columns
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


def add_standard_deviations(
    df: pd.DataFrame, columns=None, min_std=1, max_std=5
) -> pd.DataFrame:
    """Adds random deviations to entries in specified numeric columns to simulate data anomalies.

    Args:
        df (pd.DataFrame): The DataFrame to manipulate.
        columns (list or str, optional): Column names to modify. Defaults to numeric columns if not specified.
        min_std (int): Minimum number of standard deviations to add.
        max_std (int): Maximum number of standard deviations to add.

    Returns:
        pd.DataFrame: The DataFrame with deviations added.
    """
    if not columns:
        columns = df.select_dtypes(include="number").columns

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
    """Adds duplicate rows to a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to which duplicates will be added.
        sample_size (int, optional): Number of rows to duplicate. Randomly selected if not specified.

    Returns:
        pd.DataFrame: The DataFrame with duplicate rows added.
    """
    if not sample_size:
        sample_size = random.randint(len(df[col]) // 100, len(df[col]) // 10)
    new_rows = df.sample(sample_size)
    return pd.concat([df, new_rows])


def add_nulls(
    df: pd.DataFrame, columns=None, min_percent=1, max_percent=10
) -> pd.DataFrame:
     """Inserts null values into specified DataFrame columns.

    Args:
        df (pd.DataFrame): The DataFrame to modify.
        columns (list or str, optional): Specific columns to add nulls to. Defaults to all columns if not specified.
        min_percent (int): Minimum percentage of null values to insert.
        max_percent (int): Maximum percentage of null values to insert.

    Returns:
        pd.DataFrame: The DataFrame with null values inserted.
    """
    if not columns:
        columns = df.columns
    for col in columns:
        indices_to_none = df.sample(
            len(df) * random.randint(min_percent, max_percent) // 100
        ).index
        df.loc[indices_to_none, col] = None
    return df

