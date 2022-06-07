arr=[1,1,2,3,4,5,6,6]
count = [0]*len(arr)
for i in arr:
    count[i]=count[i]+1
print(count)