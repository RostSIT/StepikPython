import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


f = open('textAjaxSystems_JuniorPythonDeveloperInTestApps.txt')
n = open('nameRecruiter.txt')
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(10)
browser.set_page_load_timeout(10)
wait = WebDriverWait(browser, 10)
browser.get('https://djinni.co/jobs/279686-junior-python-developer-in-test-apps-/')

logIn = browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[5]/a[1]')
browser.execute_script("return arguments[0].scrollIntoView(true);", logIn)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[5]/a[1]')))
logIn.click()

inputMail = browser.find_element_by_xpath('//*[@id="email"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", inputMail)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
inputMail.send_keys('kyivmycity@i.ua')

inputPassword = browser.find_element_by_xpath('//*[@id="password"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", inputPassword)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
inputPassword.send_keys('123Hjcn')

buttonLogIn = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/form/div[1]/div[3]/button')
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonLogIn)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div[2]/form/div[1]/div[3]/button')))
buttonLogIn.click()

browser.maximize_window()

browser.execute_script("window.scrollBy(0, -100);")

buttonRespond = browser.find_element_by_class_name('btn.btn-primary.btn-lg.js-inbox-toggle-reply-form')
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonRespond)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.btn-lg.js-inbox-toggle-reply-form')))
browser.execute_script("window.scrollBy(0, -100);")
buttonRespond.click()

inputRespondToTheVacancy = browser.find_element_by_xpath('//*[@id="message"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", inputRespondToTheVacancy)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="message"]')))
inputRespondToTheVacancy.send_keys('Ms ' + n.read() + ',' + '\n\n' + f.read())

checkboxSaveMessageAsTemplate = browser.find_element_by_id("save_answer_templates")
checkboxSaveMessageAsTemplate.click()

inputTheNameOfTheTemplate = browser.find_element_by_name('template_name')
# browser.execute_script("return arguments[0].scrollIntoView(true);", inputTheNameOfTheTemplate)
wait.until(EC.element_to_be_clickable((By.NAME, 'template_name')))
time.sleep(1)
inputTheNameOfTheTemplate.send_keys('Сопроводительное письмо')

inputVC = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[6]/div/form/div['
                                        '4]/table/tbody/tr/td[1]/input')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'Ruslan_Streltsov_QA_Automation.pdf')           # добавляем к этому пути имя файла
inputVC.send_keys(file_path)

buttonOpenContactsAndStartCommunication = browser.find_element_by_id('job_apply')
#browser.execute_script("return arguments[0].scrollIntoView(true);", buttonCVInput)
wait.until(EC.element_to_be_clickable((By.ID, 'job_apply')))
# buttonOpenContactsAndStartCommunication.click()

time.sleep(20)
browser.quit()


