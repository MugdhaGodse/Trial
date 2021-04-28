import mysql.connector


def insert_data(uname, passwd):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO login(username, password) VALUES ("{0}","{1}");'.format(uname, passwd)
    dbcursor.execute(sql)
    mysqldb.commit()


def fetch_data():
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    dbcursor.execute("select * from login")
    result=dbcursor.fetchall()
    return result


def fetch_studentdetails():
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="botproject")
    dbcursor = mysqldb.cursor()
    dbcursor.execute("select * from studentdetails,login where studentdetails.Roll_no==login.username")
    result=dbcursor.fetchall()
    return result



