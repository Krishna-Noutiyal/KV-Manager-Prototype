import pymysql as sql

# Connecting to the DATABASE
Db = sql.connect(host="localhost", user="root",
                 passwd="19780000", database="Flask", autocommit=True)

# Cursor on the DATABASE
cr = Db.cursor()


def Get_News(Class="Class",Teacher="Teacher"):

    cr.execute("Select * from news order by sr desc;")
    lst = cr.fetchall()
    return lst

def Get_Events():

    cr.execute("Select * from events;")
    lst = cr.fetchall()
    return lst


