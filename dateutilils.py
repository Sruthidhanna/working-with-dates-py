# Python Code

"""
This module provides functions to validate dates, calculate the age in days 
from a birthdate to today, and compute the number of days between two dates.
"""

import datetime


def is_valid_date(year, month, day):
    """
    Check if the given year, month, and day form a valid date.
    
    Args:
        year (int): The year component.
        month (int): The month component (1-12).
        day (int): The day component.
    
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False


def age_in_days(year, month, day):
    """
    Calculate age in days from the given birthdate to today's date.
    
    Args:
        year (int): Birth year.
        month (int): Birth month.
        day (int): Birth day.
    
    Returns:
        int: Number of days since birthdate. Returns 0 if the date is invalid 
             or birthdate is in the future.
    """
    if not is_valid_date(year, month, day):
        return 0
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    if birth_date > today:
        return 0
    return (today - birth_date).days


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Calculate the absolute number of days between two dates.
    
    Args:
        year1, month1, day1 (int): The first date.
        year2, month2, day2 (int): The second date.
    
    Returns:
        int: Number of days between the two dates. Returns 0 if either date is invalid.
    """
    if not (is_valid_date(year1, month1, day1) and
            is_valid_date(year2, month2, day2)):
        return 0
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    return abs((date2 - date1).days)

def run_tests():
    print("Testing is_valid_date:")
    print(is_valid_date(2020, 2, 29))  # True (leap year)
    print(is_valid_date(2019, 2, 29))  # False (not leap year)
    print(is_valid_date(2023, 4, 31))  # False (April has 30 days)
    print(is_valid_date(2023, 12, 25)) # True

    print("\nTesting age_in_days:")
    print(age_in_days(2000, 1, 1))     # Should be positive number
    print(age_in_days(3000, 1, 1))     # Future date, expect 0
    print(age_in_days(2023, 2, 29))    # Invalid date, expect 0

    print("\nTesting days_between:")
    print(days_between(2020, 1, 1, 2020, 1, 31))  # 30 days
    print(days_between(2023, 12, 25, 2023, 12, 25)) # 0 days (same day)
    print(days_between(2019, 2, 28, 2019, 3, 1))   # 1 day
    print(days_between(2023, 2, 29, 2023, 3, 1))   # Invalid date, expect 0

if __ name __ == "_main_":
    run_tests()
