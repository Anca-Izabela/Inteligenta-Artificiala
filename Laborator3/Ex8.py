import datetime

acum = "2023-04-24 09:03:32.744178"

extrage_anul = lambda dt: dt.split('-')[0]
extrage_luna = lambda dt: dt.split('-')[1]
extrage_ziua = lambda dt: dt.split('-')[2].split(' ')[0]
extrage_ora = lambda dt: dt.split(' ')[1]

print(acum)
print(extrage_anul(acum))
print(extrage_luna(acum))
print(extrage_ziua(acum))
print(extrage_ora(acum))