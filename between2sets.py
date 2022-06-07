def getTotalX(a, b):
    # Write your code here
    maxA=max(a)
    maxB=max(b)
    counter = 0
    for i in range(maxA,maxB+1): #minB+1 to include last element
        mul = all([i%numA==0 for numA in a])
        fac = all([numB%i==0 for numB in b])
        counter = counter + (mul*fac)
    return counter
    

