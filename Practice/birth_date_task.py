import calendar
from datetime import datetime

def get_day_of_birth(year, month, day):
    
    birth_date = datetime(year, month, day)
    
    
    day_of_week = birth_date.weekday()
    
    
    day_name = calendar.day_name[day_of_week]
    
    return day_name

# Example usage
year = int(input("Enter Year :"))
month = int(input("Enter Month :"))
day = int(input("Enter Date :"))
print("--------------------------------------")
print("--------------------------------------")
day_of_birth = get_day_of_birth(year, month, day)
print("Day of birth:", day_of_birth)
print("Date is ",day)
print("Year of birth is ",year)

print(f"{day}/{month}/{year}")

