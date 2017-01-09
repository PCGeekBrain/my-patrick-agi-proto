import sqlite3, os, sys

#SQL FUNCTIONS

#CHECK IF DB IS ALIVE
class sqlitedb:
	
	def __init__(self, dbPathName):
		self.dbPath = dbPathName
	def checkDB(self):
		if os.path.isfile(self.dbPath) == False:
			conn = sqlite3.connect(self.dbPath)
			conn.execute("CREATE TABLE queue(caller_id TEXT NOT NULL, context TEXT NOT NULL, extension TEXT NOT NULL, priority TEXT NOT NULL);")
			conn.commit()
			conn.close()
	
	#ADD TO DB
	def add_to_queue(self, caller_id, context, extension, priority):
		self.checkDB()
		if len(caller_id) > 10:
			caller_id = caller_id[-10:]
		conn = sqlite3.connect(self.dbPath)
		conn.execute("INSERT INTO queue (caller_id, context, extension, priority) VALUES ('{0}', '{1}','{2}','{3}');".format(caller_id,context,extension,priority))
		conn.commit()
		conn.close()
	
	#GET FROM QUEUE
	def get_from_queue(self, query, agi):
		self.checkDB()
		returnData = ""
		conn = sqlite3.connect(self.dbPath)
		x = conn.execute("SELECT * FROM queue WHERE caller_id={0};".format(query)).fetchall()
		agi.verbose("PYTHON: DB QUERY: {0} -> {1} RESULTS".format(query ,str(len(x))))
		if len(x) > 0:
			returnData = x[0]
			agi.verbose("PYTHON: RETURNING RESULT 0 -> ({0}), DELETEING ALL RESULTS".format(str(x[0])))
			try:
				agi.verbose("PYTHON: QUERY -> DELETE FROM queue WHERE caller_id='{0}';".format(query))
				z = conn.execute("DELETE FROM queue WHERE caller_id='{0}';".format(query))
				conn.commit()
				agi.verbose("DATA DELEATED: z -> " + str(len(z.fetchall())))
			except:
				agi.verbose("ERROR:")
				e = sys.exc_info()
				agi.verbose(str(e))
		conn.close()
		agi.verbose("PYTHON RETURNING DATA AFTER DELEATION")
		return returnData

	#GET ALL THE ROWS IN THE DATABASE
	def get_all(self):
		self.checkDB()
		returnList = []
		conn = sqlite3.connect(self.dbPath)
		for queue in conn.execute("SELECT caller_id, context, extension, priority FROM queue ORDER BY caller_id;"):
			returnList.append(queue)
		conn.close()
		return returnList

	#REMOVE A CALLER ID FROM THE DATABASE
	def remove_from_db(self, caller_id):
		self.checkDB()
		conn = sqlite3.connect(self.dbPath)
		try:
			conn.execute("DELETE FROM queue WHERE caller_id={0};".format(caller_id))
		except:
			pass
		conn.commit()
		conn.close()

