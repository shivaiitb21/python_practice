def countingSort(arr):
    count = [0]*100              ## Change 1 : Working Fine
    for x in arr:
        count[x] = count[x]+1
    return count
        