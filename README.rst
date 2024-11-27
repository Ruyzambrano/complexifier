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

.. autofunction:: complexifier.create_spag_error

introduce_spag_error
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: complexifier.introduce_spag_error

add_or_subtract_outliers
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: complexifier.add_or_subtract_outliers

add_standard_deviations
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: complexifier.add_standard_deviations

duplicate_rows
~~~~~~~~~~~~~~

.. autofunction:: complexifier.duplicate_rows

add_nulls
~~~~~~~~~

.. autofunction:: complexifier.add_nulls

mess_it_up
~~~~~~~~~~

.. autofunction:: complexifier.mess_it_up

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

Version 0.3.3

Badges
------

.. image:: https://github.com/ruyzambrano/complexifier/workflows/Test/badge.svg
    :target: https://github.com/ruyzambrano/complexifier/actions

