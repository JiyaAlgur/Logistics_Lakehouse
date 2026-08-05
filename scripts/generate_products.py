import os
import random
import pandas as pd

# ------------------------------------------
# Configuration
# ------------------------------------------

NUM_PRODUCTS = 200
OUTPUT_PATH = "datasets/raw/products.csv"

# ------------------------------------------
# Product Catalog
# ------------------------------------------

product_catalog = [
    ("Coca Cola", "Beverages", "Coca Cola"),
    ("Pepsi", "Beverages", "Pepsi"),
    ("Sprite", "Beverages", "Coca Cola"),
    ("Fanta", "Beverages", "Coca Cola"),
    ("Mountain Dew", "Beverages", "Pepsi"),

    ("Lay's Classic", "Snacks", "Lay's"),
    ("Lay's Magic Masala", "Snacks", "Lay's"),
    ("Doritos Nacho", "Snacks", "Doritos"),
    ("Kurkure", "Snacks", "Kurkure"),
    ("Bingo Mad Angles", "Snacks", "Bingo"),

    ("Amul Milk", "Dairy", "Amul"),
    ("Amul Butter", "Dairy", "Amul"),
    ("Mother Dairy Milk", "Dairy", "Mother Dairy"),
    ("Amul Cheese", "Dairy", "Amul"),
    ("Yakult", "Dairy", "Yakult"),

    ("Britannia Bread", "Bakery", "Britannia"),
    ("Britannia Cake", "Bakery", "Britannia"),
    ("Harvest Gold Bread", "Bakery", "Harvest Gold"),
    ("Muffin", "Bakery", "Britannia"),
    ("Croissant", "Bakery", "Britannia"),

    ("Frozen Peas", "Frozen Foods", "Safal"),
    ("Frozen Corn", "Frozen Foods", "Safal"),
    ("Frozen Pizza", "Frozen Foods", "McCain"),
    ("French Fries", "Frozen Foods", "McCain"),
    ("Ice Cream", "Frozen Foods", "Amul"),

    ("Colgate Toothpaste", "Personal Care", "Colgate"),
    ("Dove Soap", "Personal Care", "Dove"),
    ("Lux Soap", "Personal Care", "Lux"),
    ("Clinic Plus Shampoo", "Personal Care", "Clinic Plus"),
    ("Nivea Face Wash", "Personal Care", "Nivea"),

    ("Surf Excel", "Household", "Surf Excel"),
    ("Ariel Detergent", "Household", "Ariel"),
    ("Lizol Cleaner", "Household", "Lizol"),
    ("Harpic", "Household", "Harpic"),
    ("Vim Dishwash", "Household", "Vim"),

    ("Classmate Notebook", "Stationery", "Classmate"),
    ("Apsara Pencil", "Stationery", "Apsara"),
    ("Cello Pen", "Stationery", "Cello"),
    ("Camlin Eraser", "Stationery", "Camlin"),
    ("Camel Sketch Pen", "Stationery", "Camel")
]

sizes = [
    "100g",
    "200g",
    "250ml",
    "500ml",
    "750ml",
    "1L",
    "2L",
    "Small",
    "Medium",
    "Large"
]

products = []

# ------------------------------------------
# Generate Products
# ------------------------------------------

for i in range(1, NUM_PRODUCTS + 1):

    product_name, category, brand = random.choice(product_catalog)

    full_name = f"{product_name} {random.choice(sizes)}"

    price = random.randint(20, 800)

    cost_price = random.randint(20, 600)

    profit_margin = random.uniform(0.15, 0.40)

    selling_price = round(cost_price * (1 + profit_margin), 2)

    products.append({
        "product_id": f"P{i:04d}",
        "product_name": full_name,
        "category": category,
        "brand": brand,
        "cost_price": cost_price,
        "selling_price": selling_price
})

# ------------------------------------------
# Create DataFrame
# ------------------------------------------

df = pd.DataFrame(products)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_PRODUCTS} products.")
print(f"Saved to: {OUTPUT_PATH}")