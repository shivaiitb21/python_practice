def beautifulDays(i, j, k):
    # Write your code here
    nums = range(i,j+1)
    revnums = []
    for num in nums:
        rev = str(num)[::-1]
        revnum = int(rev)
        revnums.append(revnum)
        
    bd=0
    
    for i,j in zip(nums,revnums):
        if abs(i-j)%k==0:
            bd += 1 
    return bd