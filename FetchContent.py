
def sql(query):
    """ Takes a query as input 
        Optional arguments are Serial No, Class and Teacher
        if arguments are passed it executes the query with 
        arguments

        Args:
            query (str): Query to be executed
            Serial No (str): Serial No
            Class (str): Class
            Teacher (str): Teacher

        Returns:
            str: Result of the query

        Caution:
            Write %s in the query to formate the data
    """

    import pymysql as sql
    # Connecting to the DATABASE
    Db = sql.connect(host="localhost", user="root",
                     passwd="19780000", database="Flask", autocommit=True)

    # Cursor on the DATABASE
    cr = Db.cursor()
    cr.execute(query)

    Fetch = cr.fetchall()

    # Closing the cursor
    cr.close()
    # Closing the connection
    Db.close()

    return Fetch


def Get_News(Sr="sr", Class= "Class", Teacher= "Teacher"):
    """ 
    Returns the News related to the given arguments

    Args:
        Sr (str): Serial No
        Class (str): Class
        Teacher (str): Teacher

    """

    lst = sql(f"Select * from news where sr = {Sr} and class = {Class} and Teacher = {Teacher} Order By Sr Desc;")

    return lst


def Get_Event(Sr="sr", Class= "Class", Teacher= "Teacher"):
    """ 
    Returns the News related to  arg

    Args:
        Sr (str): Serial No
        Class (str): Class
        Teacher (str): Teacher
        
    """
    # Since there are Some Null values in class  wrote the query like this 
    lst = sql(f"Select * from events where Sr = {Sr} and (Class = {Class} or Class is null) and Teacher = {Teacher} Order By Sr Desc;")
    return lst


def Get_Newses():
    lst = sql("Select * from news order by sr desc;")
    return lst


def Get_Events():
    lst = sql("Select * from events Order By Sr Desc;")
    return lst


def Get_Classwork():
    lst = sql("Select * from classwork;")

    return lst