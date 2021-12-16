import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_moyenne_int(self):
		self.assertEqual(funcs.max_int(0,2),1)
		self.assertEqual(funcs.max_int(-1,-5),-3)
		self.assertEqual(funcs.max_int(-1,3),1)
		self.assertEqual(funcs.max_int(0,0),0)

if __name__ == '__main__':
	unittest.main()


#git push -u origin moyenne
#git checkout main
#git merge moyenne
