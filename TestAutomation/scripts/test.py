from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://localhost:3000")
#assert "Python" in driver.title

time.sleep(15)
#finds the cookie button
elem1 = driver.find_element_by_class_name("button-continue-with-cookies")
#assert elem1.text == "Okay, let's go!"

#finds the no cookie button
elem2 = driver.find_element_by_class_name("button-continue-without-cookies")
elem2.click()
#assert str(elem2.text) not in driver.page_source

#turns location button off
elem3 = driver.find_element_by_class_name("leaflet-bar-part")
elemDot = driver.find_element_by_class_name("leaflet-interactive")
elem3.click()
#assert str(elemDot) not in driver.page_source

#turns loction button on 
elem4 = driver.find_element_by_class_name("leaflet-bar-part")
elemDot2 = driver.find_element_by_class_name("leaflet-interactive")
elem4.click()
#assert str(elemDot) in driver.page_source


elem5 = driver.find_element_by_class_name("search-input")
elem5.send_keys("Halls Chophouse")
elem5.send_keys(Keys.RETURN)
assert "King Street, 29424" in driver.page_source

time.sleep(15)
#driver.close()

