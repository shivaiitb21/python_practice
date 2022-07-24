import random
User__choose=input("Enter Head or Tail")
toss=['head','tail']
result=random.choice(toss)
print(result)
if result==user__choice:
    print("You Won")
else:
    print("You Loss")    


user_choose=input("Do You Wanna Play Again?(yes/exit)")
if user_chose=="yes":
   continue
    
else:
   break    
