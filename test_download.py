# This file tests download.py

import unittest
import os
from download import get_data,delete_data

class TestDownload(unittest.TestCase):
	def testLocalPresent(self):
		result = os.path.isfile('data.txt')
		self.assertTrue(result)


	def testLocalNotPresent(self):
		flag = os.path.isfile('4xy5-26gy.csv')
		self.assertFalse(flag)
		get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
		flag = os.path.isfile('4xy5-26gy.csv')
		self.assertTrue(flag)
		os.remove('4xy5-26gy.csv')

	def testUrlFail(self):
		result = get_data('https://data.stle.v/resource/4xy.csv')
		
		self.assertFalse(result)



if __name__ == '__main__':
	unittest.main()