def compareTriplets(a, b):
    # Write your code here
    ascore = 0
    bscore = 0
    score = []
    for i in range(len(a)):
        if a[i]>b[i]:
            ascore = ascore + 1
        elif a[i]<b[i]:
            bscore = bscore + 1
    score.append(ascore)
    score.append(bscore)
    return(score)

a = [1, 2, 3]
b = [3, 2, 1]

print(compareTriplets(a,b))