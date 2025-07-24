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

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="Select the browser you wish to use"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,  # Disable password manager
        "profile.password_manager_enabled": False  # Disable password-saving prompt
    })
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument("--disable-notifications") # Block notification popups
    # options.add_argument("--disable-popup-blocking") # Avoid pop-up blocks
    # options.add_argument("--log-level=3")
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome(options=options)
    elif browser_name=="firefox":
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(4)
    yield driver
    driver.quit()


