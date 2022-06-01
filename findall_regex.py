import re

line = "MyNameIsShivanand"

reslist = []

reslist = re.findall('[A-Z][^A-Z]*',line)

print(reslist)

for i in range(len(reslist)):
    print(reslist[i].lower(), end=' ')