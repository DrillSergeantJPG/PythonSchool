from datetime import datetime

def calculate_age_and_zodiac(birthdate):
    try:
        birthdate = datetime.strptime(birthdate, "%d-%m-%Y")

        current_date = datetime.now()

        age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))

        zodiac_sign = determine_zodiac_sign(birthdate.month, birthdate.day)

        return {"возраст": age, "знак_зодиака": zodiac_sign}

    except ValueError as e:
        return f"Ошибка: {e}"

def determine_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    else:
        return "Рыбы"

birthdate = "29-08-1993"
result = calculate_age_and_zodiac(birthdate)

print(f"Дата рождения: {birthdate}")
print(f"Возраст: {result['возраст']} лет")
print(f"Знак зодиака: {result['знак_зодиака']}")