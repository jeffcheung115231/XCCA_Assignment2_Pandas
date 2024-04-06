import pytest
from week2 import *
import pandas as pd


def test2():
    x = pd.Series(['Cheap','Very Expensive','Very Expensive','Cheap','Not Cheap','Expensive','Cheap','Expensive','Not Cheap','Not Cheap'])
    assert x.equals(makeCategory())
