import os
import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='root',
    password=os.environ.get("SQL_PASSWORD", ""),
    database='CST1510dbs'
)