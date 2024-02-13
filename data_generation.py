import csv
import random
from datetime import datetime, timedelta

from faker import Faker


faker = Faker()

# Pandas data file
header = ["FirstName", "LastName", "City", "PurchasePrice", "Quantity"]

data = []
for _ in range(30):
    column_data = {"FirstName": random.choice(["James", "Jessica", "Ryan", "Chris", "Jenn"]),
                   "LastName": faker.last_name(),
                   "City": faker.city(),
                   "PurchasePrice": round(random.uniform(1, 20), 2),
                   "Quantity": random.randint(1, 100)}
    data.append(column_data)

with open('test_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

# Generate plot data

header = ["Day", "Temperature"]

data = []
start_date = datetime(2000, 1, 1)
start_temperature = 20.5
for _ in range(100):
    start_date = start_date + timedelta(days=1)
    start_temperature = start_temperature + round(random.uniform(-2.0, 2.0), 2)
    column_data = {
        "Day": start_date.strftime("%Y-%m-%d"),
        "Temperature": start_temperature
    }
    data.append(column_data)

with open('plot_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
