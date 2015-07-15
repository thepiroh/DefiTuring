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


factors(20130101) -> [1, 19, 1059479, 20130101]
# on regarde le plus grand facteur, qui est 1059479. Et voici la réponse


# Alerte Spoiler:
# réponse = 1059479
