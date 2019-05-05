import unittest
from mergesort import merge_sort,merge


class SearchTestCase(unittest.TestCase):
	
	def test_merge_sort(self):
		values=[5,2,4,1,3]
		merge_sort(values)
		required=[1,2,3,4,5]
		self.assertListEqual(values,required)

if __name__=="__main__":
	unittest.main()