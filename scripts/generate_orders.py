import os
import random
import pandas as pd
from datetime import datetime, timedelta

# ------------------------------------------
# Configuration
# ------------------------------------------

NUM_ORDERS = 10000
OUTPUT_PATH = "datasets/raw/orders.csv"

# ------------------------------------------
# Read Required Datasets
# ------------------------------------------

customers = pd.read_csv("datasets/raw/customers.csv")
products = pd.read_csv("datasets/raw/products.csv")
warehouses = pd.read_csv("datasets/raw/warehouses.csv")

order_status = [
    "Completed",
    "Pending",
    "Cancelled"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

orders = []

# ------------------------------------------
# Generate Orders
# ------------------------------------------

for i in range(1, NUM_ORDERS + 1):

    customer = customers.sample(1).iloc[0]
    product = products.sample(1).iloc[0]
    warehouse = warehouses.sample(1).iloc[0]

    quantity = random.randint(1, 10)

    selling_price = float(product["selling_price"])

    subtotal = quantity * selling_price

    # Discount between 0% and 20%
    discount = round(subtotal * random.uniform(0, 0.20), 2)

    final_amount = round(subtotal - discount, 2)

    order_date = (
        datetime.today()
        - timedelta(days=random.randint(0, 365))
    ).strftime("%Y-%m-%d")

    orders.append({
        "order_id": f"O{i:06d}",
        "customer_id": customer["customer_id"],
        "product_id": product["product_id"],
        "warehouse_id": warehouse["warehouse_id"],
        "quantity": quantity,
       "selling_price": selling_price,
        "discount": discount,
        "final_amount": final_amount,
        "payment_method": random.choice(payment_methods),
        "order_status": random.choice(order_status),
        "order_date": order_date
    })

# ------------------------------------------
# Save CSV
# ------------------------------------------

df = pd.DataFrame(orders)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_ORDERS} orders.")
print(f"Saved to: {OUTPUT_PATH}")