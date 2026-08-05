import os
import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker("en_IN")

# Number of customers
NUM_CUSTOMERS = 500

# Output path
OUTPUT_PATH = "datasets/raw/customers.csv"

# Cities and states
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

# Create DataFrame
df = pd.DataFrame(customers)

# Create output directory if it doesn't exist
os.makedirs("datasets/raw", exist_ok=True)

# Save CSV
df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated {NUM_CUSTOMERS} customers.")
print(f"Saved to: {OUTPUT_PATH}")