# -*- coding: UTF-8 -*-

import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


current_script_name = os.path.basename(__file__)

with open(current_script_name, "r") as myfile:
    current_script_text = myfile.read()

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

#time.sleep(1)
#button = wait.until(
#    EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]')))
#button.click()

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
inputMail.send_keys('Добрый день. Прошу уточнить информацию, на какой стадии находиться отбор на курс QA Automation '
                    'стартующий первого октября 2021. Я подал заявку на участие 06 августа. Прошу рассмотреть мою '
                    'кандидатуру с положительной стороны. Заранее благодарю за участие.\n\n P.S. Ниже по тексту код '
                    'автозаполнения формы и отправки письма.\n\n' + current_script_text)

checkboxAgreement = browser.find_element_by_xpath('//*[@id="CONTACT_CONSENT_OPTIONAL_B2E"]/div/label/span')
browser.execute_script("return arguments[0].scrollIntoView(true);", checkboxAgreement)
time.sleep(2)
checkboxAgreement.click()

notARobot = browser.find_element_by_xpath('//*[@id="submit-button"]')
action = ActionChains(browser)
browser.maximize_window()

action.move_to_element_with_offset(notARobot, -500, 0).click().perform()

#time.sleep(65)  # для выбора фото вручную

# checkboxNotARobot = browser.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
# browser.execute_script("return arguments[0].scrollIntoView(true);", checkboxNotARobot)
# checkboxNotARobot.click()

# agreeAndSendButton = browser.find_element_by_xpath('//*[@id="submit-text-button"]')
# browser.execute_script("return arguments[0].scrollIntoView(true);", agreeAndSendButton)
# agreeAndSendButton.click()
browser.minimize_window()
agreeAndSendButton = browser.find_element_by_xpath('//*[@id="submit-text-button"]')
time.sleep(90)
browser.execute_script("return arguments[0].scrollIntoView(true);", agreeAndSendButton)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-text-button"]')))
time.sleep(2)
agreeAndSendButton.click()

# selectMessageCategory = Select(browser.find_element_by_xpath('//*[@id="form_text_936"]'))
# #browser.execute_script("return arguments[0].scrollIntoView(true);", selectMessageCategory)
# wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-text-button"]')))
# time.sleep(2)
# selectMessageCategory.select_by_visible_text('Career')
#
# inputMail = browser.find_element_by_xpath('//*[@id="form_CONTACT_TEXT"]')
#
# time.sleep(3)
# inputMail.send_keys('Добрый день. Прошу уточнить информацию, на какой стадии находиться отбор на курс QA Automation '
#                     'стартующий первого октября 2021. Я подал заявку на участие 06 августа. Прошу рассмотреть мою '
#                     'кандидатуру с положительной стороны. Заранее благодарю за участие.\n\n P.S. Ниже по тексту '
#                     'код автозаполнения формы и отправки письма.\n\n' + '''CV\n
# RUSLAN STRELTSOV
# QA AUTOMATION
#
# P E R S O N A L
# P R O F I L E
# Motivated to get a job in a
# project to be involved in
# creating quality and user-
# friendly software
# applications.
#
# C O N T A C T
# Kiev,
# Ukraine
# streltsovrp@gmail.com
# +38(050)774-61-96
# /ruslan-streltsov
#
# E D U C A T I O N
# Kyiv Economical Institute of
# Management
# Start-IT (training center)
# Stepik (online courses)
# Bachelor in Management
# and administration, 2008
# September
# still training
# Test automation with
# Selenium and Python
#
# S K I L L S
# outstanding knowledge of testing theory and test
# design techniques (pairwise, state-transition etc.)
# clear understanding of Software development life
# cycle, Agile frameworks (Scrum)
# basic knowledge of HTML and CSS, HTTP/HTTPS
# protocols and methods, client-server architecture
# experienced in creating test cases, checklists, bug
# reports
# proficient user of Chrome Dev tools, Trello,
# PyCharm.
#
# W O R K E X P E R I E N C E
# MANUAL QC ENGINEER
# STARTIT TESTING LAB | JUL 2018 - OCT 2018
# Project: Natureal Responsibilities: Creation of bug
# reports, tasks and subtasks in Trello -
# management system; functional, sanity, regression
# and verification testing. UI/UX testing,
# positive/negative testing \n
# Project: Tickerry Responsibilities: Creation of bug
# reports, tasks and subtasks in Trello -
# management system; smoke, functional,
# regression, verification and exploratory testing.
# ''' + current_script_text)
# time.sleep(1)
#
# # agreeAndSendButton = browser.find_element_by_xpath('//*[@id="submit-text-button"]')
# # browser.execute_script("return arguments[0].scrollIntoView(true);", agreeAndSendButton)
# # agreeAndSendButton.click()
#
# agreeAndSendButton = browser.find_element_by_xpath(
#     '//*[@id="submit-text-button"]')
# browser.execute_script("return arguments[0].scrollIntoView(true);", agreeAndSendButton)
# wait.until(EC.element_to_be_clickable((
#     By.XPATH, '//*[@id="submit-text-button"]')))
# time.sleep(1)
# agreeAndSendButton.click()
#
# time.sleep(60)

browser.quit()

# P.S. Ниже по тексту '
#                     'код автозаполнения формы и отправки письма.\n\n' + '''CV\n
# RUSLAN STRELTSOV
# QA AUTOMATION
#
# P E R S O N A L
# P R O F I L E
# Motivated to get a job in a
# project to be involved in
# creating quality and user-
# friendly software
# applications.
#
# C O N T A C T
# Kiev,
# Ukraine
# streltsovrp@gmail.com
# +38(050)774-61-96
# /ruslan-streltsov
#
# E D U C A T I O N
# Kyiv Economical Institute of
# Management
# Start-IT (training center)
# Stepik (online courses)
# Bachelor in Management
# and administration, 2008
# September
# still training
# Test automation with
# Selenium and Python
#
# S K I L L S
# outstanding knowledge of testing theory and test
# design techniques (pairwise, state-transition etc.)
# clear understanding of Software development life
# cycle, Agile frameworks (Scrum)
# basic knowledge of HTML and CSS, HTTP/HTTPS
# protocols and methods, client-server architecture
# experienced in creating test cases, checklists, bug
# reports
# proficient user of Chrome Dev tools, Trello,
# PyCharm.
#
# W O R K E X P E R I E N C E
# MANUAL QC ENGINEER
# STARTIT TESTING LAB | JUL 2018 - OCT 2018
# Project: Natureal Responsibilities: Creation of bug
# reports, tasks and subtasks in Trello -
# management system; functional, sanity, regression
# and verification testing. UI/UX testing,
# positive/negative testing \n
# Project: Tickerry Responsibilities: Creation of bug
# reports, tasks and subtasks in Trello -
# management system; smoke, functional,
# regression, verification and exploratory testing.
# ''' + current_script_text)
# # time.sleep(1)
