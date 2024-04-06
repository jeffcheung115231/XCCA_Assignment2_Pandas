import pytest
from week2 import *
import pandas as pd


def test4():
	lst=[3,7,1,10]
	ind = ['$101-200','$201-400','$51-100','Below $50']
	a = pd.Series(lst, index= ind)
	assert a.equals(totalDislike())
