from datetime import datetime, timedelta


users = {"Vasya":"14.11.2022",
"Petya":"15.11.2022",
"John":"23.11.2022",
"Afonya":"19.11.2022",
"WALDEMAAAR": "14.11.2022",
"Sonya": "11.11.2022"}


def get_birthdays_per_week(users: dict):
    lst = list[str]
    rules = {0:"Monday", 5:"Monday", 6:"Monday", 1:"Tuesday", 2: "Wednesday", 3:"Thursday", 4: "Friday"}
    to_congratulate = {"Monday":[], "Tuesday":[], "Wednesday": [], "Thursday": [], "Friday": []}
    today = datetime.now()
    start_day = today
    while start_day.weekday() < 5:
        start_day += timedelta(days=1)
    if start_day.weekday() > 5:
        while start_day.weekday()>5:
            start_day -= timedelta(days=1)
    
    finish_day = start_day + timedelta(days=6)
    for user in users:
        birth_day = datetime.strptime(users.get(user),"%d.%m.%Y")
        if birth_day >= start_day and birth_day <= finish_day:
            week_day = birth_day.weekday()
            day_to_congrats = rules.get(week_day)
            to_congratulate.get(day_to_congrats).append(user)
    for w_day in to_congratulate:
        bd_boys = to_congratulate.get(w_day)
        if len(bd_boys)>0:
            usrs = ""
            i = 0
            while i<len(bd_boys):
                usrs += bd_boys[i]
                if len(bd_boys)-i != 1:
                    usrs += ", "
                i += 1
            print(w_day + ": " + usrs)

get_birthdays_per_week(users)