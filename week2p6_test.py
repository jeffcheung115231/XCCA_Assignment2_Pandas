import pytest
from week2 import *
import pandas as pd



def test6():
	ans = extractReview().astype('int64')
	lst=[133,30,43,39,57,33,25,37,32,37]
	ind =[0,1,2,3,4,5,6,7,8,9]
	b = pd.Series(lst, index= ind)
	assert b.equals(ans)
