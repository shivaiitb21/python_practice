def timeConversion(s):
    # Write your code here
    hh=int(s[:2])
    if "PM" in s:
        if hh!=12:
            hh=hh+12

    if "AM" in s:
        if hh==12:
            hh=00
            
    hour=(str(hh)).zfill(2)
    
    return f"{hour}{s[2:-2]}"

s = "07:25:00PM"

print(timeConversion(s))

