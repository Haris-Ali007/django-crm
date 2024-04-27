import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db = os.environ.get("DB")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")


connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port
)

connection.autocommit = True
cursor = connection.cursor()

sqlQuery = (f"CREATE DATABASE {db}")
cursor.execute(sqlQuery)

print('Database created...')
cursor.close()