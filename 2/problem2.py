def problem2():
    
    def F(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return F(n-1)+F(n-2)
    
    
    liste = []
    i=0
    while F(i) < 4000000:
        if F(i)%2 != 0:
            print(F(i))
            liste.append(F(i))
        i+=1
    #print(liste)
    print(sum(liste))

problem2()

# Alerte Spoiler:
# réponse = 4613732
