from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/adelas93/PycharmProjects/test/drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.momox.fr/")
driver.minimize_window()
driver.refresh()
driver.find_element_by_class_name("searchbox-input").send_keys("9782729894931")
time.sleep(4)
driver.find_element_by_id("buttonMediaSearchSubmit").click()
time.sleep(4)
prix = driver.find_element_by_class_name("searchresult-price").text
titre = driver.find_element_by_class_name("product-title").text
driver.quit()

print("helloworld")
print (prix)
print (titre)
