#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to select all states ordered by id ASC
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
