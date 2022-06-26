def wrap(string, max_width):
    n=len(string)
    s=""
    for i in range(0,n,max_width):
        s += string[i:i+max_width] + "\n"
    return s