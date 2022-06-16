def saveThePrisoner(n, m, s):
    res = (s + m-1) % n
    return res if res != 0 else n