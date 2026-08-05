import os
import random
import pandas as pd



NUM_SUPPLIERS = 50
OUTPUT_PATH = "datasets/raw/suppliers.csv"



supplier_names = [
    "ABC Distributors",
    "Fresh Foods Pvt Ltd",
    "Global Beverages",
    "Amul Distribution",
    "Pepsi Supply Chain",
    "Coca Cola India",
    "Britannia Foods",
    "Nestle India",
    "ITC Foods",
    "Hindustan Unilever",
    "Reliance Retail Supply",
    "Metro Cash & Carry",
    "BigBasket Suppliers",
    "D-Mart Wholesale",
    "Future Retail Supply",
    "Safal Frozen Foods",
    "McCain India",
    "Colgate India",
    "Dabur India",
    "Godrej Consumer",
    "Marico Limited",
    "Parle Products",
    "Patanjali Foods",
    "Paper World",
    "Office Essentials"
]

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
    ("Lucknow", "Uttar Pradesh")
]

suppliers = []



for i in range(1, NUM_SUPPLIERS + 1):

    city, state = random.choice(locations)

    supplier = {
        "supplier_id": f"S{i:04d}",
        "supplier_name": random.choice(supplier_names) + f" {i}",
        "city": city,
        "state": state
    }

    suppliers.append(supplier)


df = pd.DataFrame(suppliers)

os.makedirs("datasets/raw", exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_SUPPLIERS} suppliers.")
print(f"Saved to: {OUTPUT_PATH}")