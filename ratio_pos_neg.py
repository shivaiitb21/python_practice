def plusMinus(arr):
    zc=0
    pc=0
    nc=0
    n=len(arr)
    for i in range(len(arr)):
        if arr[i]==0:
            zc=zc+1
        if arr[i]<0:
            nc=nc+1
        if arr[i]>0:
            pc=pc+1
    # return(pc,nc,zc)

    l=[pc,nc,zc]

    for j in range(len(l)):
        x = l[j]/n
        print(x)
    
arr=[-1,-2,0,3,4]

print(plusMinus(arr))
    