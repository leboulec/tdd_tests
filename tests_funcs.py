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


if __name__ == '__main__':
	unittest.main()
