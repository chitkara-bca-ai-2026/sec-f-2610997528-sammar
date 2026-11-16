import math

print("="*50)
print("      ENGINEERING CALCULATION TOOL")
print("="*50)

# 1. Accept a numerical value
value = float(input("Enter a numerical value: "))

# 2. Accept an exponent and calculate power using pow()
exponent = float(input("Enter an exponent: "))
power = math.pow(value, exponent)

# 3. Calculate square root using sqrt()
square_root = math.sqrt(value)

# 4. Accept decimal measurement for ceil() and floor()
decimal = float(input("Enter a decimal measurement: "))
ceil_val = math.ceil(decimal)
floor_val = math.floor(decimal)

# 5. Display all results
print("\n--- Results ---")
print(f" Value               : {value}")
print(f" Exponent            : {exponent}")
print(f" Power (pow)         : {power}")
print(f" Square Root (sqrt)  : {square_root:.4f}")
print(f" Decimal Value       : {decimal}")
print(f" Ceil Value          : {ceil_val}")
print(f" Floor Value         : {floor_val}")
print("="*50)