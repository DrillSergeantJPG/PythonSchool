from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def find_next_friday_13(count):
    friday_13_dates = []
    current_date = datetime.now()

    while len(friday_13_dates) < count:

        current_date = current_date.replace(day=13)

        if current_date.weekday() == 4:
            friday_13_dates.append(current_date)
            current_date += relativedelta(months=1)
        else:
            current_date += relativedelta(months=1)

    return friday_13_dates


next_friday_13_dates = find_next_friday_13(10)

for date in next_friday_13_dates:
    print(date.strftime("%Y-%m-%d"))
