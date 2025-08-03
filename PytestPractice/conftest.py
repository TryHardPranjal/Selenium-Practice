import os

import pytest
driver=None

@pytest.fixture(params=[("Chrome","Adam","warlock"), ("Firefox","Thor"), ("Safari","Hela")])
def crossBrowser(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome",help="Select the browser you wish to use"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
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

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(4)

    yield driver
    driver.quit()

import os

import os
import pytest
import os
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("browserInstance", None)
        if driver:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "Reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") + ".png"
            abs_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(abs_path)

            # Embed image in report
            extra.append(pytest_html.extras.image(abs_path))
        else:
            print(" No WebDriver instance found to take screenshot.")

    report.extra = extra
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when in ('call', 'setup'):
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # Set up correct path
#             reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Reports'))
#             screenshots_dir = os.path.join(reports_dir, 'screenshots')
#             os.makedirs(screenshots_dir, exist_ok=True)
#
#             # Screenshot filename
#             file_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") + ".png"
#             abs_path = os.path.join(screenshots_dir, file_name)
#             rel_path = f"screenshots/{file_name}"
#
#             print(f"📸 Saving screenshot to: {abs_path}")
#
#             # Get driver from fixture
#             driver = item.funcargs.get("browserInstance", None)
#             if driver:
#                 driver.get_screenshot_as_file(abs_path)
#
#                 # Embed in report
#                 html = f'''
#                 <div style="text-align:right">
#                     <img src="{rel_path}" alt="screenshot"
#                          style="width:304px;height:228px;"
#                          onclick="window.open(this.src)" />
#                 </div>
#                 '''
#                 extra.append(pytest_html.extras.html(html))
#             else:
#                 print("WebDriver not found for screenshot capture.")
#
#         report.extra = extra


def _capture_screenshot(file_name, driver):
    if driver:
        driver.get_screenshot_as_file(file_name)
    else:
        print("Cannot capture screenshot — WebDriver instance not found.")
