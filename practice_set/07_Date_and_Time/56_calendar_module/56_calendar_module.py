import calendar

date = input().split()

mm = int(date[0])
dd = int(date[1])
yyyy = int(date[2])


# Get the weekday index (0 = Monday, 6 = Sunday)
weekday_index = calendar.weekday(yyyy, mm, dd)

# Get the day name
day_name = calendar.day_name[weekday_index]

print(day_name.upper())  # Output: Thursday (for 29 May 2025)