# Python Expense Tracker

## Overview
The Expense Tracker is a menu-driven command-line application built using Python. It allows users to record expenses, view saved records, filter expenses, and calculate spending totals by category.

## Features
- Add expenses with a date, category, description, and amount.
- View all recorded expenses.
- Filter expenses by category or date.
- Calculate category-wise totals and the grand total.
- Store records in a CSV file so they persist after restarting the program.
- Validate dates and positive expense amounts.
- Handle invalid menu selections and common file errors.

## Technologies Used
- Python 3
- `csv` for reading and writing records
- `datetime` for date validation
- `decimal` for accurate monetary calculations

## Project Files
- `expense_tracker.py` — application source code.
- `expenses.csv` — sample expense records.
- `README.md` — project documentation.

## How to Run
1. Install Python 3 if it is not already installed.
2. Place the project files in the same folder.
3. Open a terminal in that folder.
4. Run:

   `python expense_tracker.py`

5. Select an option from the menu.

## Sample Data
The included CSV file contains ten fictional expense records across Food, Transport, Shopping, Entertainment, and Bills.

## Problem Fixed
One issue addressed was losing expense records when the program closed. Saving each new expense directly to a CSV file ensures that records remain available the next time the program runs.

## Future Improvements
- Monthly expense reports.
- Budget limits and overspending alerts.
- Charts showing spending by category.
- Exporting filtered expenses to a separate CSV file.
