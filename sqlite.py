import sqlite3

#conn = sqlite3.connect('temperature.db')
#c = conn.cursor()
# c.execute("""CREATE TABLE temperature (
#                date text,
#                degrees real
#                )""")
# conn.close


def DeleteFromDB(c, conn):
    c.execute('DELETE FROM temperature')
    conn.commit()


def UpdateData(c, conn, list1, list2):
    for date, degrees in zip(list1, list2):
        c.execute("INSERT INTO temperature VALUES((?), (?))", (date, degrees))
    conn.commit()


def ShowData(c):
    c.execute("SELECT * FROM temperature")
    rows = c.fetchall()
    for row in rows:
        print(row)
