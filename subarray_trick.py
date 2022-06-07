
def birthday(s, d, m):
    # Write your code here
    n = len(s)
    return sum(1 for i in range(n-m+1) if sum(s[i:i+m])==d)

# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month