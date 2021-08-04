import datetime

now = datetime.datetime.now()
print(now)

print("Date & Time:{:%Y-%m-%d, %H:%M:%S}".format(now))

print("Date: {:%Y, %m, %d}".format(now))
print("Time: {:%H/%M/%S}".format(now))

now = datetime.datetime.now()
set_dt = datetime.datetime(2020, 12, 1, 12, 30, 45)

print("현재 날짜 및 시각:", now)
print("차이:", set_dt - now)