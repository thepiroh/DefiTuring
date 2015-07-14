def problem1():

    score = 0

    for i in range(2013):
        if (i%5 == 0) or (i%7 == 0):
            score+=i
    print(score)
    
problem1()
