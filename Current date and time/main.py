from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print(f"Today's date is {today}")
print(f"\n Current Date and time is {now}")
print(f"\n Date components {today.year} {today.month} {today.day}")