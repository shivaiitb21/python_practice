def migratoryBirds(arr):
    # Write your code here
    count = [0]*len(arr)
    
    for i in arr:
        count[i] = count[i]+1
    return count.index(max(count))    
    