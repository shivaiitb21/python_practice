def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    maxsum=sum(i for i in arr[1:] )
    minsum=sum(i for i in arr[:4])
    
    print(minsum , maxsum)