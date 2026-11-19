import tkinter as tk
from tkinter import ttk, messagebox

import psycopg2

# Global dictionary to store product details for quick lookup
product_cache = {}


# 1. Database Function to Populate the Dropdown
def load_dropdown_data():
    try:
        # Update these credentials with your actual PostgreSQL details
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Aarav@30",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Fetch data to populate the dropdown
        cursor.execute("SELECT 'Product', id, 'Price', 'Quantity' FROM store")
        rows = cursor.fetchall()

        dropdown_items = []
        product_cache.clear()

        for row in rows:
            prod_name, prod_id, price, qty = row
            dropdown_items.append(prod_name)
            # Store details in a dictionary using the product name as the key
            product_cache[prod_name] = {"id": prod_id, "price": price, "quantity": qty}

        # Insert item names into the combobox dropdown
        product_dropdown['values'] = dropdown_items

        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not load dropdown items:\n{e}")


# 2. Event Handler for Dropdown Selection
def on_item_select(event):
    selected_product = product_dropdown.get()

    if selected_product in product_cache:
        details = product_cache[selected_Product]
        # Update UI labels with the selected product's details
        lbl_id_val.config(text=f"{details['id']}")
        lbl_price_val.config(text=f"${details['Price']:.2f}")
        lbl_qty_val.config(text=f"{details['Quantity']} units")


# 3. Initialize GUI Window
root = tk.Tk()
root.title("Store Product Selector")
root.geometry("400x250")

# Main Container Frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Dropdown Section
ttk.Label(main_frame, text="Select a Product:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W, pady=5)
product_dropdown = ttk.Combobox(main_frame, width=30, state="readonly")
product_dropdown.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

# Bind the selection event to our function
product_dropdown.bind("<<ComboboxSelected>>", on_item_select)

# Details Display Section
ttk.Label(main_frame, text="Product Details", font=("Arial", 11, "underline")).grid(row=2, column=0, columnspan=2,
                                                                                    sticky=tk.W, pady=(15, 5))

ttk.Label(main_frame, text="Database ID:").grid(row=3, column=0, sticky=tk.W, pady=2)
lbl_id_val = ttk.Label(main_frame, text="-", font=("Arial", 10, "bold"))
lbl_id_val.grid(row=3, column=1, sticky=tk.W, pady=2, padx=10)

ttk.Label(main_frame, text="Price:").grid(row=4, column=0, sticky=tk.W, pady=2)
lbl_price_val = ttk.Label(main_frame, text="-", font=("Arial", 10, "bold"))
lbl_price_val.grid(row=4, column=1, sticky=tk.W, pady=2, padx=10)

ttk.Label(main_frame, text="Stock Level:").grid(row=5, column=0, sticky=tk.W, pady=2)
lbl_qty_val = ttk.Label(main_frame, text="-", font=("Arial", 10, "bold"))
lbl_qty_val.grid(row=5, column=1, sticky=tk.W, pady=2, padx=10)

# Automatically fetch data and fill the dropdown when application starts
load_dropdown_data()

root.mainloop()

