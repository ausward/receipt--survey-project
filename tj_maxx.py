from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def inputSurveyCode(code, month, day, year, hour, minute):
    global driver
    service = "D:\Program Files/Chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(service, options=options )
    driver.get(url="https://www.TJMAXXFEEDBACK.COM")

    code_box = driver.find_element(By.NAME, "SurveyNumber")
    code_box.send_keys(str(code))

    month_box = driver.find_element(By.ID, "InputMonth")
    if len(str(month)) == 1:
        month = str(0) + str(month)

    month_box.send_keys(month)

    day_box = driver.find_element(By.ID, "InputDay")
    if len(str(day)) == 1:
        day = str(0) + str(day)

    day_box.send_keys(day)

    year_box = driver.find_element(By.ID, "InputYear")
    year_box.send_keys(year)

    hour_box = driver.find_element(By.ID,"InputHour")
    hour_box.send_keys(hour)

    minute_box = driver.find_element(By.ID, "InputMinute")
    minute_box.send_keys(minute)
    next()

def next():
    next = driver.find_element(By.ID, "NextButton")
    next.send_keys("\n")

def fill_survey():
    q1 = driver.find_element(By.CLASS_NAME, "radioBranded")
    q1.click()
    next()
    q2 = driver.find_element(By.CLASS_NAME, "checkboxBranded")
    q2.click()
    next()
    q3 = driver.find_element(By.CLASS_NAME, "radioBranded")
    nextLink = driver.find_elements(By.ID, "NextButton")
    while len(nextLink) != 0:
        optionButton = driver.find_elements(By.CLASS_NAME, "radioBranded")
        for i in range(0, 4):
            optionButton[i].click()
        nextLink = driver.find_elements(By.ID, "NextButton")
        # if len(nextLink) == 0:
        #     break
        nextLink[0].click()





def main(code, month, day, year, hour, minute):
    inputSurveyCode(code, month, day, year, hour, minute)
    fill_survey()
    driver.quit()

main("0855037844", '04',11,22,11,'06')
