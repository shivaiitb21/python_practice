def pickingNumbers(a):
    # Write your code here
    maxi=0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        b=c+d
        
        if b>maxi:
            maxi=b
            
    return maxi
