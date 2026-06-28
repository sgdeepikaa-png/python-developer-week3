from datetime import date, datetime

def days_until(date_string):
    target = datetime.strptime(date_string, "%Y-%m-%d").date()
    today = date.today()

    days = (target - today).days

    if days > 0:
        print(days, "days remaining")
    elif days == 0:
        print("Today is the date")
    else:
        print(abs(days), "days ago")

def format_date(date_string):
    d = datetime.strptime(date_string, "%Y-%m-%d")
    print(d.strftime("%A, %d %B %Y"))

def day_of_week(date_string):
    d = datetime.strptime(date_string, "%Y-%m-%d")
    print(d.strftime("%A"))

date_input = input("Enter Date (YYYY-MM-DD): ")

days_until(date_input)
format_date(date_input)
day_of_week(date_input)