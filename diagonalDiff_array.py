
def diagonalDifference(arr):
    # Write your code here
    lr = 0
    rl = 0
    n = len(arr)
    for i in range(n):
        lr = lr+arr[i][i]
        rl = rl+arr[i][n-i-1]
    return(abs(lr-rl))
