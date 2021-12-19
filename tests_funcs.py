import funcs
import unittest

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

if __name__ == '__main__':
	unittest.main()
