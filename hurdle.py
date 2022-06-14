def hurdleRace(k, height):
    # Write your code here
    maxh = max(height)
    if k<maxh:
        return maxh-k
    else:
        return 0