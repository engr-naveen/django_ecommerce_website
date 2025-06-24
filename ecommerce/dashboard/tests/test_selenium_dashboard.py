import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# @pytest.mark.selenium
# def test_cerate_admin_user(cerate_admin_user,transactional_db):
#     assert cerate_admin_user.__str__() == "admin"  


# pytest markup to mark all selenium tests
@pytest.mark.selenium
def test_dashboad_admin_login(live_server,db_fixture_setup,chrome_browser_instance):
    
    delay = 1 #sec

    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url,"/admin/login/")))
    time.sleep(delay)

    user_name = browser.find_element(By.NAME,"username")
    user_password = browser.find_element(By.NAME,"password")
    log_in_submit = browser.find_element(By.XPATH,'//input[@value="Log in"]')
    
    user_name.send_keys("admin")
    user_password.send_keys("password")
    log_in_submit.send_keys(Keys.RETURN)
    time.sleep(delay)
    
    # assert cerate_admin_user.__str__() == "admin" 
    assert "Site administration" in browser.page_source

    log_out_submit = browser.find_element(By.XPATH,'//button[contains(.,"Log out")]')
    log_out_submit.send_keys(Keys.RETURN)
    time.sleep(delay)
    
    assert "Logged out" in browser.page_source
