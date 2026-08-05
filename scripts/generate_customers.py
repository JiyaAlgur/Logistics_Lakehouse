import os
import random
import pandas as pd
from faker import Faker


fake = Faker("en_IN")


NUM_CUSTOMERS = 500


OUTPUT_PATH = "datasets/raw/customers.csv"


locations = [
    ("Bangalore", "Karnataka"),
    ("Mumbai", "Maharashtra"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Delhi", "Delhi"),
    ("Pune", "Maharashtra"),
    ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh")
]

customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    city, state = random.choice(locations)

    customers.append({
        "customer_id": f"C{i:04d}",
        "customer_name": fake.name(),
        "city": city,
        "state": state,
        "email": fake.email()
    })


df = pd.DataFrame(customers)

os.makedirs("datasets/raw", exist_ok=True)


df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_CUSTOMERS} customers.")
print(f"Saved to: {OUTPUT_PATH}")