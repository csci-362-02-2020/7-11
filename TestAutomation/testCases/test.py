from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("localhost:3000")

elem1 = driver.find_element_by_class_name("button-continue-with-cookies")
elem1.click()
elem9 = driver.find_element_by_link_text("Improve this map")
elem9.click()
#print(value)
print(elem9.get_attribute("href"))
print(driver.current_url)

#.startsWith("https://ee.humanitarianresponse.info/single/::WBnyIcbH?returnUrl=https%3A%2F%2Flocalhost%2Fcontribution-thanks%3FuniqueSurveyId%3D4aaecc0b-c8aa-4ec9-bda6-30bdb712ec5d")


driver.quit()
