# 🗓️ Working with Dates in Python | Coursera project - Rice University

This project is part of the **Python Programming Essentials** course. It demonstrates how to work with date and time using Python's built-in libraries.

## 📚 Overview

The goal of this project is to:
1. Understand Python's `datetime` module.
2. Extract and format date/time information.
3. Perform basic operations with dates, such as finding the difference between two dates.

## 📚 Project Description

The project consists of multiple problems. Each problem will utilize functions you wrote for the previous problems.

 ### Problem 1: Computing the number of days in a month
 
First, you will write a function called days_in_month that takes two integers: a year and a month. The function should return the number of days in that month.  You may assume that both inputs are valid (in other words, you do not need to write any code to check whether or not they are reasonable, you can just assume that the month input is a number between 1 and 12 and the year input is a number between datetime.MINYEAR and datetime.MAXYEAR)

### Problem 2: Checking if a date is valid

Next, you will write a function called is_valid_date that takes three integers: a year, a month, and a day. The function should return 
True if that date is valid and False otherwise. This function should not assume that the inputs are valid. Rather, this function should check that all three inputs combine to form a valid date, with a year between datetime.MINYEAR and datetime.MAXYEAR, a month between 1 and 12, and a day between 1 and the number of days in the given month. Notice that the function days_in_month that you wrote for Part 1 will be useful here!

### Problem 3: Computing the number of days between two dates

Now that we have a way to check if a given date is valid, you will write a function called 
days_between that takes six integers (year1, month1, day1, year2, month2, day2) and returns the number of days from an earlier date (year1-month1-day1) to a later date (year2-month2-day2). If either date is invalid, the function should return 0. Notice that you already wrote a function to determine if a date is valid or not! If the second date is earlier than the first date, the function should also return 0.

### Problem 4: Calculating a person's age in days
Finally, you will write a function called 
age_in_days that takes three integers as input: the year, month, and day of a persons birthday. The function should return that person's age in days as of today. The function should return 0 if the input date is invalid (remember you have a function to check that!). The function should also return 0 if the input date is in the future.

Remember that you already have a function that returns the number of days between two dates that you wrote in Part 3. Which two dates could you pass to that function to solve this problem?


## 🧠 Key Concepts Covered

- Importing `datetime` module
- Creating date objects
- Accessing date components (year, month, day)
- Formatting dates
- Calculating date differences (e.g., age, days until a specific date)

## 🛠️ Technologies Used

- Python 3.x
- `datetime` module



