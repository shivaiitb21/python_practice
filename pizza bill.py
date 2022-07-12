print("Welcome To The Pizza Center")
size=input("Enter The Size Of Pizza")
pip=input("Want To Add Piporonie")
cheese=input("Want Extra Cheese")
bill=0


if size=="S":
    bill+=15
if size=="M":
    bill+=20
else:
    bill+=25

if pip=="Y":
    if size=="S":
        bill+=2
    if size=="M" or size=="L":
        bill+=3
else:
    bill+=0
if cheese=="Y":
    bill+=1
else:
    bill+=0

print(f"The Total Bill Is ${bill}")

