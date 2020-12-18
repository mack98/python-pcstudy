from selenium import webdriver

url = "https://www.baidu.com"

driver = webdriver.Chrome()

driver.get(url)

input_element = driver.find_element_by_id()
click_element = driver.find_element_by_id()

click_element.click()