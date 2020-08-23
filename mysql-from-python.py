import pymysql
import os

""" Get Username """
username = os.getenv('C9_user')

""" Connect to the Database Object """
connection = pymysql.connect(host='localhost', 
                            user=username,
                            password='',
                            db= 'Chinook')

try:
    # Run a Query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close connection to SQL
    connection.close()
