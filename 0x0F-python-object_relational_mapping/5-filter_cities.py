#!/usr/bin/python3
"""
state listed as argument
list all cities of that state using database
"""

import sys
import MySQLdb

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    cursor = db.cursor()

    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
