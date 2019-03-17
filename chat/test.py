from datetime import date, timedelta

today =  date.today()
print(today)
today -= timedelta(50)
print(today)
print(str(today)[:4])
