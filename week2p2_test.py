import pytest
from week2 import *
import pandas as pd

df = pd.read_csv('data/openrice.csv', index_col=[0])

def test1():
	assert df.equals(load())
