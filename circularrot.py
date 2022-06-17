a=[2,5,7,8,9]
k=2
queries=[1,2]
def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        le=a[len(a)-1]
        a.pop()
        a.insert(0,le)
    
    print(a)
    
    for q in queries:
        print(a[q])
    

circularArrayRotation(a, k, queries)
