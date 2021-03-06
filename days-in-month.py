# Given a string with a month and a year (separated by a space), 
# return the number of days in that month.

# Leap years are a bit tricky. A year is a leap year if and only if:

# it is evenly divisible by 4
# except if it is divisible by 100, in which case it isn’t
# except if it is divisible by 400, in which case it is
# So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 
# 2000 is divisible by 400, so it was.


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


# The Input
# The month will be given as a number.

# >>> for i in range(1, 13):
# ...     date = str(i) + " 2016"
# ...     print "%s has %s days." % (date, days_in_month(date))
# 1 2016 has 31 days.
# 2 2016 has 29 days.
# 3 2016 has 31 days.
# 4 2016 has 30 days.
# 5 2016 has 31 days.
# 6 2016 has 30 days.
# 7 2016 has 31 days.
# 8 2016 has 31 days.
# 9 2016 has 30 days.
# 10 2016 has 31 days.
# 11 2016 has 30 days.
# 12 2016 has 31 days.

# >>> days_in_month("02 2015")
# 28



def days_in_month(date):
    """How many days are there in a month?"""

    # START SOLUTION

    month, year = date.split()
    month = int(month)
    year = int(year)

    # Account for February

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31

    if month in {4, 6, 9, 11}:
        return 30



