print("="*50)
print("      CLOTHING STORE BILLING SYSTEM")
print("="*50)

# 1. Accept customer's name
customer_name = input("Enter Customer Name: ")

# 2. Accept garment name
garment_name = input("Enter Garment Name: ")

# 3. Accept price of one garment - use float()
price = float(input("Enter Price of one garment: "))

# 4. Accept number of garments - use int()
quantity = int(input("Enter Number of Garments: "))

# 5. Calculate total cost
total_amount = price * quantity

# 6. Display simple bill
print("\n" + "="*50)
print("                 BILL")
print("="*50)
print(f" Customer Name   : {customer_name}")
print(f" Garment Name    : {garment_name}")
print(f" Price per unit  : Rs. {price}")
print(f" Quantity        : {quantity}")
print(f" Total Amount    : Rs. {total_amount}")
print("="*50)