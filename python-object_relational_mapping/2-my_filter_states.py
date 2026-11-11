#!/usr/bin/python3
"""Display states matching a user-provided name."""

import sys

import MySQLdb


def get_states(username, password, database, state_name):
    """Retrieve and print states matching the given name."""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()

    query = (
        "SELECT * FROM states WHERE name = BINARY '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
