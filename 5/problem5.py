def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    print(s)


def problem5():
    sum_digits(2**2222)
problem5()
