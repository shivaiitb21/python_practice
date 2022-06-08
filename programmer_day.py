import datetime
from datetime import timedelta

def dayOfProgrammer(year):
    
    # Write your code here
    start_date = datetime.date(year,1,1)
    
    final_date = start_date + timedelta(days=255)
    
    print(final_date.strftime("%d.%m.%y"))

dayOfProgrammer(2020)

