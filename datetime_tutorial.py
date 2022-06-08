import datetime
from datetime import timedelta

date = datetime.date(2017,1,1)
print(date.strftime("%d.%m.%y"))

#Future date after n days
new_date = date + timedelta(days=5)



print(new_date.strftime("%j"))
