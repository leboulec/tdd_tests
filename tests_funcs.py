import funcs
import unittest
import sqlite3
import os

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_min_int(self):
		self.assertEqual(funcs.min_int(0,2),0)
		self.assertEqual(funcs.min_int(-1,-5),-5)
		self.assertEqual(funcs.min_int(-1,2),-1)
		self.assertEqual(funcs.min_int(0,0),0)

	def test_mediane_int(self):
		self.assertEqual(funcs.mediane_int([1, 5, 3, 2, 8]), 3)
		self.assertEqual(funcs.mediane_int([-1, -2, -10]), -2)
		self.assertEqual(funcs.mediane_int([10]), 10)
		self.assertEqual(funcs.mediane_int([0, -3, 8, 7]), 0)
		self.assertEqual(funcs.mediane_int([]), None)

	def test_moyenne_int(self):
		self.assertEqual(funcs.moyenne_int([1, 5, 3, 2, 8]), 3.8)
		self.assertEqual(funcs.moyenne_int([-1, -1, -10]), -4)
		self.assertEqual(funcs.moyenne_int([10, 10]), 10)
		self.assertEqual(funcs.moyenne_int([3, -3, 8, -8]), 0)

	def test_ecart_type_int(self):
		self.assertEqual(funcs.ecart_type_int([10, 8, 10, 8, 8, 4]), 2)
		self.assertEqual(funcs.ecart_type_int([3, 3, 3, 3]), 0)
		self.assertEqual(funcs.ecart_type_int([]), None)

	def test_is_geometric(self):
		self.assertEqual(funcs.is_geometric([2, 6, 18, 54]), True)
		self.assertEqual(funcs.is_geometric([10, 5, 2.5, 1.25]), True)
		self.assertEqual(funcs.is_geometric([5, 8, 9, 11]), False)
		self.assertEqual(funcs.is_geometric([10, 5, 2.5, 25]), False)
		self.assertEqual(funcs.is_geometric([]), None)

	def test_is_arithmetic(self):
		self.assertEqual(funcs.is_arithmetic([2, 4, 6, 8]), True)
		self.assertEqual(funcs.is_arithmetic([7, 5, 3, 1]), True)
		self.assertEqual(funcs.is_arithmetic([5, 8, 9, 11]), False)
		self.assertEqual(funcs.is_arithmetic([2, 4, 6, 10]), False)
		self.assertEqual(funcs.is_arithmetic([]), None)

	def test_get_next_geometric(self):
		self.assertEqual(funcs.get_next_geometric([1, 2, 4, 8], 4), (True, [16, 32, 64, 128]))
		self.assertEqual(funcs.get_next_geometric([10, 5, 2.5, 1.25], 2), (True, [0.625, 0.3125]))
		self.assertEqual(funcs.get_next_geometric([5, 8, 9, 11], 5), False)
		self.assertEqual(funcs.get_next_geometric([10, 5, 2.5, 25], 2), False)
		self.assertEqual(funcs.get_next_geometric([], 3), None)

	def test_get_next_arithmetic(self):
		self.assertEqual(funcs.get_next_arithmetic([2, 4, 6, 8], 4), (True, [10, 12, 14, 16]))
		self.assertEqual(funcs.get_next_arithmetic([7, 5, 3, 1], 2), (True, [-1, -3]))
		self.assertEqual(funcs.get_next_arithmetic([5, 8, 9, 11], 5), False)
		self.assertEqual(funcs.get_next_arithmetic([2, 4, 6, 10], 2), False)
		self.assertEqual(funcs.get_next_arithmetic([], 3), None)
	def test_add_user(self):
		# ouverture/initialisation de la base de donnee 
		try:
			os.remove('test.db')
		except:
			pass
		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")
		
		key = "a" * 128
		# TEST OK
		res = funcs.add_user('Clement', 'Password!1', key, key, key, key)
		self.assertEqual(res, 'Clement')
		c.execute("SELECT * FROM users WHERE username='Clement'")
		rows = c.fetchall()
		for row in rows:
			self.assertEqual(row['username'], 'Clement')
			self.assertEqual(row['password'], 'Password!1')
			self.assertEqual(row['spublickey'], key)

		conn.commit()
		conn.close()

		# TEST UNIQUE
		key = "b" * 128
		res = funcs.add_user('Clement', 'HUhdeu#heufuq!8', key, key, key, key)
		self.assertEqual(res, None)

		# TEST PASSWORD
		res = funcs.add_user('toto', '', key, key, key, key)
		self.assertEqual(res, None)
		res = funcs.add_user('toto', 'abfeokzdffujfe', key, key, key, key)
		self.assertEqual(res, None)
		res = funcs.add_user('toto', 'abfeokz!dffujfe', key, key, key, key)
		self.assertEqual(res, None)
		res = funcs.add_user('toto', 'abf9eokz!dffujfe', key, key, key, key)
		self.assertEqual(res, None)
		res = funcs.add_user('toto', '!#^~~~!!()89(((())', key, key, key, key)
		self.assertEqual(res, None)

		# TEST TAILLE KEY
		key = "b" * 127
		res = funcs.add_user('toto', 'HUhdeu#heufuq!8', key, key, key, key)
		self.assertEqual(res, None)
		key = "b" * 324
		res = funcs.add_user('toto', 'HUhdeu#heufuq!8', key, key, key, key)
		self.assertEqual(res, None)
	
	def test_login(self):
		# ouverture/initialisation de la base de donnee 
		try:
			os.remove('test.db')
		except:
			pass
		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")
		conn.commit()
		conn.close()

		key = "b" * 128
		funcs.add_user('Clement', 'Password!1', key, key, key, key)
		funcs.add_user('Julie', 'Swordpass!1', key, key, key, key)
		self.assertEqual(funcs.login('Clement', 'Password!1'), True)
		self.assertEqual(funcs.login('Clement', 'NotPassword'), False)
		self.assertEqual(funcs.login('Clement', 'Swordpass!1'), False)
		self.assertEqual(funcs.login('Julie', 'Swordpass!1'), True)
		self.assertEqual(funcs.login('Julie', 'Swordpass!'), False)

	def test_get_keys(self):
		try:
			os.remove('test.db')
		except:
			pass
		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")
		conn.commit()
		conn.close()

		key1 = "cgtCQ94Nxf0qz4md3oxScISAU4R14PADIzYzqXL6Z2lud7tq7Ptz78GtDB54z1cZoeNENpiNwn8PhI3E5eNEDE0zS5ebQ8tZK57sMh0tZJg5u836A2wUXSylU6i6pq3L"
		key2 = "HPRu7erX3L2RJ6uLS967t870eS7NnMdYSwmkZpGLCH20RD7IiKN4St3e2RES9cxmav7msCz3lEJs3zRth2lAHI8hCVBtk0OJ06y9a76gk39NF2Y4iKdMnE0ofx3L0XxA"
		key3 = "75vN85a29NtoCiXve57ACvjsf354Ve3W2ew9PDJwG6tj8byjcn3ZtGB1NurmKVElqH8GTGrhSlvbcE7obgfVHMtIowh3k9mPboLBu3E8v2CVQYVrkCD014ThX9rCn9TL"
		key4 = "LJ325iV2IO52n0dCxfohO9wCUKP8D8gnvb30ozYZiaav8Z10MLDDn7kT3SttiCeWn229hkI1HZkqQki20dg1MeaCu5CLqj5eSEjqimcd9yEIR9Pa2Jja3hTZXm4F3y8u"
		funcs.add_user('Clement', 'Password!1', key1, key2, key3, key4)
		keys = funcs.get_keys("Clement")
		self.assertEqual(keys["spublickey"], key1)
		self.assertEqual(keys["sprivatekey"], key2)
		self.assertEqual(keys["epublickey"], key3)
		self.assertEqual(keys["eprivatekey"], key4)
	
	def test_is_db_corrupted(self):
		try:
			os.remove('test.db')
		except:
			pass
		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")

		self.assertEqual(funcs.is_db_corrupted(), False)

		key = "LJ325iV2IO52n0dCxfohO9wCUKP8D8gnvb30ozYZiaav8Z10MLDDn7kT3SttiCeWn229hkI1HZkqQki20dg1MeaCu5CLqj5eSEjqimcd9yEIR9Pa2Jja3hTZXm4F3y8u"
		c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", ("Clement", "Password!1", key, key, key, key))
		conn.commit()
		conn.close()
		self.assertEqual(funcs.is_db_corrupted(), False)

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		key = "LJ325iV2IO52n"
		c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", ("Clement", "Password!1", key, key, key, key))
		conn.commit()
		conn.close()
		self.assertEqual(funcs.is_db_corrupted(), True)

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("DROP TABLE users")
		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")
		key = "LJ325iV2IO52n0dCxfohO9wCUKP8D8gnvb30ozYZiaav8Z10MLDDn7kT3SttiCeWn229hkI1HZkqQki20dg1MeaCu5CLqj5eSEjqimcd9yEIR9Pa2Jja3hTZXm4F3y8u"
		c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", ("Clement", "Password", key, key, key, key))
		conn.commit()
		conn.close()
		self.assertEqual(funcs.is_db_corrupted(), True)

		conn = sqlite3.connect('test.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("DROP TABLE users")
		c.execute("CREATE TABLE users (id INTEGER primary key autoincrement, username TEXT NOT NULL, password TEXT NOT NULL, spublickey TEXT NOT NULL, sprivatekey TEXT NOT NULL, epublickey TEXT NOT NULL, eprivatekey TEXT NOT NULL)")
		key = "LJ325iV2IO52n0dCxfohO9wCUKP8D8gnvb30ozYZiaav8Z10MLDDn7kT3SttiCeWn229hkI1HZkqQki20dg1MeaCu5CLqj5eSEjqimcd9yEIR9Pa2Jja3hTZXm4F3y8u"
		c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", ("Clement", "Password!1", key, key, key, key))
		c.execute("INSERT INTO users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES(?,?,?,?,?,?)", ("Clement", "Password!2", key, key, key, key))
		conn.commit()
		conn.close()
		self.assertEqual(funcs.is_db_corrupted(), True)


if __name__ == '__main__':
	unittest.main()
