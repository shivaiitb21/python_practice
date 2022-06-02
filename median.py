def getmedian(arr):

    n = len(arr)

    if n%2 !=0:
        m = int((n+1)/2)-1
        return arr[m]

    else:
        m1 = int(n/2)-1
        m2 = int(n/2)
        m = int((m1+m2)/2)
        return arr[m]

arr = [1,2,3,4]

print(getmedian(arr))
