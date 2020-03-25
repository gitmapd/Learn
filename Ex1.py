"""Hello World"""
from datetime import date, datetime

print("Hello World")
today=datetime.today()
current=lambda d: datetime.strftime(d,"%d-%m-%Y")
print(current(today))

