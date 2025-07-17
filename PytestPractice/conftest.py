import pytest

@pytest.fixture(scope="class")
def setup():
    print("This will print first")

    yield
    print("\nThis will print second")


@pytest.fixture(scope="class")
def Dataload():
    print("Data is being loaded")
    return ["Adam", "Warlock", "Password123"]

@pytest.fixture(params=[("Chrome","Adam","warlock"), ("Firefox","Thor"), ("Safari","Hela")])
def crossBrowser(request):
    return request.param
