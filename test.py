import sqlite3test
import sqlite3

db = sqlite3test.sqlitedb("/usr/agi/test.db")

print "WRITING TO DB"

db.add_to_queue("6016016611","test","1","1")

print db.get_all()

print "REMOVING FROM DB"

db.remove_from_db("6016016611")

print db.get_all()

conn = sqlite3.connect("test.db")
x = conn.execute("SELECT * FROM queue;").fetchall()

print "SIZE OF DB"
print(len(x))
