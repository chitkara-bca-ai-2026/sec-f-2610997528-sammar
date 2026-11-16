name=input("Enter product name:-")
price=float(input("Enter price:-"))
qut=int(input("enter quantity:-"))

total=price*2
total1=type(str)

print("===================================================")
print("       DATA CONVERSION UTILITY       ")
print("===================================================")

print(f"Enter Product Name : {name}")
print(f"Enter Price : {price:.2f}")
print(f"Enter Quantity : {qut}")

print("-------------------------------------------------------")
print("            TYPE CASTING SUMMARY            ")
print("-------------------------------------------------------")
print("Variable         Value            Python Type")
print("-------------------------------------------------------")

print(f"product_name    {name}           type(name)")
print(f"price           {price}          type(price)")
print(f"quantity        {qut}            type(qut)")
print(f"total_price     {total}          type(total)")
print(f"amount_str      {total1}         type(total1)")
print("-------------------------------------------------------")
print("                                                       ")
print("                                                       ")
print("                                                       ")

print("-------------------------------------------------------")
print("           TAX INVOICE           ")
print("-------------------------------------------------------")

print(f"Product Name  : {name}")
print(f"Price per unit  : Rs. {price:.2f}")
print(f"Quantity    : {qut}")
print("---------------------------------")
print(f"Invoice Total  : Rs. {total:.1f}")


