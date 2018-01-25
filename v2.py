import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Users/uguryildirim/PycharmProjects/selenium/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://wwwv.site/')
time.sleep(2) # Let the user actually see something!

#
# assert "Python" in driver.title
driver.find_element_by_id("username").send_keys('test')
driver.find_element_by_id("password").send_keys('123456Uy')
driver.find_element_by_name("button").click()
time.sleep(2) # Let the user actually see something!

# ee = driver.find_elements_by_css_selector("a[onlick*=javascript:doarea(2)]")
driver.find_element_by_xpath('//input[@value="START WATCHING PAYED ADS"]').click()


# elem.clear()
# elem.send_keys("pycon")
# time.sleep(1) # Let the user actually see something!
#
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# time.sleep(1) # Let the user actually see something!
#
# driver.close()