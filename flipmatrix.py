def matrixflip(m,d):
    if d=='h':
        m=myl
        for i in range(0,len(m),1):
                    m[i].reverse()
        return(m)
    elif d=='v':
        m=myl
        m.reverse()
        return(m)
    else:
       return(m)