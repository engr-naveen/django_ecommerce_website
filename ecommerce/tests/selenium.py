import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# fixture are small functions that we attach to tests befire the test in run
# scope allows us to share the function between funtion, class, modules, packages or seesions
@pytest.fixture(scope="function")
def chrome_browser_instance(request):
    
    """
    Provie a selenium webdriver instance
    """
    # To run in background
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    bowser = webdriver.Chrome(options=options)

    # # To run in foreground
    # bowser = webdriver.Chrome()

    bowser.maximize_window()
    yield bowser
    bowser.close()