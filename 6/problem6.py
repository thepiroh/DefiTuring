import math

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    print(s)


def problem6():
    sum_digits(math.factorial(2013))
problem6()
