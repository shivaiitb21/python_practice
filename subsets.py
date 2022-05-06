# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
# We need to write the program right from taking input
    #Variable A contains a set of items.
#Variable N tells the program how many sets will be created.

    A = set(map(int, input().split()))
    N = int(input())

    #List in which we will store different sets once we create them.

    set_list = []

    #We loop N times and variable x creates N sets. We append these sets to a list. Previously created variable set_list now contains a number of different sets.

    for i in range(N):
        x = set(map(int, input().split()))
        set_list.append(x)

    #Default value of the resuls variable is True

    result = True

    #We iterate over differnet sets in a list.  Result will stay True, unless we find a set to whom A is not a superset.

    for i in set_list:
        if not A.issuperset(i):
            result = False

    print (result)
