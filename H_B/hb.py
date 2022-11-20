from datetime import datetime, timedelta
users = [
    {"name": "Tanya", "birthday": datetime(year=1992, month=11, day=23)},
    {"name": "Kostya", "birthday": datetime(year=1992, month=11, day=8)},
    {"name": "Serhiy", "birthday": datetime(year=1992, month=11, day=8)},
    {"name": "Sasha", "birthday": datetime(year=1994, month=11, day=3)},
    {"name": "Nastya", "birthday": datetime(year=1989, month=11, day=29)},
    {"name": "Vasya", "birthday": datetime(year=1986, month=11, day=24)},
    {"name": "Pasha", "birthday": datetime(year=1986, month=11, day=27)},
    {"name": "Pasha Padlo", "birthday": datetime(year=1986, month=11, day=26)},
    {"name": "I Ego Brat", "birthday": datetime(year=1986, month=11, day=26)},
    {"name": "Nezhdanchik", "birthday": datetime(year=1986, month=11, day=1)},
    {"name": "Olia", "birthday": datetime(year=1995, month=11, day=30)}
]


def get_birthdays_per_week(users: list):
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
        birth_day = datetime(
            year = today.year,
            month = user.get('birthday').month,
            day = user.get('birthday').day
        )
        if birth_day >= start_day and birth_day <= finish_day:
            week_day = birth_day.weekday()
            day_to_congrats = rules.get(week_day)
            to_congratulate.get(day_to_congrats).append(user.get("name"))
    
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