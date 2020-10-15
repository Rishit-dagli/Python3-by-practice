import datetime

time = datetime.time(7, 20, 30, tzinfo=datetime.timezone.utc)

print(time)

print(f'hour : {time.hour}')
print(f'minute : {time.minute}')
print(f'second : {time.second}')
print(f'microsecond : {time.microsecond}')
print(f'timezone : {time.tzinfo}')
print(f'minimum datetime : {datetime.time.min}')
print(f'maximum datetime : {datetime.time.max}')

today = datetime.date.today()
print(f'today is {today}')
print(f'date tuple : {today.timetuple()}')
print(f'year : {today.year}')
print(f'day : {today.day}')
print(f'month : {today.month}')
print(f'minimum date : {datetime.date.min}')
print(f'maximum date : {datetime.date.max}')

