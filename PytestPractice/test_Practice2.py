import pytest


# def test_secondProgram():
#     msg="Hello"
#     assert msg=="Hello" ,"Strings does not match"
#
# @pytest.mark.Smoke
# def test_thirdCreditcard():
#     a=2
#     b=6
#     assert a==b,"Test failed because a and b are not equal"


def test_Crossbrowser(crossBrowser):
    print(crossBrowser[1])