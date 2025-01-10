#!/usr/bin/python3
"""
Get MySQL credentials and database name from arguments
Connect to MySQL server on localhost at port 3306
Create a cursor to execute sql all queries
SQL query to select states with names starting with 'N' order by states.id
Fetch all the results
Display the results
Close cursor and database connection
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
