import re
import sqlite3

def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def min_int(a,b):
    if a < b:
        return a
    else:
        return b

""" La médiane renvoit la valeur basse
"""
def mediane_int(l):
	if (l == []):
		return None
	tmp = l
	tmp.sort()
	lon = len(tmp)
	if lon % 2 == 0:
		return tmp[len(tmp) // 2 - 1]
	else:
		return tmp[len(tmp) // 2]

def add_user(username, password, spublickey, sprivatekey, epublickey, eprivatekey):
	# Check password
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	pat = re.compile(reg)
	mat = re.search(pat, password)
	if not mat:
		return None
	
	# Check key lenght
	if len(spublickey) != 128 or len(sprivatekey) != 128 or len(epublickey) != 128 or len(eprivatekey) != 128:
		return None
	
	# Check unique username
	conn = sqlite3.connect('test.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	query = "SELECT * FROM users WHERE username='" + username + "'"
	c.execute(query)
	rows = c.fetchall()
	if len(rows) != 0:
		return None

	c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", (username, password, spublickey, sprivatekey, epublickey, eprivatekey))

	conn.commit()
	conn.close()
		
	return username

def login(username, password):
	pass