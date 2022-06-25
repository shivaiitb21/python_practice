def add(a, b):
  return a + b
l1 = [1,2,3,4,5,6]
l2 = [1,2,54,6,4,5]
x = map(add, l1,l2)

#Convert map into list for readability 
print(list(x))