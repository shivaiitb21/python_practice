for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FUZZ BUZZ")
    elif i%3==0:
        print("FUZZ")
    elif i%5==0:
        print("BUZZ")
    else:
        print(i)            
