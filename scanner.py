import sqlite3

conn = sqlite3.connect('scanner.db')
c = conn.cursor()

def insert_req(cursor,domain,ip,host):
	cursor.execute("insert into requests values(datetime(),'%s','%s','%s')" % (domain,ip,host))

#for i in range(100,200):
#	insert_req(c,'http://www.google.com',('192.168.2.%s' % (i)) ,'QBA-PC')

conn.commit()

_cursor = conn.cursor()

def select_reqs():
	res = _cursor.execute("SELECT * FROM REQUESTS")
	return res;

allReqs = select_reqs()

for row in allReqs:
	print("%s %s %s %s" % (row[0],row[1],row[2],row[3]))	

conn.close()

