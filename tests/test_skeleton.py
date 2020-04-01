# -*- coding: utf-8 -*-

import pytest
from pytemplate.skeleton import fib

__author__ = "martin.tripiana@gmail.com"
__copyright__ = "martin.tripiana@gmail.com"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
