# coding=utf-8
import math
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

def moyenne_int(l):
	moyenne = sum(l)/float(len(l))
	return moyenne

def ecart_type_int(list):
	if (list == []):
		return None

	mean = sum(list) / len(list)
	var = sum((l-mean)**2 for l in list) / len(list)
	st_dev = math.sqrt(var)

	return st_dev

def is_geometric(li):
	if (li == []):
		return None

	if len(li) <= 1:
		return True

	ratio = li[1]/float(li[0])
	for i in range(1, len(li)):
		if (li[i]/float(li[i-1])) != ratio:
			return False
	return True

def is_arithmetic(li):
	if (li == []):
		return None

	if len(li) <= 1:
		return True

	diff = li[1] - float(li[0])
	for i in range(1, len(li)):
		if (li[i] - float(li[i-1])) != diff:
			return False
	return True

def get_next_geometric(li, n):
	if (li == []):
		return None

	if is_geometric(li) == False:
		return False

	ratio = li[1]/float(li[0])
	prec = li[len(li)-1]

	next_val = []

	for i in range(n):
		val = prec * ratio
		next_val.append(val)
		prec = val

	return True, next_val

def get_next_arithmetic(li, n):
	if (li == []):
		return None

	if is_arithmetic(li) == False:
		return False

	diff = li[1] - float(li[0])
	prec = li[len(li)-1]

	next_val = []

	for i in range(n):
		val = prec + diff
		next_val.append(val)
		prec = val

	return True, next_val
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
	conn = sqlite3.connect('test.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	query = "SELECT * FROM users WHERE username='" + username + "'"
	c.execute(query)
	rows = c.fetchall()
	for row in rows:
		if row['password'] == password:
			return True
	
	return False

def get_keys(username):
	conn = sqlite3.connect('test.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	query = "SELECT * FROM users WHERE username='" + username + "'"
	c.execute(query)
	rows = c.fetchall()
	keys = {}
	for row in rows:
		keys["spublickey"] = row["spublickey"]
		keys["sprivatekey"] = row["sprivatekey"]
		keys["epublickey"] = row["epublickey"]
		keys["eprivatekey"] = row["eprivatekey"]
	
	return keys

def is_db_corrupted():
	conn = sqlite3.connect('test.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	query = "SELECT * FROM users"
	c.execute(query)
	rows = c.fetchall()
	for row in rows:
		# Check password
		password = row["password"]
		reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
		pat = re.compile(reg)
		mat = re.search(pat, password)
		if not mat:
			return True

		# Check key lenght
		spublickey = row["spublickey"]
		sprivatekey = row["sprivatekey"]
		epublickey = row["epublickey"]
		eprivatekey = row["eprivatekey"]
		if len(spublickey) != 128 or len(sprivatekey) != 128 or len(epublickey) != 128 or len(eprivatekey) != 128:
			return True
		
		# Check uniqueness
		username = row["username"]
		query = "SELECT * FROM users WHERE username='" + username + "'"
		c.execute(query)
		rows = c.fetchall()
		if len(rows) > 1:
			return True
	
	return False
