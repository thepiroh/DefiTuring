def problem9():

    for a in range(1000,3600):
        for b in range(1000,3600):
            for c in range(1000,3600):
                if (a*a + b*b == c*c) and (a+b+c == 3600):
                    print(a,b,c)
                    print(a*b*c)
                    
problem9()

# algorithme couteux en complexité
