def angryProfessor(k, a):
    # Write your code here
    e = sum(1 for i in a if i<=0)
    if e<k:
        return "YES"
    else:
        return "NO"
    