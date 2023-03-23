import os
import mysql.connector as mysql


db = mysql.connect(
    host='localhost',
    user='root',
    password="root",
    database='CST1510dbs'
)