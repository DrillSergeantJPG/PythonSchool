from datetime import datetime
import pytz


def time_difference(city1, city2):
    timezone1 = pytz.timezone(city1)
    timezone2 = pytz.timezone(city2)

    time1 = datetime.now(timezone1)
    time2 = datetime.now(timezone2)

    time_difference = time2 - time1

    return {
        city1: time1.strftime("%Y-%m-%d %H:%M:%S %Z"),
        city2: time2.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "time_difference": str(time_difference)
    }


city1 = "Europe/Berlin"
city2 = "Europe/Kiev"
result = time_difference(city1, city2)

print(f"Сurrent time in {city1}: {result[city1]}")
print(f"Curent time in {city2}: {result[city2]}")
print(f"Difference in time is  {result['time_difference']}")
