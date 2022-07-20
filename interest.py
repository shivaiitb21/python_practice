def simple_interest(p,r,t):
    return (p*r*t)/100

p= float(input("ENTER THE PRINCIPAL AMOUNT:"))
r= float(input("ENTER THE RATE OF INTEREST:"))
t= float(input("ENTER THE TIME IN YEAR:"))

print("THE INTEREST IS:",simple_interest(p,r,t))
