
import pytest

@pytest.mark.usefixtures("Dataload")
class TestSuit2:
    def test_profile(self,Dataload):
        print("\nTest Profile")
        print(Dataload[0])
        print(Dataload[1])