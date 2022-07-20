d={}
n=int(input("Enter number of student"))
i=1
while i<=n:
    name=input("Enter the name")
    marks=int(input("Enter the marks"))
    d[name]=marks
    i=i+1
print("Name of the student","\t","%marks") 
for x in d:
    print("\t",x,"\t\t",d[x])
