#!/usr/bon/python3
''' Unit Test for calculator liberary'''

import calculator

class TestCalculator:
	
	def test_addition(self):
		assert(4)==calculator.add(2,2)
	
	def test_substraction(self):
		assert(6)==calculator.substract(12,6)


