from ftplib import print_line

import pytest


@pytest.fixture(scope = "function")
def jerry():

    print("qw")
    yield

    print("tom")


@pytest.mark.demo1
def test_fx(jerry):

    print("ddd")
