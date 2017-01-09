#!/usr/bin/python

"""

SCRIPT BY MENDEL HORNBACHER TO REROUTE CALLS IN ASTERISK BASED ON DB INPUT

STATUS: BUG FIXING

"""

from asterisk.agi import *

agi = AGI()

import sys

import sqlite3test

agi.verbose("PYTHON AGI SCRIPT: CONNECTING TO DATABASE")

db = sqlite3test.sqlitedb("/usr/agi/test.db")

agi.verbose("PYTHON AGI SCRIPT: STARTED")

agi.verbose("PYTHON AGI SCRIPT: CALLER ID -> " + agi.env['agi_callerid'])

agi.verbose("PYTHON AGI SCRIPT: CALLER ID TYPE -> " + str(type(agi.env['agi_callerid'])))

database = db.get_from_queue(agi.env['agi_callerid'], agi)

agi.verbose("PYTHON AGI SCRIPT: DATABASE TYPE -> "+str(type(database)))

if len(database) > 0:
	agi.verbose("PYTHON AGI SCRIPT: CALLER ID FOUND IN DB -> REROUTING CALLER ID -> " + str(database[0]))
	agi.goto_on_exit(context=str(database[1]), extension=str(database[2]), priority=str(database[3]))
else:
	agi.verbose("PYTHON AGI SCRIPT: CALLER ID NOT IN DB -> NOT REROUTING CALLER ID -> " +str(agi.env['agi_callerid']))
agi.verbose("PYTHON AGI SCRIPT: ENDED")
