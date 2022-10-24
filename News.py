import json
import mysql.connector as sql

# Connecting to the DATABASE
Db = sql.connect(host="localhost", user="root",
                 passwd="19780000", database="Flask", autocommit=True, auth_plugin='mysql_native_password')

# Cursor on the DATABASE
cr = Db.cursor()


def Get_News(Class="Class",Teacher="Teacher"):

    cr.execute("Select * from news;")
    lst = cr.fetchall()
    # print(json.dumps(lst))
    return lst