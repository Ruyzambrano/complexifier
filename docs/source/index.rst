Complexifier
=============

Make your pandas even worse!

Complexifier is a Python library crafted to transform clean datasets into messy versions by introducing random errors and anomalies. This is particularly useful for educational purposes, where students learn to clean data through practical experience.

Problem
-------

When teaching students to work with data, an important lesson is how to clean it.

The problem with this is that there are two types of datasets available on the internet:

1. Data that is good, but already cleaned
2. Data that is not cleaned, but is terrible and incomprehensible

Complexifier solves this problem by allowing you to take the former and turn it into a better version of the latter!

Dependencies
------------

Complexifier relies on the following packages:

- `pandas`
- `typo`
- `random`

Ensure these dependencies are installed in your environment.

Installation
------------

You can install `complexifier` via `pip`:

.. code-block:: sh

    pip install complexifier

Usage
-----

Once installed, use `complexifier` to add mistakes and simulate anomalies in your data. This library provides several methods:

Methods
-------

create_spag_error
~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_spag_error(word: str) -> str

Introduces a 10% chance of a random spelling error in a given word, helpful for simulating typos.

**Parameters**:

- `word` (str): The original word to potentially alter.  

introduce_spag_error
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    introduce_spag_error(df: pd.DataFrame, columns=None) -> pd.DataFrame

Applies `create_spag_error` to each string entry in specified DataFrame columns, introducing random spelling errors with a 10% probability.

**Parameters**:

- `df` (pd.DataFrame): The DataFrame to alter.  

- `columns` (list or str): Column names to apply errors to. Defaults to all string columns.  

add_or_subtract_outliers
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    add_or_subtract_outliers(df: pd.DataFrame, columns=None) -> pd.DataFrame  

Randomly adds or subtracts values in specified numeric columns, simulating outliers in 1% to 10% of rows.

**Parameters**:

- `df` (pd.DataFrame): The DataFrame to modify.  

- `columns` (list or str): Column names to adjust. Defaults to all numeric columns if not specified.  

add_standard_deviations
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    add_standard_deviations(df: pd.DataFrame, columns=None, min_std=1, max_std=5) -> pd.DataFrame  

Adds between 1 to 5 standard deviations to random entries in numeric columns to simulate data anomalies.

**Parameters**:

- `df` (pd.DataFrame): The DataFrame to manipulate.  

- `columns` (list or str): Column names to modify. Defaults to numeric columns if not specified.  

- `min_std` (int): Minimum number of standard deviations to add. Defaults to 1.  

- `max_std` (int): Maximum number of standard deviations to add. Defaults to 5.  

duplicate_rows
~~~~~~~~~~~~~~

.. code-block:: python

    duplicate_rows(df: pd.DataFrame, sample_size=None) -> pd.DataFrame

Introduces duplicate rows into a DataFrame, useful for testing deduplication processes.

**Parameters**:

- `df` (pd.DataFrame): DataFrame to which duplicates will be added.  

- `sample_size` (int): Number of rows to duplicate. A random percentage between 1% and 10% if not specified.  

add_nulls
~~~~~~~~~

.. code-block:: python

    add_nulls(df: pd.DataFrame, columns=None, min_percent=1, max_percent=10) -> pd.DataFrame  

Inserts null values into specified DataFrame columns, simulating missing data conditions.

**Parameters**:

- `df` (pd.DataFrame): The DataFrame to modify.  

- `columns` (list or str): Specific columns to add nulls to. Defaults to all columns if not specified.  

- `min_percent` (int): Minimum percentage of null values to insert. Defaults to 1%.  

- `max_percent` (int): Maximum percentage of null values to insert. Defaults to 10%.  

mess_it_up
~~~~~~~~~~

.. code-block:: python

    mess_it_up(df: pd.DataFrame, columns=None, min_std=1, max_std=5, sample_size=None, min_percent=1, max_percent=10, 
               introduce_spag=True, add_outliers=True, add_std=True, duplicate=True, add_null=True) -> pd.DataFrame

Integrates all methods to add errors comprehensively to the DataFrame.

**Parameters**:

- `df` (pd.DataFrame): The DataFrame to modify.  

- `columns` (list or str): Specific columns to add nulls to. Defaults to all columns if not specified.  

- `min_std` (int): Minimum number of standard deviations to add. Defaults to 1.  

- `max_std` (int): Maximum number of standard deviations to add. Defaults to 5.  

- `sample_size` (int): Number of rows to duplicate. Randomly selected if not specified.  

- `min_percent` (int): Minimum percentage of null values to insert. Defaults to 1%.  

- `max_percent` (int): Maximum percentage of null values to insert. Defaults to 10%.  

- `introduce_spag` (bool): Adds spelling and grammar errors into string data. Defaults to True.  

- `add_outliers` (bool): Adds outliers to numerical data. Defaults to True.  

- `add_std` (bool): Adds standard deviations to the data. Defaults to True.  

- `duplicate` (bool): Adds duplicate rows to the data. Defaults to True.  

- `add_null` (bool): Adds null values to the dataset. Defaults to True.  

Contributing
------------

Feel free to contribute by submitting a pull request on GitHub. For large changes, please open an issue to discuss before implementing changes.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Contact Information
-------------------

For support or inquiries, please contact Ruy at ruyzambrano@gmail.com

Changelog
---------

Version 0.3.1

Badges
------

.. image:: https://img.shields.io/badge/build-passing-brightgreen
    :target: https://github.com/yourusername/complexifier

.. image:: https://img.shields.io/badge/coverage-95%25-green
    :target: https://codecov.io/gh/yourusername/complexifier
