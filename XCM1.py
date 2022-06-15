from time import sleep
import driver as driver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome(r"/Users/dell/Desktop/Training/chromedriver")
sleep(3)
driver.get("https://workflow.cchaxcess.com/xcmv2/account/PartialLogin?ReturnUrl=%2Fxcmv2%2F")
sleep(1)
driver.maximize_window()
# Assert the login page
a = driver.find_element(By.XPATH, "//h1[@class='text-primary']").text
if a == ("CCH AxcessTM"):
    print("Login page rendered")

driver.find_element(By.ID, "Email").send_keys("Subramanya.madhyastha@gmail.com")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
# driver.close()
sleep(2)
driver.find_element(By.ID, "Password").send_keys("date****")
sleep(1)
driver.find_element(By.CLASS_NAME, "login-btn").click()
sleep(5)
handles = driver.window_handles
for items in handles:
    print(items)
    driver.switch_to.window(handles[0])
    sleep(5)
driver.find_element(By.XPATH,"//button[@id='skipNagScreen']").click()
driver.close()
