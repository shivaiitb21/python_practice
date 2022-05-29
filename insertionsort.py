def insertionsort(l):
    for sliceend in range(len(l)):
        pos = sliceend
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos = pos-1
    
    print(l)

l = [1,5,2,3,7,564,20,15]

insertionsort(l)