from fileinput import filename
from flask import Flask, render_template, redirect, url_for, request, session
from cryptography.fernet import Fernet
import json
import pymysql as sql

from FetchContent import Get_News, Get_Newses, Get_Event, Get_Events, Get_Classwork

app = Flask(__name__)
app.secret_key = "SecretKey"
UserName = ""
Passwd = ""

# Display: Msg1 displayed if UserName and Password is incorrect
Display = ""

# Display: Msg2 displayed if UserName and Password is incorrect
Display1 = ""

# Msg Displayed when redirected from the Signup page to the Login Page
SingupDisplay = ""
SingupDisplay1 = ""


def Key():
    """Returns the Key to be used"""
    return open("Encryption.key", "rb").read()


def Encrypt(String, Key=Key()):
    """Encrypts a string \nReturns Encrypted string"""
    return Fernet(Key).encrypt(String.encode())


def Decrypt(String, Key=Key()):
    """Decrypts a string \nReturns Decrypted string"""
    return Fernet(Key).decrypt(String).decode()


""" Mode of the body"""


@app.route("/Mode/", methods=['POST', 'GET'])
def UpdateMode():
    """Checks if User has toggled dark mode add 'dark' in BodyMode if DARK MODE is enabled else blank"""
    # If the Toggle Mode Button is pressed
    # JS generates a Post request with the ITS DATA = CLASS OF THE BODY
    if request.method == "POST":

        # Variable containing the Class of the Body
        RequestContent = json.loads(request.data)
        # print(f"Theme of the Website : {RequestContent}")

        # Setting the BodyMode
        session["Mode"] = RequestContent
        print(f"\n\n\n\nMode of the body :{session['Mode']}\n\n\n")
        return f"Website Mode changed to {'Dark' if session['Mode'] == 'dark' else 'Light'} Successfully"

    # To set the Mode of the website JS automatically
    # Sends a GET request to get the Current mode of the body
    # Returns the Mode of the body to JS
    else:
        return session["Mode"]


""" Home page"""


@app.route("/")
def Index():
    # If the user has logged in to the WEBSITE
    try:
        if session["Log"] == True and session["Admin"]:
            return render_template("Index.html", Content=f"Logged in As Admin Successfully !!")
        
        elif session["Log"] == True:
            return render_template("Index.html", Content=f"Logged in Successfully !!")
        
        
        # If the user has not yet Logged in to the WEBSITE
        else:
            return render_template("Index.html", Content="Welcome to Home Page !!")

    except:
        return render_template("Index.html", Content="Welcome to Home Page !!")
    




""" Login PAGE """


@app.route("/User_Admin_Login", methods=["POST", "GET"])
def User_Admin_Login():

    return render_template("User-Admin-Login.html")


""" Login PAGE """


@app.route("/Login", methods=["POST", "GET"])
def Login():
    """Saves UserName and Password in the Global Variables and changes log = True"""
    global Display
    global Display1
    global SingupDisplay
    global SingupDisplay1

    # Style of the Warning
    Style = 'style="font-size: 19px; color: red; text-align: center;"'

    #   If the Form is Submitted
    if request.method == "POST":

        # Try except if UserName and Password are not in the DATABASE
        try:

            # Gets the data from the server and stores it in UserInfo dictionary (Username: Password)
            cr.execute("select username,passwd,email from flask;")
            UserInfo = {i[0]: [Decrypt(i[2]), Decrypt(i[1])]
                        for i in cr.fetchall()}

            # print("This function ran !!!")
            # for i, j in UserInfo.items():
            #     print(f"UserName : {i}")
            #     print(f"Email : {j[0]}")
            #     print(f"Passwd : {j[1]}")

            
            # UserName taken from the FORM
            UserName = request.form["Usr"]
            # Passwd was taken from the FORM
            Passwd = request.form['Passwd']
            # If Credentials in the database does not match the User Input
            # Raises an Exception
            if UserInfo[UserName][1] != Passwd:

                raise Exception("Wrong UserName")

            # If Credentials match Sets log variable = true
            # Means the user is now Logged in to the Website
            else:

                # Log = True if the user has logged in to the website
                session["Log"] = True

                return redirect(url_for("Index"))

        # If Exception Occurs Changes Display and Displa1 variable
        # And Renders the Login page again but with the Msg of Display and Display1
        except Exception as e:
            Display = "Wrong Username or Password"
            Display1 = "!! TRY AGAIN !!"

            return render_template("Login.html", Style=Style, Msg1=Display, Msg2=Display1)

    
    else:
        """
    If the User has not yet Logged in to the website  OR
    If the User has ALREADY logged in to the website
    """
        # If the user has clicked the log in button

        try :
            if session["Log"] == False and SingupDisplay == "" and SingupDisplay1 == "":

                # Style of the Warning
                Style = 'style="font-size: 19px; color: red; text-align: center; display: none; "'

                return render_template("Login.html", Style=Style, Msg1=Display, Msg2=Display1)

            # If the user has been redirected to Login from the Signup Page
            elif session["Log"] == False and SingupDisplay != "" and SingupDisplay1 != "":
                a = SingupDisplay
                b = SingupDisplay1
                SingupDisplay = ""
                SingupDisplay1 = ""

                # Changeing the Warning colour to orange
                Style = Style.replace("red", "orange")
                return render_template("Login.html", Style=Style, Msg1=a, Msg2=b)
            
        except:
            return render_template("Login.html")


@app.route("/AdminLogin", methods=["POST", "GET"])
def AdminLogin():
    """Saves UserName and Password in the Global Variables and changes log = True"""
    global Display
    global Display1
    global SingupDisplay
    global SingupDisplay1

    # Style of the Warning
    Style = 'style="font-size: 19px; color: red; text-align: center;"'

    #   If the Form   is Submitted
    if request.method == "POST":

        # Try except if UserName and Password are not in the DATABASE
        try:

            # Gets the data from the server and stores it in the UserInfo dictionary (Username: Password)
            cr.execute("select username,passwd,email from flask;")
            UserInfo = {i[0]: [Decrypt(i[2]), Decrypt(i[1])]
                        for i in cr.fetchall()}

            
            # UserName taken from the FORM
            UserName = request.form["Usr"]
            # Passwd was taken from the FORM
            Passwd = request.form['Passwd']
            
            # If Credentials in the database does not match the User Input
            # Raises an Exception
            if UserInfo[UserName][1] != Passwd:

                raise Exception("Wrong UserName")

            # If Credentials match Sets log variable = true
            # Means the user is now Logged in to the Website
            else:

                # Log = True if the user has logged in to the website
                session["Log"] = True

                """ Admin = True to let know if the account logged in is admin"""

                session["Admin"] = True
                print(f"\n\n\n\n {session['Admin']}\n\n\n\n")
                return redirect(url_for("Index"))

        # If Exception Occurs Changes Display and Displa1 variable
        # And Renders the Login page again but with the Msg of Display and Display1
        except Exception as e:
            Display = "Wrong UserName or Password"
            Display1 = "!! TRY AGAIN !!"

            return render_template("AdminLogin.html", Style=Style, Msg1=Display, Msg2=Display1)
    else:
        return render_template("AdminLogin.html")
""" Logout PAGE """


@app.route("/logout")
def Logout():
    session["Log"] = False
    session["Admin"] = False
    # return redirect(url_for("Index"))
    return render_template("Index.html", Content = "Logged Out Successfully")


""" Signup Page """


@app.route("/Signup", methods=["POST", "GET"])
def Signup():
    global Display
    global Display1
    global SingupDisplay
    global SingupDisplay1
    Msg1 = ""
    Msg2 = ""
    Style = 'style="font-size: 20px; color: red; text-align: center; display: none;"'

    # If users submit the form
    if request.method == "POST":

        # Storing the form input to variables
        UserName = request.form["Usr"]
        Email = request.form["Email"].lower()
        Passwd = Encrypt(request.form["Passwd"])

        # Throws Error if the Email and UserName already exist in the database
        # If not exist add the new user to the database
        try:
            if Email == "":
                raise Exception("Wrong Email !!!")

            # Executing MySQL query
            cr.execute("select email from flask;")

            # List of all emails on the server
            l = [Decrypt(j) for i in cr.fetchall() for j in i]
            # print(l)

            # IF email is in Database Throws and error
            if Email in l:
                raise Exception("Email already used !!")

            # Else Adds a new user to the Database
            else:
                # Encrypting the Email before sending it to the Database
                Email = Encrypt(Email)

                cr.execute(
                    "INSERT INTO flask(UserName,Passwd,Email) values(%s,%s,%s);", (UserName, Passwd, Email))

                # Commiting the changes
                Db.commit()

                # print(l)

                SingupDisplay = "!!! Successfully Signed Up !!!"
                SingupDisplay1 = "You Can Login Now"
                return redirect(url_for("Login"))

        except Exception as e:
            print(e)
            Msg1 = "UserName or Email already Taken" if Email != "" else "Email Can't be empty"
            Msg2 = "!! Use another UserName or Email !!"

            Style = Style.replace("display: none;", "")
            redirect(url_for("Signup"))

    return render_template("Signup.html", Style=Style, Msg1=Msg1, Msg2=Msg2)


""" Forgot Page"""


@app.route("/Forgotpasswd", methods=["POST", "GET"])
def Forgot():
    Style = 'style="font-size: 19px; color: red; text-align: center;"'
    # If the request is POST
    if request.method == "POST":

        # Email Entered by the user
        Email = request.form["Email"]

        try:
            # SQL Query to retrieve UserName Email and Password from the database
            cr.execute("select Username,Email,Passwd from flask;")

            # List containing the data of the user in Decrypted form
            Lst = [[i[0], Decrypt(i[1]), Decrypt(i[2])] for i in cr.fetchall()]
            for i in Lst:

                # If the Email is in database
                if i[1] == Email:

                    # Changes the style color to orange
                    Style = Style.replace("red", "orange")

                    # Renders the forget.html with UserName and Password of the Associated Email
                    return render_template("Forgot.html", Style=Style, Msg1=f"UserName : {i[0]}", Msg2=f"Password : {i[2]}")

            raise Exception("Email Not Associated with any Account")
        except Exception as e:
            return render_template("Forgot.html", Style=Style, Msg1=f"No Account Found Associated With", Msg2=f"{Email}")

    # Changes the style Display: none; to avoid unnecessary spacing if no warning is displayed
    Style = 'style="font-size: 19px; color: red; text-align: center; display : none ;"'
    return render_template("Forgot.html", Style=Style)














""" Other Pages"""


@app.route("/Events", methods=["GET", "POST"])
def Events():
    return render_template("Events.html", Content=Get_Events())


@app.route("/News", methods=["GET", "POST"])
def News():
    return render_template("News.html", Content=Get_Newses())



@app.route("/Classwork", methods=["GET", "POST"])
def Classwork():
    Work = Get_Classwork()
    return render_template("Classwork.html",Length = len(Work), Content= Work)


@app.route("/Homework", methods=["GET", "POST"])
def Homework():
    return render_template("Homework.html")


@app.route("/T_Console", methods=["GET", "POST"])
def T_Console():
    return render_template("T_Console.html")


@app.route("/Post/<NewsOrPost>/<SerialNo>", methods=["GET", "POST"])
def Post(NewsOrPost, SerialNo):

    if NewsOrPost == "News":
        try:
            return render_template("Post.html", Cnt=Get_News(Sr=SerialNo)[0])
        except:
            return redirect(url_for('ReRoute', i="Something went wrong"))
    elif NewsOrPost == "Post":

        try:
            return render_template("Post.html", Cnt=Get_Event(Sr=SerialNo)[0])
        except:
            return redirect(url_for('ReRoute', i="Something went wrong"))


""" Change Credentials """


@app.route("/ChangeCredentials", methods=["POST", "GET"])
def ChangeCredentials():
    global cr
    global Db

    # Style for the Msg
    Style = 'style="font-size: 18px; color: red; text-align: center; display: none;"'

    # If the request is POST
    if request.method == "POST":

        # Storing the form input to variables
        Email = request.form["Email"].lower()
        UserName = request.form["Usr"]
        Passwd = Encrypt(request.form["Passwd"])

        # SQL Query to retrieve UserName Email and Password from the database
        cr.execute("select Username,Email,Passwd from flask;")

        # List containing the data of the user in Decrypted form
        Lst = [[i[0], i[1], i[2]] for i in cr.fetchall()]

        for i in Lst:

            # If the UserName and Email matches
            if i[0] == UserName and Decrypt(i[1]) == Email:

                # Style for the Message
                Style = Style.replace("display: none;", "")
                Style = Style.replace("red", "orange")

                # Updates the Username Email and Password
                cr.execute("UPDATE flask SET USERNAME = %s, EMAIL = %s, PASSWD = %s WHERE USERNAME = %s and EMAIL = %s;",
                           (UserName, Encrypt(Email), Passwd, UserName, i[1]))
                return render_template("ChangeCredentials.html", Style=Style, Msg0=f"New Credentials !!", Msg1=f"Username : {UserName}", Msg2=f"Email : {Email}", Msg3=f"Password : {Decrypt(Passwd)}")

            # elif Decrypt(i[1]) == Email:
            #     cr.execute("UPDATE flask SET USERNAME= %s, PASSWD= %s WHERE EMAIL= %s;",(UserName,Passwd,i[1]))
                # return render_template("ChangeCredentials.html",Warning="orange",Msg0=f"New Credentials !!", Msg1=f"Username : {UserName}", Msg2=f"Email : {Email}", Msg3=f"Password : {Decrypt(Passwd)}")

        # Style for the Msg
        Style = Style.replace("display: none;", "")

        # After the for loop if the Username and Email don't match Throws an error on the page
        return render_template("ChangeCredentials.html", Style=Style, Msg0=f"Credentials Doesn't Match", Msg1=f"!! Enter Email or UserName Correctly !!")

    # If the request is GET
    else:
        return render_template("ChangeCredentials.html", Style=Style)


@app.route("/<i>/")
def ReRoute(i=str):
    return render_template("PageNotFound.html")


if __name__ == "__main__":

    # Connecting to the DATABASE
    # Db = sql.connect(host="localhost", user="root",
    #                  passwd="YourPassword", database="Flask", autocommit=True, auth_plugin='mysql_native_password')
    Db = sql.connect(host="localhost", user="root",
                     passwd="YourPassword", database="Flask", autocommit=True)

    # Cursor on the DATABASE
    cr = Db.cursor()

    app.run(debug=True, host="0.0.0.0", port=80)
