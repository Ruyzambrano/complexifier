import pytest
from unittest.mock import patch
import pandas as pd
from math import floor
from .main import (
    create_spag_error,
    introduce_spag_error,
    add_or_subtract_outliers,
    add_standard_deviations,
    duplicate_rows,
    add_nulls,
    mess_it_up,
)


@pytest.fixture
def sample_df():
    """
    A fixture for tests
    """
    return pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
            "Age": [28, 34, 29, 42, 25],
            "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
            "Salary": [70000, 80000, 72000, 95000, 67000],
        }
    )


@pytest.mark.parametrize("word", ["hello", "world", "testword"])
def test_create_spag_error(word):
    """
    Tests that the word returned is still a string
    """
    error_word = create_spag_error(word)
    assert isinstance(error_word, str)


@pytest.mark.parametrize("column_name", ["Name", "City"])
def test_introduce_spag_error(sample_df, column_name):
    """
    Test that DataFrame columns contain the potential spelling errors
    """
    df_with_errors = introduce_spag_error(sample_df, columns=column_name)
    assert column_name in df_with_errors.columns
    assert all([isinstance(name, str) for name in df_with_errors[column_name].values])


@pytest.mark.parametrize("column_name", ["Salary"])
def test_add_or_subtract_outliers(sample_df, column_name):
    """
    Test that outliers are added to the numerical columns
    """
    df_with_outliers = add_or_subtract_outliers(sample_df, columns=column_name)
    assert column_name in df_with_outliers.columns
    assert pd.api.types.is_numeric_dtype(df_with_outliers[column_name])


@pytest.mark.parametrize("column_name", ["Age", "Salary"])
def test_add_standard_deviations(sample_df, column_name):
    """
    Test that standard deviations are added to the specified column
    """
    df_with_deviations = add_standard_deviations(sample_df, columns=column_name)
    assert column_name in df_with_deviations.columns
    assert pd.api.types.is_numeric_dtype(df_with_deviations[column_name])


@pytest.mark.parametrize("sample_size", [0, 2, 5])
def test_duplicate_rows(sample_df, sample_size):
    """
    Test that duplicate rows are added
    """
    df_with_duplicates = duplicate_rows(sample_df, sample_size=sample_size)
    assert len(df_with_duplicates) == len(sample_df) + sample_size


@pytest.mark.parametrize(
    "column_name,min_percent,max_percent", [("City", 10, 20), ("Name", 20, 30)]
)
def test_add_nulls(sample_df, column_name, min_percent, max_percent):
    """
    Test that nulls are added to the DataFrame
    """
    df_with_nulls = add_nulls(
        sample_df, columns=column_name, min_percent=min_percent, max_percent=max_percent
    )
    assert column_name in df_with_nulls.columns
    null_count = df_with_nulls[column_name].isnull().sum()
    print(df_with_nulls)
    assert float(null_count) >= 0.0
    assert (
        (min_percent * 0.01 * len(sample_df))
        <= null_count
        <= round(max_percent * 0.01 * len(sample_df))
    )


def test_mess_it_up(sample_df):
    """
    Tests the mess_it_up_function
    """
    df_messed_up = mess_it_up(
        sample_df,
        columns=["Name", "Age", "City", "Salary"],
        min_std=1,
        max_std=2,
        sample_size=2,
        min_percent=10,
        max_percent=20,
    )

    # Check that the specified number of duplicate rows has been added
    assert (
        len(df_messed_up) == len(sample_df) + 2
    ), "Unexpected number of duplicate rows"

    # Check for potential null values
    for col in ["Name", "Age", "City", "Salary"]:
        null_count = df_messed_up[col].isnull().sum()
        assert null_count > 0, f"No nulls introduced in {col} column"


@pytest.mark.parametrize(
    "columns,min_std,max_std,sample_size,min_percent,max_percent",
    [
        (["Name", "Age"], 1, 2, 2, 10, 20),
        (["City", "Salary"], 2, 4, 3, 15, 25),
        (["Name", "City", "Age"], 1, 3, 1, 5, 10),
    ],
)
def test_parameterised_mess_it_up(
    sample_df, columns, min_std, max_std, sample_size, min_percent, max_percent
):
    """
    Tests the mess_it_up function with different configurations
    """
    df_messed_up = mess_it_up(
        sample_df,
        columns=columns,
        min_std=min_std,
        max_std=max_std,
        sample_size=sample_size,
        min_percent=min_percent,
        max_percent=max_percent,
    )

    # Check that the specified number of duplicate rows has been added
    assert (
        len(df_messed_up) == len(sample_df) + sample_size
    ), "Unexpected number of duplicate rows"

    # Check for potential null values
    for col in columns:
        null_count = df_messed_up[col].isnull().sum()
        assert null_count > 0, f"No nulls introduced in {col} column"


def test_empty_dataframe_introduce_spag_error():
    """
    Test introduce_spag_error with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["Name"])
    df_spag = introduce_spag_error(empty_df, columns="Name")
    assert df_spag.empty


def test_empty_dataframe_add_or_subtract_outliers():
    """
    Test add_or_subtract_outliers with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["Salary"])
    df_outliers = add_or_subtract_outliers(empty_df, columns="Salary")
    assert df_outliers.empty


def test_empty_dataframe_add_standard_deviations():
    """
    Test add_standard_deviations with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["Age"])
    df_deviations = add_standard_deviations(empty_df, columns="Age")
    assert df_deviations.empty


def test_empty_dataframe_duplicate_rows():
    """
    Test duplicate_rows with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["Name", "Age"])
    df_duplicates = duplicate_rows(empty_df, sample_size=2)
    assert df_duplicates.empty


def test_empty_dataframe_add_nulls():
    """
    Test add_nulls with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["City"])
    df_nulls = add_nulls(empty_df, columns="City", min_percent=10, max_percent=20)
    assert df_nulls.empty


def test_empty_dataframe_mess_it_up():
    """
    Test mess_it_up with an empty DataFrame
    """
    empty_df = pd.DataFrame(columns=["Name", "Age", "City", "Salary"])
    df_messed = mess_it_up(empty_df, columns=["Name", "Age", "City", "Salary"])
    assert df_messed.empty


def test_nonexistent_column_introduce_spag_error(sample_df):
    """
    Test introduce_spag_error with a nonexistent column
    """
    with pytest.raises(ValueError):
        introduce_spag_error(sample_df, columns="Nonexistent")


def test_nonexistent_column_add_or_subtract_outliers(sample_df):
    """
    Test add_or_subtract_outliers with a nonexistent column
    """
    with pytest.raises(ValueError):
        add_or_subtract_outliers(sample_df, columns="Nonexistent")


def test_nonexistent_column_add_standard_deviations(sample_df):
    """
    Test add_standard_deviations with a nonexistent column
    """
    with pytest.raises(ValueError):
        add_standard_deviations(sample_df, columns="Nonexistent")


def test_mixed_data_types_introduce_spag_error():
    """
    Test introduce_spag_error with mixed data types
    """
    mixed_df = pd.DataFrame(
        {
            "String": ["A", "B", "C"],
            "Integer": [1, 2, 3],
            "Float": [0.1, 0.2, 0.3],
            "DateTime": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        }
    )
    df_spag = introduce_spag_error(mixed_df, columns="String")
    assert "String" in df_spag.columns


def test_mixed_data_types_add_or_subtract_outliers():
    """
    Test add_or_subtract_outliers with mixed data types
    """
    mixed_df = pd.DataFrame(
        {
            "String": ["A", "B", "C"],
            "Integer": [1, 2, 3],
            "Float": [0.1, 0.2, 0.3],
            "DateTime": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        }
    )
    df_outliers = add_or_subtract_outliers(mixed_df, columns="Integer")
    assert "Integer" in df_outliers.columns


def test_mixed_data_types_add_standard_deviations():
    """
    Test add_standard_deviations with mixed data types
    """
    mixed_df = pd.DataFrame(
        {
            "String": ["A", "B", "C"],
            "Integer": [1, 2, 3],
            "Float": [0.1, 0.2, 0.3],
            "DateTime": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
        }
    )
    df_deviations = add_standard_deviations(mixed_df, columns="Float")
    assert "Float" in df_deviations.columns
