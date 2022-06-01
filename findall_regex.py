import re

line = "MyNameIsShivanand"

reslist = []

reslist = re.findall('[A-Z][^A-Z]*',line)

print(reslist)