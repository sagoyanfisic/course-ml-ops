import imp
import sys
from src import math_func
import pytest


def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9