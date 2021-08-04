import datetime

day1 = datetime.date(2021, 4, 1)
day2 = datetime.date(2021, 7, 10)
diff_day = day2 - day1
print(diff_day)
type(day1)
type(diff_day)

print("** 지정된 두 날짜의 차이는 {}일입니다. **".format(diff_day.days))