#Examples of list comprehensions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# expression
# newlist = [expression for item in iterable if condition == True]

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]