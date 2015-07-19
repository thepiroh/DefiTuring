def problem10(n):
    taille = n//2
    filtre = [1]*taille
    limit = int(n**0.5)
    for i in range(1, limit):
        if filtre[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            filtre[i+val::val] = [0]*tmp
    print(sum([2] + [i*2+1 for i, v in enumerate(filtre) if v and i>0]))


problem10(10000000)

# Alerte Spoiler:
# réponse = 3203324994356
