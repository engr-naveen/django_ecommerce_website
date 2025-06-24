import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep

# from selenium.webdriver.chrome.service import Service

# fixture are small functions that we attach to tests befire the test in run
# scope allows us to share the function between funtion, class, module, package or session
@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    
    """
    Provie a selenium webdriver instance
    """
    # To run in background
    chrome_options = webdriver.ChromeOptions()
    
    # To hide the window
    chrome_options.add_argument('--headless')
    
    bowser = webdriver.Chrome(options=chrome_options)

    # # To run in foreground
    # bowser = webdriver.Chrome()

    bowser.maximize_window()
    yield bowser
    # sleep(60)
    bowser.close()