import os
import random
import pandas as pd

# ------------------------------------------
# Configuration
# ------------------------------------------

NUM_WAREHOUSES = 20
OUTPUT_PATH = "datasets/raw/warehouses.csv"

# ------------------------------------------
# Warehouse Locations
# ------------------------------------------

locations = [
    ("Bangalore", "Karnataka"),
    ("Mumbai", "Maharashtra"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Delhi", "Delhi"),
    ("Pune", "Maharashtra"),
    ("Ahmedabad", "Gujarat"),
    ("Kolkata", "West Bengal"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"),
    ("Kochi", "Kerala"),
    ("Bhubaneswar", "Odisha"),
    ("Indore", "Madhya Pradesh"),
    ("Nagpur", "Maharashtra"),
    ("Surat", "Gujarat")
]

warehouse_types = [
    "Regional Distribution Center",
    "Fulfillment Center",
    "Cold Storage",
    "Retail Distribution Hub"
]

warehouses = []

# ------------------------------------------
# Generate Warehouses
# ------------------------------------------

for i in range(1, NUM_WAREHOUSES + 1):

    city, state = random.choice(locations)

    warehouses.append({
        "warehouse_id": f"W{i:03d}",
        "warehouse_name": f"{city} Warehouse {i}",
        "city": city,
        "state": state,
        "warehouse_type": random.choice(warehouse_types),
        "capacity": random.randint(5000, 50000)
    })

# ------------------------------------------
# Create DataFrame
# ------------------------------------------

df = pd.DataFrame(warehouses)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_WAREHOUSES} warehouses.")
print(f"Saved to: {OUTPUT_PATH}")