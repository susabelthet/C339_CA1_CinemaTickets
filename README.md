# C339 CA1 – Cinema Ticket System (Project 04)

Unit tests for the Cinema Ticket System, written with pytest and run automatically with GitHub Actions.

## Functions tested
- `ticket_price(ticket_count)` in `src/cinema_price.py`: total price at 1200 cents per ticket
- `can_watch(age)` in `src/cinema_entry.py`: entry allowed for age 16 or older

## Project structure
- `src/`: source code
- `tests/`: pytest unit tests
- `.github/workflows/tests.yml`: GitHub Actions workflow

## How to run the tests
    python -m pip install -r requirements.txt
    python -m pytest -v --cov=src --cov-report=term-missing

## Test results
30 tests: 28 passed, 2 failed (defects found in the source code)
- `ticket_price(0)` returns 1200 instead of 0
- `can_watch(16)` returns False instead of True

## Author
Su Sabel Thet (25036559)