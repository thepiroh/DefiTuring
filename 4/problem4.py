def problem4():
    liste=[]
    for i in range(9999):
        for j in range(999):
            s=i*j
            s=str(s)
            if s == s[::-1] and s != '0':
                s=int(s)
                liste.append(s)
    liste=sorted(liste)
    print(liste[-1]) # dernier element de la liste: le plus grand palindrome


problem4()
