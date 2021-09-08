import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

'''current_script_name = os.path.basename(__file__)

with open(current_script_name, "r") as myfile: current_script_text = myfile.read()  # Закомментировал, по причине 
того, что текстовое поле странички не принимает сообщения объемом позволяющим передать код автозаполнения и отправки 
письма. Использовал ссылку на гит '''

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(100)
browser.set_page_load_timeout(100)
wait = WebDriverWait(browser, 100)
browser.get('https://career.luxoft.com/locations/ukraine/lux-campus/')

buttonAccept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]')))
time.sleep(2)
buttonAccept.click()

buttonConnectWithUs = browser.find_element_by_xpath(
    '//*[@id="contact-us"]/section[1]/div/div/div[1]/div/div[2]/div/div/a')
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonConnectWithUs)
wait.until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="contact-us"]/section[1]/div/div/div[1]/div/div[2]/div/div/a')))
time.sleep(1)
buttonConnectWithUs.click()

inputFirstName = browser.find_element_by_xpath('//*[@id="form_CONTACT_NAME"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", inputFirstName)
time.sleep(1)
inputFirstName.send_keys('Руслан')

inputLastName = browser.find_element_by_xpath('//*[@id="form_CONTACT_LAST_NAME"]')
inputLastName.send_keys('Стрельцов')

inputCompany = browser.find_element_by_xpath('//*[@id="form_CONTACT_COMPANY"]')
inputCompany.send_keys('None')

inputEmail = browser.find_element_by_xpath('//*[@id="form_CONTACT_CONTACT"]')
inputEmail.send_keys('streltsovrp@gmail.com')

inputPhone = browser.find_element_by_xpath('//*[@id="form_CONTACT_PHONE"]')
inputPhone.send_keys('+38(050)-774-61-91')

selectMessageCategory = Select(browser.find_element_by_xpath('//*[@id="form_text_936"]'))
selectMessageCategory.select_by_visible_text('Career')

inputSpecialization = browser.find_element_by_xpath('//*[@id="form_CONTACT_SPECIALIZATION"]')
inputSpecialization.send_keys('QA Automation')

inputMail = browser.find_element_by_xpath('//*[@id="form_CONTACT_TEXT"]')
time.sleep(1)
inputMail.send_keys('Доброго времени суток. Пишу письмо №5 в надежде на ответ. Понимая, что поток обращений '
                    'просто несоизмерим с возможностью их обработать, решил отправлять по нескольку писем в день, '
                    'для увеличения шансов получить ответ - на какой стадии находиться отбор на курс QA Automation '
                    'стартующий первого октября 2021. Я подал заявку на участие 06 августа. Прошу рассмотреть мою '
                    'кандидатуру с положительной стороны. Заранее благодарю за участие.\n\n P.S. Ниже по тексту '
                    'ссылка на код автозаполнения формы и отправки '
                    'письма.\n\nhttps://github.com/RostSIT/StepikPython/blob/main/Luxoft/LuxoftClear.py')

checkboxAgreement = browser.find_element_by_xpath('//*[@id="CONTACT_CONSENT_OPTIONAL_B2E"]/div/label/span')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkboxAgreement)
time.sleep(2)
checkboxAgreement.click()

notARobot = browser.find_element_by_xpath('//*[@id="submit-button"]')
action = ActionChains(browser)
browser.maximize_window()

action.move_to_element_with_offset(notARobot, -500, 0).click().perform()

#  browser.minimize_window()
agreeAndSendButton = browser.find_element_by_xpath('//*[@id="submit-text-button"]')
time.sleep(90)  # Для прохождения фото теста от гугла
browser.execute_script("return arguments[0].scrollIntoView(true);", agreeAndSendButton)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-text-button"]')))
time.sleep(2)
agreeAndSendButton.click()


