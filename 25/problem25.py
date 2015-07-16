def problem25():
    def fib(n, computed = {0: 0, 1: 1}):
        if n not in computed:
            computed[n] = fib(n-1, computed) + fib(n-2, computed)
        return computed[n]

    i=0
    while True:
        i+=1
        if len(str(fib(i))) == 2013:
            print("rang:{0}, fib: {1}".format(i, fib(i)))
            break

problem25()

# Alerte Spoiler:
# réponse = 9630
