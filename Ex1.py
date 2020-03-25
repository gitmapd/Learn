"""Hello World"""
from datetime import date, datetime

print("Hello World")
today=datetime.today()
current=lambda d: datetime.strftime(d,"%d-%m-%Y")

print(f'Date is  {current(today)}')

sieve=[True]*10
newsieve=[]
dict={}
for i in range(len(sieve)//2):
    if sieve[i]:
        newsieve.append((sieve[i]*i+2))
    dict[i]=newsieve[i]

for i,v in dict.items():
    print(f'key={i} and value={v}')


print(newsieve)