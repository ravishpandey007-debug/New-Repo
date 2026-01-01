# Copilot Instructions for New-Repo

## Overview
This repository contains scripts for processing customer, product, and sales data. The main script, `Graded_Assignment_2.py`, performs data cleaning and normalization on customer data from `customers_raw.csv`.

## Architecture
- **Data Sources**: The project relies on three main CSV files:
  - `customers_raw.csv`: Contains customer information.
  - `products_raw.csv`: Contains product details.
  - `sales_raw.csv`: Contains sales transaction records.

- **Data Processing**: The primary processing is done in `Graded_Assignment_2.py`, which:
  - Loads customer data.
  - Cleans and normalizes the data (e.g., removing duplicates, cleaning phone numbers).
  - Saves the cleaned data to `Cleaned_customers_rav.csv`.

## Developer Workflows
- **Running the Script**: Execute `Graded_Assignment_2.py` using Python. Ensure that the required libraries (`pandas`, `phonenumbers`) are installed.
- **Testing**: There are no explicit tests defined in this repository. Consider adding unit tests for the data cleaning functions.

## Project Conventions
- **Data Cleaning**: The script uses specific methods for cleaning data, such as:
  - Removing rows with missing emails.
  - Normalizing phone numbers to E.164 format.
- **File Naming**: Output files are prefixed with `Cleaned_` to indicate processed data.

## Integration Points
- **External Libraries**: The project uses `pandas` for data manipulation and `phonenumbers` for phone number validation and formatting.
- **Data Flow**: Data flows from raw CSV files to cleaned CSV outputs, with transformations applied in between.

## Examples
- **Phone Number Cleaning**: The `clean_phone` function demonstrates how to validate and format phone numbers.
- **Data Normalization**: The script normalizes column names by stripping whitespace and converting to lowercase.

## Conclusion
This document serves as a guide for AI agents to understand the structure and workflows of the New-Repo project. For further enhancements, consider documenting additional workflows and integration points as they arise.