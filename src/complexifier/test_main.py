import pytest
import pandas as pd
from .main import (create_spag_error,
                   introduce_spag_error,
                   add_or_subtract_outliers,
                   add_standard_deviations,
                   duplicate_rows,
                   add_nulls)


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


def test_create_spag_error():
    """
    Test that for a word with sufficient length, the function must return a string of same length
    """
    word = "hello"
    error_word = create_spag_error(word)
    assert isinstance(error_word, str)
    assert len(error_word) == len(word)

def test_introduce_spag_error(sample_df):
    """
    Test that DataFrame columns contain the potential spelling errors
    """
    df_with_errors = introduce_spag_error(sample_df, columns='Name')
    assert 'Name' in df_with_errors.columns
    assert all([isinstance(name, str) for name in df_with_errors['Name'].values])

def test_add_or_subtract_outliers(sample_df):
    """
    Test that outliers are added to the numerical columns
    """
    df_with_outliers = add_or_subtract_outliers(sample_df, columns='Salary')
    assert 'Salary' in df_with_outliers.columns
    assert df_with_outliers['Salary'].dtype == float or df_with_outliers['Salary'].dtype == int

def test_add_standard_deviations(sample_df):
    """ 
    Test that standard deviations are added to the Age column
    """
    df_with_deviations = add_standard_deviations(sample_df, columns='Age')
    assert 'Age' in df_with_deviations.columns
    assert df_with_deviations['Age'].dtype == float or df_with_deviations['Age'].dtype == int

def test_duplicate_rows(sample_df):
    """
    Test that duplicate rows are added
    """
    df_with_duplicates = duplicate_rows(sample_df, sample_size=2)
    assert len(df_with_duplicates) == len(sample_df) + 2

def test_add_nulls(sample_df):
    """
    Test that nulls are added to the DataFrame
    """
    df_with_nulls = add_nulls(sample_df, columns='City', min_percent=20, max_percent=30)
    assert 'City' in df_with_nulls.columns
    assert df_with_nulls['City'].isnull().sum() > 0
