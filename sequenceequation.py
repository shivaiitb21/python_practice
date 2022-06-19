def permutationEquation(p):
    # Write your code here
    f1=[]
    n=len(p)
    for x in range(1,n+1):
        f1.append(p.index(x)+1)
    f2=[]
    for f in f1:
        f2.append(p.index(f)+1)
    return f2
    