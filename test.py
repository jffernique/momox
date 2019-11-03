from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/adelas93/PycharmProjects/test/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://alliance-healthcare.magic-bpm.com/bin/Main.php?menu=request&ScreenID=0&_action=11&iCurrentPage=6")
driver.maximize_window()
driver.refresh()
driver.find_element_by_name("sUsername").send_keys("jferniqu")
time.sleep(4)
driver.find_element_by_name("sPassword").send_keys("@delas93")

time.sleep(4)
driver.find_element_by_name("loginButton").click()
time.sleep(4)
# driver.quit()

print("helloworld")
