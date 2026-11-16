# Lab 13 - Inventory Control System

# Initial inventory with 4 products
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("="*50)
print("      INVENTORY CONTROL SYSTEM")
print("="*50)

while True:
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # 1. View Inventory
    if choice == "1":
        print("\n--- Current Inventory ---")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

    # 2. Add Item using append()
    elif choice == "2":
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(f'[SUCCESS] "{item}" added to inventory.')

    # 3. Remove Item using in and remove()
    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')

    # 4. Sort Inventory using sort()
    elif choice == "4":
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

    # 5. Exit using break
    elif choice == "5":
        print("\nThank you for using Inventory Control System. Goodbye!")
        break

    # Invalid input handling
    else:
        print("[ERROR] Invalid choice! Please enter 1 to 5.")