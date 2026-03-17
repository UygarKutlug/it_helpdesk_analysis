import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n = 1000

categories = ["Network", "Software", "Hardware", "Security"]
priorities = ["Low", "Medium", "High"]
teams = ["Team A", "Team B", "Team C"]

start_date = datetime(2025, 1, 1)

data = []

for i in range(n):
    open_date = start_date + timedelta(days=np.random.randint(0, 180))
    resolution_time = np.random.randint(4, 96)
    close_date = open_date + timedelta(hours=resolution_time)

    category = np.random.choice(categories)
    priority = np.random.choice(priorities)

    if priority == "High":
        sla = 24
    elif priority == "Medium":
        sla = 48
    else:
        sla = 72

    data.append([
        i+1,
        open_date,
        close_date,
        category,
        priority,
        np.random.choice(teams),
        sla,
        resolution_time
    ])

df = pd.DataFrame(data, columns=[
    "Ticket_ID", "Open_Date", "Close_Date",
    "Category", "Priority", "Assigned_Team",
    "SLA_Hours", "Resolution_Hours"
])

df.to_csv("it_tickets.csv", index=False)

print("Dataset oluşturuldu!")
