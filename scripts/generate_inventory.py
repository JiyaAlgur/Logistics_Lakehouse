import os
import random
import pandas as pd
from datetime import datetime, timedelta

# ------------------------------------------
# Configuration
# ------------------------------------------

NUM_RECORDS = 2000
OUTPUT_PATH = "datasets/raw/inventory.csv"

# ------------------------------------------
# Read Products & Warehouses
# ------------------------------------------

products = pd.read_csv("datasets/raw/products.csv")
warehouses = pd.read_csv("datasets/raw/warehouses.csv")

inventory = []

# ------------------------------------------
# Generate Inventory
# ------------------------------------------

for _ in range(NUM_RECORDS):

    product = products.sample(1).iloc[0]
    warehouse = warehouses.sample(1).iloc[0]

    quantity = random.randint(0, 1000)
    reorder_level = random.randint(20, 150)

    if quantity == 0:
        stock_status = "Out of Stock"
    elif quantity <= reorder_level:
        stock_status = "Low Stock"
    else:
        stock_status = "In Stock"

    inventory.append({
        "inventory_id": f"INV{len(inventory)+1:05d}",
        "warehouse_id": warehouse["warehouse_id"],
        "product_id": product["product_id"],
        "quantity": quantity,
        "reorder_level": reorder_level,
        "stock_status": stock_status,
        "last_updated": (
            datetime.today() -
            timedelta(days=random.randint(0, 365))
        ).strftime("%Y-%m-%d")
    })

# ------------------------------------------
# Create DataFrame
# ------------------------------------------

df = pd.DataFrame(inventory)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_RECORDS} inventory records.")
print(f"Saved to: {OUTPUT_PATH}")