def breakingRecords(scores):
    n = len(scores)
    maxr=0
    minr=0
    
    for i in range(n):
        if i>0 and (scores[i]>(max(scores[:i]))):
            maxr=maxr+1
        if i>0 and (scores[i]<(min(scores[:i]))):
            minr=minr+1
    return(maxr,minr)

scores=[12,10,52,12,8,63]

print(breakingRecords(scores))
