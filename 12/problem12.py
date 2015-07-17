def factors(n):
        l1, l2 = [], []
        for i in range(1, int(n ** 0.5) + 1):
            q,r = n//i, n%i     # Alter: divmod() fn can be used.
            if r == 0:
                l1.append(i)
                l2.append(q)    # q's obtained are decreasing.
        if l1[-1] == l2[-1]:    # To avoid duplication of the possible factor sqrt(n)
            l1.pop()
        l2.reverse()
        l3 = l1 + l2
        return l3

def triangulaire(x):
    return x*(x-1)/2

def problem12():

    for i in range(5000, 10000000):
        #print("i = {}".format(i))
        #print(len(factors(triangulaire(i))))
        if len(factors(triangulaire(i))) > 1000:
            print("C'est lui: {}".format(triangulaire(i)))
            break

problem12()

# Alerte Spoiler:
# réponse = 842161320
