from time import sleep
import driver as driver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome(r"/Users/dell/Desktop/Training/chromedriver")
sleep(3)
driver.get("https://workflow.cchaxcess.com/xcmv2/account/PartialLogin?ReturnUrl=%2Fxcmv2%2F")
sleep(1)
driver.find_element(By.ID, "Email").send_keys("Subramanya@mail.com")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
# driver.close()
sleep(2)
driver.find_element(By.ID, "Password").send_keys("Password")
driver.find_element(By.CLASS_NAME, "login-btn").click()
sleep(2)

driver.implicitly_wait(10)
driver.close()
