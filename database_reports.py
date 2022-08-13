import db_tools as db
import sqlite3 as sl


def print_str_db(input_str):
    for i in input_str:
        print(i)


con = sl.connect("pupils.db")
cur = con.cursor()

# cur.execute("SELECT * FROM PUPILS;")
cur.execute(
    "SELECT name,  MATHEMATICS, RUSSIAN, HISTORY FROM PUPILS, ESTIMATE  WHERE pupil_id = PUPILS.id"
)

print_str_db(cur.fetchall())
# print(cur.fetchall())

# cur.execute("""SELECT *, users.fname, users.lname FROM orders
#     LEFT JOIN users ON users.userid=orders.userid;""")
# print(cur.fetchall())


# db.read_data("pupils.db", "PUPILS")
