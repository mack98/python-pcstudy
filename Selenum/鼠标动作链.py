from selenium import webdriver
from selenium.webdriver import ActionChains


url = "https://www.runoob.com/try/try-cdnjs.php?filename=jqueryui-example-droppable"

driver = webdriver.Chrome()
driver.get(url)
driver.switch_to.frame("iframeResult")

#要拖动的元素  html5元素疑似不能生效
drag = driver.find_element_by_id("draggable")
#拖放地点
drop = driver.find_element_by_id("droppable")
#实例化 鼠标动作链
action = ActionChains(driver)
#定义动作
action.drag_and_drop(drag,drop).perform()
#执行动作
action.perform()
#
