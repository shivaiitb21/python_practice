def sockMerchant(n, ar):
    # Write your code here
    counter=0
    ar_set=list(set(ar))
    for i in ar_set:
        if ar.count(i)%2==0:
            m = int(ar.count(i)/2)
            counter = counter + m
        else:
            l = int((ar.count(i)-1)/2)
            counter = counter +l
            
    return counter

