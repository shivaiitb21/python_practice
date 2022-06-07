#Count the pairs in an array ar whose sum will be devisible by an integer k
def divisibleSumPairs(n, k, ar):
    # Write your code here
    import itertools
    
    return len([x for x in itertools.combinations(ar,r=2) if (x[0]+x[1])%k==0])

a = [1,2,3,4,5]
print(divisibleSumPairs(5,2,a))