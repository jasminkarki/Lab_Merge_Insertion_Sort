import unittest
from insertionsort import insertion_sort


class SearchTestCase(unittest.TestCase):
	
	def test_insertion_sort(self):
		values=[5,2,4,1,3]
		insertion_sort(values)
		required=[1,2,3,4,5]
		self.assertListEqual(values,required)

if __name__=="__main__":
	unittest.main()