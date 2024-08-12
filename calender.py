#python program to find day  given date
import datetime
# import calendar
# week=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','SATURDAY','SUNDAY']
# month,day,year =map(int,input().split())
# weekday=calendar.weekday(year,month,day)
#
#
#
# print(week[weekday])
import calendar
a=list(map(int,input().split()))
m=a[0]
d=a[1]
y=a[2]
#m,d,y=map(int, input().split())
x=calendar.weekday(y,m,d)

print(calendar.day_name[x].upper())
