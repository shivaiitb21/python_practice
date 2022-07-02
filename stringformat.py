price = 49
txt = "The price is {} dollars!"
print(txt.format(price))

txt2 = "The price in decimal is {:.2f} dollars!"
print(txt2.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))



