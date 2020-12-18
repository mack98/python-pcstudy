from selenium import webdriver

url = "https://www.baidu.com"

driver = webdriver.Chrome()

driver.get(url)

input_element = driver.find_element_by_id("kw")
click_element = driver.find_element_by_id("su")
input_element.send_keys("黑洞")
click_element.click()