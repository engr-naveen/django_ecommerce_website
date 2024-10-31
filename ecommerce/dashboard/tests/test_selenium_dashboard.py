import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_cerate_admin_user(cerate_admin_user):
    assert cerate_admin_user.__str__() == "admin"  


# pytest markup to mark all selenium tests
@pytest.mark.selenium
def test_dashboad_admin_login(live_server,cerate_admin_user,chrome_browser_instance):
    
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url,"/admin/login")))
    
    user_name = browser.find_element(By.NAME,"username")
    user_password = browser.find_element(By.NAME,"password")
    submit = browser.find_element(By.XPATH,'//input[@value="Log in"]')

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send_keys(Keys.RETURN)

    # time.sleep(20)

    assert "Site administration" in browser.page_source