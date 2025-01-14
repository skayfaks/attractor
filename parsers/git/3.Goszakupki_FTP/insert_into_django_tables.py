import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    host="localhost",
    port=os.environ.get("DB_PORT")
)
cursor = connection.cursor()

cursor.execute("SELECT id, filename, file_date, import_date, record_count, status FROM purchase_files")
purchase_files_data = cursor.fetchall()

for row in purchase_files_data:
    cursor.execute("INSERT INTO purchase_app_purchasefilesmodel (filename, file_date, import_date, record_count, status) VALUES (%s, %s, %s, %s, %s)", row[1:])

cursor.execute("SELECT id, externalId, planNumber, versionNumber, filename, archive_name FROM purchase_plan")
purchase_plan_data = cursor.fetchall()

for row in purchase_plan_data:
    cursor.execute('INSERT INTO "purchase_app_purchaseplanmodel" ("externalId", "planNumber", "versionNumber", "filename", "archive_name") VALUES (%s, %s, %s, %s, %s)', row[1:])


# Retrieve data from the purchase table
cursor.execute("SELECT id, externalId, total_price, purchase_object_info, publish_year, purchase_files FROM purchase")
purchase_data = cursor.fetchall()

for row in purchase_data:
    cursor.execute('INSERT INTO "purchase_app_purchasemodel" ("externalId", total_price, purchase_object_info, publish_year, purchase_files, "externalId_obj_id", purchase_files_obj_id) VALUES (%s, %s, %s, %s, %s, %s, %s)', row[1:] + (row[1], row[5]))

connection.commit()
connection.close()
