import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
driver = webdriver.Firefox(executable_path='/Users/uguryildirim/PycharmProjects/selenium/geckodriver')  # Optional argument, if not specified will search path.
driver.get('http://wwwv.site/')
time.sleep(2) # Let the user actually see something!

#
# assert "Python" in driver.title
driver.find_element_by_id("username").send_keys('test')
driver.find_element_by_id("password").send_keys('123456')
driver.find_element_by_name("button").click()
time.sleep(2) # Let the user actually see something!

# ee = driver.find_elements_by_css_selector("a[onlick*=javascript:doarea(2)]")
driver.find_element_by_xpath('//input[@value="START WATCHING PAYED ADS"]').click()
time.sleep(2) # Let the user actually see something!

while True:

    # heading1 = driver.find_element_by_tag_name('img')
    page = BeautifulSoup(driver.page_source)
    # print page
    bhtml = str(page)

    # soup = BeautifulSoup(page.text, "html.parser")
    # form =  soup.findAll('form')
    # rr = open('ee.txt','w')
    # rr.write(str(page))
    # rr.close()
    # bhtml = open("ee.txt", 'r')

    soup = BeautifulSoup(bhtml, "html.parser")

    # form =  soup.findAll('form')

    profilBilgi = soup.find('form', {"name": "mainf"}).findAll('img')

    dizi = []

    for qq in profilBilgi:
        ee = str(qq)
        ee = ee.split(' ')
        ee = ee[2].split('/')
        ee = ee[2].split('.')
        rr = ee[0]
        dizi.append(rr)
    print dizi
    for yaz in dizi:
        ss = driver.find_element_by_name('capcha').send_keys(yaz)
    time.sleep(0.04)
    driver.find_element_by_name('capcha').send_keys(Keys.ENTER)
