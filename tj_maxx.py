from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

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
    # while len(nextLink) != 0:
    optionButton = driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0, 3):
        optionButton[i].click()
        # nextLink = driver.find_elements(By.ID, "NextButton")
        # if len(nextLink) == 0:
        #     break
    next()
    q4 = driver.find_element(By.CLASS_NAME, "radioBranded")
    q4.click()
    next()
    q5 = driver.find_elements(By.CLASS_NAME, "radioBranded") # elements with an S!!!!
    for i in range(0 ,21, 6):
        q5[i].click()
    next()
    q6 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    try:
       for i in range(0,26,6):
        q6[i].click()
        next()
    except: Exception

    next()
    q7 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,2,1):
        q7[i].click()
    next()
    q8 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    if len(q8) ==0:
        q8 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
        q8[0].click()
    else:
        for i in range(1):
            q8[1].click()
    next()
    q9 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
    if len(q9) != 0:
        q9[0].click()
        next()
    q10 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    if len(q10) ==0:
        q10 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
        q10[0].click()
    else:
        for i in range(0,len(q10),3):
            q10[i].click()
    next()
    next()
    q11 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(4,3):
        q11[i].click()
    next()
    q12 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    if len(q12) == 0:
        next()
    else:
        q12[2].click()
    next()
    try:
        q13 = driver.find_elements(By.CLASS_NAME, "radioBranded")
        q13[random.randrange(0,len(q13))].click()
    except: Exception
    next()
    q14 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
    if len(q14) != 0:
        for i in range(0,12,random.randrange(0,12)):
            q14[i].click()
    next()
    q15 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
    try:
        for i in range(0,len(q15),random.randint(0,len(q15))):
            q15[i].click()
        next()
    except: Exception

    q16 = driver.find_element(By.ID, "R31000")
    q16.send_keys(input("Whole dollar amount? >>\t"))
    next()
    q17 = driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,5,2):
        q17[i].click()
    next()
    q18 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,3,2):
        q18[i].click()
    next()
    q19 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
    for i in range(0,14,random.randint(0,14)):
        q19[i].click()
    next()
    q20 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,3,2):
        q20[i].click()
    next()
    q21 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,3,2):
        q21[i].click()
    next()
    q22 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,7,6):
        q22[i].click()
    next()
    q23 = driver.find_element(By.ID, "R32000")
    q23.send_keys(random.randint(1,6))
    next()
    q24 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,5,4):
        q24[i].click()
    next()
    q25 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    for i in range(0,7,6):
        q25[i].click()
    next()
    q27 = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
    for i in range(0,7,6):
        q27[i].click()
    next()
    q28 =driver.find_elements(By.CLASS_NAME, "radioBranded")
    q28[1].click()
    next()


def fill_contact(first, last, email, phone_number = 999-999-9999):
    fname = driver.find_element(By.ID, "S91000")
    fname.send_keys(first)
    lname = driver.find_element(By.ID,"S9300")
    lname.send_keys(last)
    email1 = driver.find_element(By.ID, "S94000")
    email1.send_keys(email)
    email2 = driver.find_element(By.ID, "S9500")
    email2.send_keys(email)
    ph = driver.find_element(By.ID, "S92000")
    ph.send_keys(phone_number)
    next()

def fill_recur():
    q16 = None
    q23 = None
    while True:
        try:
            check = driver.find_elements(By.CLASS_NAME, "checkboxBranded")
        except: Exception
        try:
            multi = driver.find_elements(By.CLASS_NAME, "radioBranded")
        except: Exception
        try:
            q16 = driver.find_element(By.ID, "R31000")
        except: Exception
        try:
            text = driver.find_element(By.CLASS_NAME, "textinputwrapper")
        except: Exception
        try:
            q23 = driver.find_element(By.ID, "R32000")
        except: Exception
        try:
            card = driver.find_element(By.CSS_SELECTOR)


        if len(check) != 0:
            for i in range(0, len(check), 2):
                check[i].click()
        elif len(multi) != 0:
            if len(multi) >= 6:
                try:
                    for i in range(0,len(multi) + 1, 6):
                        multi[i].click()
                except: Exception
                for i in range(0,len(multi), 2):
                        multi[i].click()
            else:
                multi[1].click()
        elif q16 != None:
            q16.send_keys(input("Whole dollar amount? >>\t"))
            q16 = None
        elif text != None:
            print("!")
        elif q23 != None:
            q23.send_keys(random.randint(1,6))
        next()

















def main(code, month, day, year, hour, minute, first_name, last_name, email, phone_with_dash = "999-999-9999"):
    inputSurveyCode(code, month, day, year, hour, minute)
    fill_recur()
    fill_contact(first_name,last_name,email,phone_with_dash)

def test():
    main("0855037844", '04',11,22,11,'06', "a","w","a@a.com")

test()
