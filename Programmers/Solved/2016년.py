import calendar
# calender.weekday(year, month, day)
# 월요일(0), 화요일(1), 수요일(2), 목요일(3), 금요일(4), 토요일(5), 일요일(6)

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
def solution(a, b):

    return day[calendar.weekday(2016, a, b)]

print(solution(5, 24))