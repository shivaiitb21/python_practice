def divisibleSumPairs(n, k, ar):
    
    counter=0
    
    for i in range(n):
        if i<n:
            for j in range(i+1,n):
                addn=ar[i]+ar[j]
                if addn%k ==0:
                    counter=counter+1
                    
    return(counter)