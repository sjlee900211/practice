import datetime

set_dt = datetime.datetime(2021, 8, 2, 10, 20, 0)
print(set_dt)

print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))