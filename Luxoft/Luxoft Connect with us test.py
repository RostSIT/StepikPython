from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.set_page_load_timeout(5)
wait = WebDriverWait(browser, 5)
browser.get('https://career.luxoft.com/locations/ukraine/lux-campus/')

buttonAceept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]')))
buttonAceept.click()

buttonLuxoftGroup = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CONTACT_CONSENT_COMPULSORY"]/label/strong[2]/a')))
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonLuxoftGroup)
buttonLuxoftGroup.click()

buttonLuxoftGroup = browser.find_element_by_xpath('//*[@id="CONTACT_CONSENT_COMPULSORY"]/label/strong[2]/a')
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonLuxoftGroup)
time.sleep(1)

privacyPolicy = ui.WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-1"]/div/div/form/div[11]/div[2]/div/a[1]')))
browser.execute_script("return arguments[0].scrollIntoView(true);", privacyPolicy)
privacyPolicy.click()

shoesize = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CONTACT_CONSENT_OPTIONAL_B2B"]/div/label/span')))
shoesize.click()


shoesize1 = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))
shoesize1.click()


shoesize2 = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]')))
shoesize2.click()


shoesize3 = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[3]')))
shoesize3.click()


shoesize4 = ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')))
shoesize4.click()

time.sleep(1)
checkboxNotARobot = browser.find_element_by_xpath('//*[@id="CONTACT_CONSENT_OPTIONAL_B2B"]/div/label/span')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkboxNotARobot)
time.sleep(3)
checkboxNotARobot.click()

button = browser.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyButtonAccept"]')
button.click()

checkbox = browser.find_element_by_xpath('//*[@id="LGK_CONSENT_OPTIONAL"]/div[1]/div/label/span[1]')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
time.sleep(1)
checkbox.click()

button = browser.find_element_by_xpath('//*[@id="submit-button"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
#button.click()

time.sleep(10)

browser.quit()

