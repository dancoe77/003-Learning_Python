zz = "#######################################################"
print(zz)

import datetime

mytime = datetime.time(13,20,1,20)
print(mytime)
print(zz)
print(mytime.minute)
print(zz)
print(mytime.hour)
print(zz)
print(mytime.microsecond)
print(zz)
print(type(mytime))
print(zz)

today = datetime.date.today()
print(today)
print(zz)
print(today.year)
print(zz)
print(today.month)
print(zz)
print(today.day)
print(zz)
print(today.ctime())
print(zz)

from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)
print(zz)

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)
print(zz)

from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
print(result)
print(type(result))
print(zz)
print(result.days)
print(zz)

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
newresult = datetime1 - datetime2
print(newresult)
print(type(newresult))
print(zz)
print(newresult.seconds)
print(zz)