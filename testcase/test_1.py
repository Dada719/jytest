from pickletools import markobject

import pytest


def test_1():
    if 1:
        print(1)
    elif 0:
        print(0)
@pytest.mark.demo
@pytest.mark.skipif("0")
@pytest.mark.xfail
class Test_1:

    def test_1(self):
        assert 1==1
        //add


