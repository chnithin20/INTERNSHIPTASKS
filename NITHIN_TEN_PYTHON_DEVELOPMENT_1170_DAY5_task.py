# Smart Inventory Management System

class InventorySystem:
    def __init__(self):
        # product_id -> product record (dict)
        self.products = {}

        # set for categories
        self.categories = set()

        # list for reports/search history
        self.reports = []

        # low stock threshold
        self.low_stock_threshold = 10

    # 1. Add Product
    def add_product(self, pid, name, category, qty, price, supplier):
        if pid in self.products:
            print("Product ID already exists!")
            return

        self.products[pid] = {
            "name": name,
            "category": category,
            "qty": qty,
            "price": price,
            "supplier": supplier
        }

        self.categories.add(category)
        print("Product added successfully!")

    # 2. Update Inventory
    def update_product(self, pid, qty=None, price=None):
        if pid not in self.products:
            print("Product not found!")
            return

        if qty is not None:
            self.products[pid]["qty"] = qty
        if price is not None:
            self.products[pid]["price"] = price

        print("Product updated successfully!")

    # 3. Search Product
    def search_product(self, keyword):
        results = []
        keyword = keyword.lower()

        for pid, data in self.products.items():
            if keyword in pid.lower() or keyword in data["name"].lower():
                results.append((pid, data))

        self.reports.append(("search", keyword, len(results)))

        if not results:
            print("No products found!")
        else:
            for pid, data in results:
                print(pid, data)

    # 4. Delete Product
    def delete_product(self, pid):
        if pid in self.products:
            del self.products[pid]
            print("Product deleted!")
        else:
            print("Product not found!")

    # 5. Display Inventory
    def display_inventory(self):
        print("\n--- INVENTORY ---")
        for pid, data in self.products.items():
            print(pid, data)

    # 6. Low Stock Alert
    def low_stock_alert(self):
        print("\n--- LOW STOCK ALERT ---")
        for pid, data in self.products.items():
            if data["qty"] < self.low_stock_threshold:
                print(pid, data)

    # 7. Out of Stock Alert
    def out_of_stock(self):
        print("\n--- OUT OF STOCK ---")
        for pid, data in self.products.items():
            if data["qty"] == 0:
                print(pid, data)

    # 8. Inventory Report
    def inventory_report(self):
        total_items = len(self.products)
        total_value = sum(data["qty"] * data["price"] for data in self.products.values())

        category_summary = {}
        for data in self.products.values():
            cat = data["category"]
            category_summary[cat] = category_summary.get(cat, 0) + 1

        report = {
            "total_items": total_items,
            "total_value": total_value,
            "category_summary": category_summary
        }

        self.reports.append(("report", report))

        print("\n--- INVENTORY REPORT ---")
        print("Total Items:", total_items)
        print("Total Value:", total_value)
        print("Category Wise:", category_summary)


# ---------------- MAIN PROGRAM ----------------

def main():
    inv = InventorySystem()

    while True:
        print("\n===== SMART INVENTORY MENU =====")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Search Product")
        print("4. Delete Product")
        print("5. Display Inventory")
        print("6. Low Stock Alert")
        print("7. Out of Stock Alert")
        print("8. Inventory Report")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            category = input("Category: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            supplier = input("Supplier: ")
            inv.add_product(pid, name, category, qty, price, supplier)

        elif choice == "2":
            pid = input("Product ID: ")
            qty = input("New Qty (leave blank if no change): ")
            price = input("New Price (leave blank if no change): ")

            qty = int(qty) if qty else None
            price = float(price) if price else None

            inv.update_product(pid, qty, price)

        elif choice == "3":
            keyword = input("Enter product ID or name: ")
            inv.search_product(keyword)

        elif choice == "4":
            pid = input("Product ID: ")
            inv.delete_product(pid)

        elif choice == "5":
            inv.display_inventory()

        elif choice == "6":
            inv.low_stock_alert()

        elif choice == "7":
            inv.out_of_stock()

        elif choice == "8":
            inv.inventory_report()

        elif choice == "9":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()