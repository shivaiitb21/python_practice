def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    pos = 0
    
    while True:
        pos = (pos+k)%n
        if c[pos]==0:
            e -= 1
        else:
            e -= 3
            
        if pos == 0:
            break
        
    return e