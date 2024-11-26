# Complexifier

Make your pandas even worse!

## Problem

When teaching students to work with data, an important lesson is how to clean it.

The problem with this is that there are two types of datasets available on the internet:

1. Data that is good, but already cleaned
2. Data that is not cleaned, but is terrible and incomprehensible

Complexifier solves this problem by allowing you take the former and turn it into a better version of the latter!

## Dependencies

- `pandas`
- `typo`
- `random`

## Installation

`complexifier` can be installed using `pip`

```sh
pip install complexifier
```

## Documentation

[Go to the documentation](https://ruyzambrano.github.io/complexifier/)

## Usage


Once installed you can use `complexifier` to add mistakes and outliers to your data

This library has several methods available:

### create_spag_error

`create_spag_error(word: str) -> str`

Introduces a 10% chance of a random spelling error in a given word. This function is useful for simulating typos and spelling mistakes in text data.

### introduce_spag_error

`introduce_spag_error(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Applies the create_spag_error function to each string entry in specified columns of a DataFrame, introducing random spelling errors with a 10% probability.

### add_or_subtract_outliers

`add_or_subtract_outliers(df: pd.DataFrame, columns=None) -> pd.DataFrame`

Randomly adds or subtracts values in specified numeric columns at random indices, simulating outliers between 1% and 10% of the rows.

### add_standard_deviations

`add_standard_deviations(df: pd.DataFrame, columns=None, min_std=1, max_std=5) -> pd.DataFrame`

Adds between 1 to 5 standard deviations to random entries in specified numeric columns to simulate data anomalies.

### duplicate_rows

`duplicate_rows(df: pd.DataFrame, sample_size=None) -> pd.DataFrame`

Introduces duplicate rows into a DataFrame. This function is useful for testing deduplication processes.

### add_nulls

`add_nulls(df: pd.DataFrame, columns=None, min_percent=1, max_percent=10) -> pd.DataFrame`

Inserts null values into specified DataFrame columns. This simulates missing data conditions.

### mess_it_up

`mess_it_up(df: pd.DataFrame, columns=None, min_std=1, max_std=5, sample_size=None,min_percent=1, max_percent=10, introduce_spag=True, add_outliers=True, add_std=True, duplicate=True, add_null=True) -> pd.DataFrame`

Adds all (or some) of the above methods. Really messes it up.
