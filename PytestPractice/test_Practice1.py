#any pyest file should start with test_
#pytest method names should start
#any code should be wrapped in method only
#-k for specific test -v info about metadata -s logs in out put
#@pytest.mark.Smoke for marking it for smoke or regression
#fixtures are used for setup and tear down for test cases conftest file to generalize fixture and make it available to
#all test cases


import pytest
@pytest.mark.usefixtures("setup")
class TestClass1:

    def test_firstProgramfixture(self):
        print("1 programming")

    def test_secondProgramfixture(self):
        print("2 programming")

    def test_thirdProgramfixture(self):
        print("3 programming")