#import calendar displaycalendar, date and check leap year
import calendar as cal
import datetime


year = 2025
month = 6

print(cal.month(year, month))

# Check if the year is a leap year
if print(cal.isleap(year)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#get the current date
current_date = datetime.date.today()
print(f"Current date: {current_date}")

#create specific date object
my_date = datetime.date(2025, 6, 18)
print(f"My specific date: {my_date}")

#get current time only
current_time = datetime.datetime.now().time()
print(f"Current time: {current_time}")



# Display the calendar for the entire year
print(cal.calendar(year))

# find the count number of leap years in a range
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))
leap_count = cal.leapdays(start_year, end_year)

print(f"There are {leap_count} leap years between {start_year} and {end_year}.")


