def problem7():
    liste=[]
    compteur=0
    for num in range(2,500000 + 1): # on choisit un grand intervalle pour être sûr d'avoir pris le 23456ème nombre premier.
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                liste.append(num)
                print(num,compteur)
                compteur+=1
                if compteur == 23456:
                    break
    print(liste[23455])
    
problem7()

# ATTENTION: cet algorithme est très couteux en complexité...
