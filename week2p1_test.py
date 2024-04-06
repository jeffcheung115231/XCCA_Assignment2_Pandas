import pytest
from week2 import makeDataFrame
import pandas as pd

def testex1():
	result = makeDataFrame({'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']})
	print(f"result {result}")
	d = {'col_1':[3, 2, 1, 0], 'col_2':['a', 'b', 'c', 'd']}
	assert pd.DataFrame(data=d).equals(result)

def testex2():
	result = makeDataFrame( {'Amy':[1], 'Bob':[2], 'Cat':[3], 'David':[5]})
	d = { 'Amy':[1], 'Bob':[2], 'Cat':[3], 'David':[5]}
	assert pd.DataFrame(data=d).equals(result)

def testex3():
	result = makeDataFrame( {'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]})
	d = { 'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]}
	assert pd.DataFrame(data=d).equals(result)
