import datetime


def get_birthdays_per_week(users):

    week_dict = {}
    for name, birthday in users.items():
        if birthday.strftime("%A") not in week_dict:
            week_dict[birthday.strftime("%A")] = []
        week_dict[birthday.strftime("%A")].append(name)

    for birthday in week_dict.keys():
        names = week_dict[birthday]
        print(f'{birthday}: {", ".join(names)}')


users = {"Jill": datetime.date(
    day=26, month=10, year=92), "Kim": datetime.date(
    day=27, month=10, year=92),  "Bill":  datetime.date(day=26, month=10, year=92)}
get_birthdays_per_week(users)
