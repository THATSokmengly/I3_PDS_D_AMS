
# (a) Check whether a year is a leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# (b) Return the number of days in a month
def days_in_month(month, year):
    if month < 1 or month > 12:
        return None

    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

# (c) Print whether the years are leap years
years = [1900, 2000, 2024, 2026]

for year in years:
    print(year, "is a leap year:", is_leap(year))

# (d) Count leap years from 2000 to 2100, inclusive
count = 0

for year in range(2000, 2101):
    if is_leap(year):
        count += 1

print("Number of leap years:", count)
