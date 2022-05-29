l = [1,8,2,5,9,10,21,18]

def selectionsort(l):
    
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        
        (l[start],l[minpos]) = (l[minpos],l[start])
    
    print

selectionsort(l)