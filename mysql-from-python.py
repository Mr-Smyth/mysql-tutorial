import pymysql
import datetime
import os

""" Get Username """
username = os.getenv('C9_user')

""" Connect to the Database Object """
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a Query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['Archibald', 'Steve', 'Dave']
        # Prepare a string, with the same number of placeholders as
        # the list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        # The format() method formats the specified value(s) and
        # insert them inside the string's placeholder.
        cursor.execute("DELETE From Friends WHERE name in ({});".format(
            format_strings), list_of_names)
        connection.commit()

finally:
    # Close connection to SQL
    connection.close()
