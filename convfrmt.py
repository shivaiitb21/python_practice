def print_formatted(number):
    # your code goes here
    n = int(number)
    
    #Space padded to match the width of biggest Binary number
    w = len("{0:b}".format(n))
    
    for i in range(1, n+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=w))
