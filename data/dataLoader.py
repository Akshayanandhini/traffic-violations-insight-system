import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "akshaya",
    password="221203",
    database = "traffic_violations_db"
)

cursor = connection.cursor()

df = pd.read_csv("../dataset/traffic_violations_cleaned.csv")

df['Stop_dateTime'] = pd.to_datetime(
    df['Stop_dateTime'],
    format='%d-%m-%Y %H:%M'
)


df = df.where(pd.notnull(df), None)

query = """
INSERT INTO traffic_violations (
    SeqID,
    Stop_dateTime,
    Month,
    Weekday,
    Hour,
    TimeOfDay,
    Violation_category,
    `Violation Type`,
    Charge,
    Location_clean,
    Latitude,
    Longitude,
    State,
    Race,
    Gender,
    `Driver City`,
    `Driver State`,
    `DL State`,
    VehicleCategory,
    Make,
    Model,
    Year,
    Color,
    Accident,
    `Personal Injury`,
    `Property Damage`,
    Fatal,
    `Contributed To Accident`,
    Alcohol,
    Belts,
    `Work Zone`,
    `Search Conducted`,
    ArrestTypeCategory
)
VALUES (
    %s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,
    %s,%s,%s
)"""

# batch Insert:

batch_size = 10000
batch = []

total_rows = len(df)

for idx, row in enumerate(df.itertuples(index=False),start = 1):
    batch.append(tuple(row))

    if len(batch) == batch_size:
        cursor.executemany(query,batch)
        connection.commit()

        print(f"Inserted {idx:,} rows")

        batch = []

if batch:
    cursor.executemany(query,batch)
    connection.commit()
    print(f"Inserted final batch")
cursor.close()
connection.close()

print("Data Insertion completed")