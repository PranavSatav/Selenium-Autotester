from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://x7propranav.000webhostapp.com/auto/")

time.sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("123")
time.sleep(2)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("abc")
time.sleep(2)
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
time.sleep(2)
login_button = driver.find_element(By.XPATH, "/html/body/button")
login_button.click()




time.sleep(5)



