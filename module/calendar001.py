import calendar

print(calendar.calendar(2021))

print(calendar.calendar(2021, m=4)) #달력 출력형식을 4열로 지정

print(calendar.month(2021, 9)) # 특정 월만 보고 싶을 경우

print(calendar.month(2021, 2)) 
calendar.monthrange(2021, 2) # 그 달의 1일이 시작하는 요일과 그 달의 날짜 수

calendar.firstweekday() #일주일의 시작요일은 월요일

calendar.setfirstweekday(calendar.SUNDAY) #달력에서 시작요일을 일요일로 바꾼 후
print(calendar.month(2021, 8)) # 달력을 출력

print(calendar.weekday(2021, 8, 1)) #해당 날짜의 요일을 반환-일요일 6

print(calendar.isleap(2020)) # 윤년구하기
print(calendar.isleap(2021))