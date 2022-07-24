leap=int(input("Enter The Year"))


if leap%4==0:
    if leap%100==0:
        if leap%400==0:
            print("LEAP YEAR")
        else:
            print("NOT A LEAP YEAR")
    else:
        print("IT IS A LEAP YEAR") 
else:
    print("NOT A LEAP YEAR")

