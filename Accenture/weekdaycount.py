import datetime
import calendar

def weekDay(start, end):
    start_date = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%Y')
    week = {}
    for i in range((end_date-start_date).days):
        day = calendar.day_name[(start_date+datetime.timedelta(days=i+1)).weekday()]
        week[day] = week[day]+1 if day in week else 1
    return week

print(weekDay('01/01/2017', '31/01/2017'))