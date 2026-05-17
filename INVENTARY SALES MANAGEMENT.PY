import json
import os

FILE_NAME = "inventory.json"

# -------------------------------
# Load inventory data from file
# -------------------------------
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            print("Error reading file. Starting with empty inventory.")
            return {}
    return {}

# -------------------------------
# Save inventory data to file
# -------------------------------
def save_data(inventory):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(inventory, file, indent=4)
    except:
        print("Error saving data!")

# -------------------------------
# Add new product
# -------------------------------
def add_product(inventory):
    print("\n--- Add Product ---")
    name = input("Enter product name: ").strip()

    if name in inventory:
        print("Product already exists!")
        return

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except:
        print("Invalid input! Please enter correct values.")
        return

    inventory[name] = {
        "price": price,
        "quantity": quantity
    }

    print("✅ Product added successfully!")

# -------------------------------
# View all products
# -------------------------------
def view_inventory(inventory):
    print("\n--- Inventory List ---")

    if not inventory:
        print("Inventory is empty!")
        return

    print(f"{'Product':<15}{'Price':<10}{'Quantity':<10}")
    print("-" * 35)

    for item, details in inventory.items():
        print(f"{item:<15}{details['price']:<10}{details['quantity']:<10}")

# -------------------------------
# Sell product
# -------------------------------
def sell_product(inventory):
    print("\n--- Sell Product ---")
    name = input("Enter product name: ").strip()

    if name not in inventory:
        print("❌ Product not found!")
        return

    try:
        qty = int(input("Enter quantity to sell: "))
    except:
        print("Invalid quantity!")
        return

    if inventory[name]["quantity"] >= qty:
        total = qty * inventory[name]["price"]
        inventory[name]["quantity"] -= qty

        print("✅ Sale successful!")
        print(f"Total amount: ₹{total}")
    else:
        print("❌ Insufficient stock!")

# -------------------------------
# Update product
# -------------------------------
def update_product(inventory):
    print("\n--- Update Product ---")
    name = input("Enter product name: ").strip()

    if name not in inventory:
        print("Product not found!")
        return

    try:
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
    except:
        print("Invalid input!")
        return

    inventory[name]["price"] = price
    inventory[name]["quantity"] = quantity

    print("✅ Product updated!")

# -------------------------------
# Delete product
# -------------------------------
def delete_product(inventory):
    print("\n--- Delete Product ---")
    name = input("Enter product name: ").strip()

    if name in inventory:
        del inventory[name]
        print("✅ Product deleted!")
    else:
        print("Product not found!")

# -------------------------------
# Main menu
# -------------------------------
def main():
    inventory = load_data()

    # ✅ Add default products if file is empty
    if not inventory:
        inventory = {
            "Apple": {"price": 50, "quantity": 10},
            "Milk": {"price": 30, "quantity": 20},
            "Bread": {"price": 40, "quantity": 15}
        }
        save_data(inventory)  # Save immediately

    while True:
        print("\n===== Inventory Management System =====")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Sell Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            view_inventory(inventory)

        elif choice == "3":
            sell_product(inventory)

        elif choice == "4":
            update_product(inventory)

        elif choice == "5":
            delete_product(inventory)

        elif choice == "6":
            save_data(inventory)
            print("💾 Data saved. Exiting program...")
            break

        else:
            print("❌ Invalid choice! Please try again.")

# -------------------------------
# Run program
# -------------------------------
if __name__ == "__main__":
    main()





