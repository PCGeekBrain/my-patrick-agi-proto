import sqlite3test, sys

db = sqlite3test.sqlitedb("test.db")

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

if len(sys.argv) == 5:
	print "ADDING TO DB"
	db.add_to_queue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	print "ADDED TO DB"
