"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""


def pos_neg(a, b, negative):
    if a == pos
    b ==neg
    print('True')

    else
    print('False')



# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""


def leap_year(year):
year = int(input('What year do you want to enter?'))
year = year / 4 or year / 40

if year % 1:
    print('It is a leap year')

elif year / 100
    print('It is not a leap year')


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))




"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------

"""


def sum_squares(n):
    n = 0
    for i in range(1,n)
        n = (n + i) **




# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))
