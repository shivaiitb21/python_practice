def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    counta=0
    counto=0
    
    aa = len(apples)
    oo = len(oranges)
    
    for i in range(aa):
        if (a+apples[i])>=s and (a+apples[i])<=t:
            counta = counta+1
    print(counta)
    
    for i in range(oo):
        if (b+oranges[i])>=s and (b+oranges[i])<=t:
            counto = counto+1
    print(counto)