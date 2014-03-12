#!/usr/bin/python3
import unittest
from generator import Generator

class TestGenerator(unittest.TestCase):
	def testOpenSqlConnection(self):
		self.assertTrue(Generator())

	def testRead(self):
		self.assertIsNotNone(Generator().read())

if __name__ == "__main__":
	unittest.main()
