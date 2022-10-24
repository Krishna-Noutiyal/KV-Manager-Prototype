import mysql.connector as sql
import json
  # Connecting to the DATABASE
Db = sql.connect(host="localhost", user="root",
                 passwd="19780000", database="flask", autocommit=True, auth_plugin='mysql_native_password')

# Cursor on the DATABASE
cr = Db.cursor()
# cr.execute("use news")


def Get_News(Class="Class", Teacher="Teacher"):
    
    cr.execute("Select * from news;")
    lst = cr.fetchall()
    print(lst)   
    return lst

if __name__ == "__main__":
    pass

