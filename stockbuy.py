
def maximumProfit(prices):
    # Write your code here.
    T = int(input())
    
    l,r = 0,1
    maxp = 0 
   
    for tc in range(len(T)):
        
        N = int(input())
        a = list(map(int, input().split()))
        
        
        while (r<len(a)):
            
            if a[l]<a[r]:
                p = a[r]-a[l]
                maxp = max(p,maxp)
                r += 1
            else:
                l = r
            r += 1
                
        print(maxp)
