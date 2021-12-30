import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_max_int(self):
		self.assertEqual(funcs.max_int(0,2),2)
		self.assertEqual(funcs.max_int(-1,-5),-1)
		self.assertEqual(funcs.max_int(-1,2),2)
		self.assertEqual(funcs.max_int(0,0),0)

	def test_moyenne_int(self):
		self.assertEqual(funcs.moyenne_int([1, 5, 3, 2, 8]), 3.8)
		self.assertEqual(funcs.moyenne_int([-1, -1, -10]), -4)
		self.assertEqual(funcs.moyenne_int([10, 10]), 10)
		self.assertEqual(funcs.moyenne_int([3, -3, 8, -8]), 0)

if __name__ == '__main__':
	unittest.main()


#git push -u origin moyenne
#git checkout main
#git merge moyenne
