print("="*50)
print("      CALENDAR VERIFICATION SYSTEM")
print("="*50)

# 1. Take input
try:
    year = int(input("Enter year: "))
except:
    print("Invalid input! Please enter a number.")
    exit()

# 2. Validate the input
if year <= 0:
    print("Error: Year must be a positive integer greater than 0.")
    exit()

# 3. Check leap year rules using if-else
reason = ""
is_leap = False

if year % 100 == 0:  # Century year
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else:  # Non-century year
    if year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

# 4. Determine calendar details
if is_leap:
    status = "LEAP YEAR"
    days_in_year = 366
    feb_days = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    feb_days = 28

# 5. Display results clearly
print("-"*50)
print(f" Year: {year}")
print(f" Status: {status}")
print(f" Days in Year: {days_in_year} days")
print(f" Days in February: {feb_days} days")
print(f" Reason: {reason}")
print("-"*50)