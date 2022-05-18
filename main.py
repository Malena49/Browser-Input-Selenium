from mimetypes import init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('http://demo.seleniumeasy.com/')
driver.implicitly_wait(8)
#fermer popup
try:
    popup = driver.find_element(by=By.CLASS_NAME, value="at-cm-no-button")
    popup.click()
except:
    print("pas de popup, ignorer cette étape")
#diriger vers la formulaire
Input_Forms = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Input Forms")
Input_Forms.click()
Simple_Form_Demo = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Simple Form Demo")
Simple_Form_Demo.click()
#tester des inputs
sum1 = driver.find_element(by=By.ID, value="sum1")
sum2 = driver.find_element(by=By.ID, value="sum2")
sum1.send_keys(Keys.NUMPAD4, Keys.NUMPAD7)
sum2.send_keys(Keys.NUMPAD9)
cacul_total = driver.find_element(by=By.CSS_SELECTOR, value='button[onclick="return total()"]')
cacul_total.click()
resultat_total = driver.find_element(by=By.ID, value= "displayvalue").get_attribute('innerHTML').strip()
if int(resultat_total) != 56:
   raise Exception("Le cacul n'est pas correct.")
driver.quit()