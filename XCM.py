from time import sleep
from selenium.webdriver import Chrome

driver = Chrome(r"/Users/dell/Desktop/Training/chromedriver")
sleep(3)
driver.get("https://workflow.cchaxcess.com/xcmv2/account/PartialLogin?ReturnUrl=%2Fxcmv2%2F")
sleep(1)
driver.find_element_by_id("Email").send_keys("Subramanya@mail.com")
# driver.close()
driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
sleep(2)
driver.find_element_by_id("Password").send_keys("XCM")
driver.find_element_by_class_name("login-btn").click()
