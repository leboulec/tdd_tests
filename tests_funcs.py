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


if __name__ == '__main__':
	unittest.main()


#git push -u origin moyenne
#git checkout main
#git merge moyenne
