from time import sleep
from selenium.webdriver import Chrome


driver = Chrome(r"/Users/dell/Desktop/Training/chromedriver")
sleep(3)
driver.get("http://demowebshop.tricentis.com/")

driver.close()