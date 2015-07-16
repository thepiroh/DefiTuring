def miroir(x):
    x = str(x)
    return int(x[::-1])
    
def problem11():
    liste=[]
    for i in xrange(10000000):
        if miroir(i) == 4*i:
            liste.append(i)
    print(liste[-1])
    
problem11()

# Alerte Spoiler:
# réponse = 2199978
