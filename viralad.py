import math
def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumlike = 0
    for i in range(1,n+1):
        liked = math.floor(shared/2)
        shared = 3*math.floor(shared/2)
        cumlike += liked
        
    return cumlike
