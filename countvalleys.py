def countingValleys(steps, path):
    alt = 0
    val = 0
    for i in path:
        if i=="U":
            alt += 1
            if alt==0: #If the alt becomes zero after step up
                val += 1
        if i=="D":
            alt -= 1
    return val