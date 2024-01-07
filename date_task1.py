from datetime import datetime, timedelta

def find_next_friday_13(current_date, count):
    friday_13_dates = []

    while len(friday_13_dates) < count:
        current_date += timedelta(days=1)
        if current_date.day == 13 and current_date.weekday() == 4:  # 4 означает пятницу в формате Python
            friday_13_dates.append(current_date)

    return friday_13_dates


current_date = datetime.now()
next_friday_13_dates = find_next_friday_13(current_date, 10)

for date in next_friday_13_dates:
    print(date.strftime("%Y-%m-%d"))