import mariadb
import sys

def dbConnect():
    """
    Returns a cursor to use for queries
    """
    try:
        conn = mariadb.connect(
                user="padmin",
                password="bulbizarre",
                host="0.0.0.0",
                port=3306,
                database="padmindb"
                )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn.cursor()

def updateAddress(place_id, address):
    cur = dbConnect()
    cur.execute(
            """
            UPDATE places
            SET address = ?
            WHERE place_id = ?
            """, (address, place_id))

def getTable(column):
    cur = dbConnect()
    cur.execute(f"SELECT * FROM {column}")
    print(column + ": ")
    return cur
