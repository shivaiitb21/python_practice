if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().strip().split(" ")
        cmd = s[0]
        
        if cmd=="insert":
            l.insert(int(s[1]),int(s[2]))
        elif cmd=="print":
            print(l)
        elif cmd=="remove":
            l.remove(int(s[1]))
        elif cmd=="append":
            l.append(int(s[1]))
        elif cmd=="sort":
            l.sort()
        elif cmd=="pop":
            l.pop()
        elif cmd=="reverse":
            l.reverse()
            