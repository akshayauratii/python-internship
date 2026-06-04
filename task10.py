# Smart Inventory Management System

# Data Structures Used (As specified in the design requirements):
# - dict: product records (Key: product_id, Value: dict of attributes)
# - set: categories (To track unique product categories)
# - list: search results, reports
# - tuple: product snapshots (Immutably capturing a product state)

inventory = {}
categories = set()

def add_product():
    print("\n--- Add Product ---")
    p_id = input("Enter Product ID: ").strip()
    if p_id in inventory:
        print("Error: Product ID already exists!")
        return
    
    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    try:
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: ₹"))
    except ValueError:
        print("Error: Invalid number format for quantity or price.")
        return
        
    supplier = input("Enter Supplier: ").strip()
    
    # Store in dict
    inventory[p_id] = {
        "name": name,
        "category": category,
        "qty": qty,
        "price": price,
        "supplier": supplier
    }
    # Track category using Set
    categories.add(category)
    print(f"Product '{name}' added successfully!")

def update_inventory():
    print("\n--- Update Inventory ---")
    p_id = input("Enter Product ID to modify: ").strip()
    if p_id not in inventory:
        print("Error: Product ID not found.")
        return
        
    print("Leave field blank to keep current value.")
    new_qty = input(f"Enter new quantity (Current: {inventory[p_id]['qty']}): ").strip()
    new_price = input(f"Enter new price (Current: ₹{inventory[p_id]['price']:.2f}): ").strip()
    
    try:
        if new_qty:
            inventory[p_id]['qty'] = int(new_qty)
        if new_price:
            inventory[p_id]['price'] = float(new_price)
        print("Inventory updated successfully!")
    except ValueError:
        print("Error: Invalid numeric input.")

def search_product():
    print("\n--- Search Product ---")
    search_term = input("Search by Product ID or Name (case-insensitive): ").strip().lower()
    
    # Track matching results using a List
    results = []
    
    for p_id, details in inventory.items():
        if search_term == p_id.lower() or search_term in details['name'].lower():
            # Use tuple to take an immutable snapshot of the search match
            snapshot = (p_id, details['name'], details['category'], details['qty'], details['price'])
            results.append(snapshot)
            
    if not results:
        print("No matching products found.")
    else:
        print(f"\nFound {len(results)} matching item(s):")
        print(f"{'ID':<10} | {'Name':<20} | {'Category':<15} | {'Qty':<6} | {'Price':<10}")
        print("-" * 70)
        for item in results:
            print(f"{item[0]:<10} | {item[1]:<20} | {item[2]:<15} | {item[3]:<6} | ₹{item[4]:.2f}")

def display_inventory():
    print("\n--- Current Inventory Status ---")
    if not inventory:
        print("Inventory is empty.")
        return
        
    print(f"{'ID':<10} | {'Name':<20} | {'Category':<15} | {'Qty':<6} | {'Price':<10} | {'Supplier':<15}")
    print("-" * 85)
    for p_id, d in inventory.items():
        print(f"{p_id:<10} | {d['name']:<20} | {d['category']:<15} | {d['qty']:<6} | ₹{d['price']:<9.2f} | {d['supplier']:<15}")

def low_stock_alert():
    print("\n--- Low Stock Alert (Threshold <= 10) ---")
    low_stock_items = [p_id for p_id, d in inventory.items() if 0 < d['qty'] <= 10]
    
    if not low_stock_items:
        print("All items are sufficiently stocked.")
    else:
        for p_id in low_stock_items:
            print(f"⚠️ LOW STOCK: ID {p_id} | Name: {inventory[p_id]['name']} | Qty Remaining: {inventory[p_id]['qty']}")

def out_of_stock_alert():
    print("\n--- Out of Stock Alert ---")
    out_of_stock = [p_id for p_id, d in inventory.items() if d['qty'] == 0]
    
    if not out_of_stock:
        print("No items are out of stock.")
    else:
        for p_id in out_of_stock:
            print(f"🚨 OUT OF STOCK: ID {p_id} | Name: {inventory[p_id]['name']} | Please Reorder!")

def category_management():
    print("\n--- Category Management ---")
    print(f"Unique Categories currently tracked: {len(categories)}")
    for cat in categories:
        print(f" - {cat}")

def inventory_report():
    print("\n==============================")
    print("       INVENTORY REPORT")
    print("==============================")
    total_items = sum(d['qty'] for d in inventory.values())
    total_value = sum(d['qty'] * d['price'] for d in inventory.values())
    
    print(f"Total Unique Products: {len(inventory)}")
    print(f"Total Quantity Items:  {total_items}")
    print(f"Total Valuation:       ₹{total_value:.2f}")
    
    print("\n--- Category-wise Summary ---")
    for cat in categories:
        cat_qty = sum(d['qty'] for d in inventory.values() if d['category'] == cat)
        cat_val = sum(d['qty'] * d['price'] for d in inventory.values() if d['category'] == cat)
        print(f"Category '{cat}': Total Items: {cat_qty} | Total Value: ₹{cat_val:.2f}")
    print("==============================")

def delete_product():
    print("\n--- Delete Product ---")
    p_id = input("Enter Product ID to remove: ").strip()
    if p_id in inventory:
        removed_item = inventory.pop(p_id)
        # Recalculate unique categories remaining
        global categories
        categories = set(d['category'] for d in inventory.values())
        print(f"Product '{removed_item['name']}' removed from inventory system.")
    else:
        print("Error: Product ID not found.")

def main():
    while True:
        print("\n--- SMART INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add Product")
        print("2. Update Inventory")
        print("3. Search Product")
        print("4. Display Inventory")
        print("5. Low Stock Alert")
        print("6. Out of Stock Alert")
        print("7. Category Management")
        print("8. Inventory Report")
        print("9. Delete Product")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == "1": add_product()
        elif choice == "2": update_inventory()
        elif choice == "3": search_product()
        elif choice == "4": display_inventory()
        elif choice == "5": low_stock_alert()
        elif choice == "6": out_of_stock_alert()
        elif choice == "7": category_management()
        elif choice == "8": inventory_report()
        elif choice == "9": delete_product()
        elif choice == "10": 
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()