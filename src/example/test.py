# 连接数据库
import mysql.connector
from mysql.connector import errorcode

try:
    database = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='1244303915',
        database='project_website'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
