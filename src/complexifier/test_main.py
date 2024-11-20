import pytest
import pandas as pd
from math import floor
from .main import (
    create_spag_error,
    introduce_spag_error,
    add_or_subtract_outliers,
    add_standard_deviations,
    duplicate_rows,
    add_nulls
)

@pytest.fixture
def sample_df():
    """
    A fixture for tests
    """
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [28, 34, 29, 42, 25],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Salary': [70000, 80000, 72000, 95000, 67000]
    })

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

@pytest.mark.parametrize("column_name,min_percent,max_percent", [
    ("City", 10, 20), 
    ("Name", 20, 30)
])
def test_add_nulls(sample_df, column_name, min_percent, max_percent):
    """
    Test that nulls are added to the DataFrame
    """
    df_with_nulls = add_nulls(sample_df, columns=column_name, min_percent=min_percent, max_percent=max_percent)
    assert column_name in df_with_nulls.columns
    null_count = df_with_nulls[column_name].isnull().sum()
    print(df_with_nulls)
    assert float(null_count) >= 0.0
    assert (min_percent*0.01*len(sample_df)) <= null_count <= round(max_percent*0.01*len(sample_df))
