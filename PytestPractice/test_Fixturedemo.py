import pytest


def test_Fixtureconfig(setup):
    print("Good Morning")
    a=2
    b=4
    assert a==b,"Not equal"
