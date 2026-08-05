import os
import random
import pandas as pd
from datetime import datetime, timedelta



OUTPUT_PATH = "datasets/raw/shipments.csv"



orders = pd.read_csv("datasets/raw/orders.csv")
warehouses = pd.read_csv("datasets/raw/warehouses.csv")

shipment_status = [
    "Delivered",
    "In Transit",
    "Delayed"
]

carrier_names = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ekart",
    "XpressBees",
    "India Post"
]

shipments = []


for i, order in enumerate(orders.itertuples(index=False), start=1):

    warehouse = warehouses[
        warehouses["warehouse_id"] == order.warehouse_id
    ].iloc[0]

    dispatch_date = (
        datetime.strptime(order.order_date, "%Y-%m-%d")
        + timedelta(days=random.randint(0, 2))
    )

    delivery_date = dispatch_date + timedelta(
        days=random.randint(1, 7)
    )

    shipments.append({
        "shipment_id": f"SH{i:06d}",
        "order_id": order.order_id,
        "warehouse_id": warehouse["warehouse_id"],
        "carrier": random.choice(carrier_names),
        "shipment_status": random.choice(shipment_status),
        "dispatch_date": dispatch_date.strftime("%Y-%m-%d"),
        "delivery_date": delivery_date.strftime("%Y-%m-%d")
    })


df = pd.DataFrame(shipments)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {len(df)} shipments.")
print(f"Saved to: {OUTPUT_PATH}")