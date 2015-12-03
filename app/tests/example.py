# NAME:
# PURPOSE:
# COMMENTS:

import pytest


def func_to_test(a, b):
    return a+b


@pytest.fixture
def setup_func_to_test():
    return func_to_test(1,2)



def test_something(setup_func_to_test):
    assert setup_func_to_test == 3



##test with py.test example.py
