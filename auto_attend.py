import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from creds import *

dirname = os.path.dirname(__file__)
chromedriver = os.path.join(dirname, 'chromedriver')
log_file_path = os.path.join(dirname, 'logs.txt')

options = Options()
options.add_argument("--user-data-dir=./chrome_profile/")
options.add_argument("--profile-directory=AutoLogin")
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

log_file = open(log_file_path, "a+")
flag = True

try:
    driver.get("https://bulkmro.hrstoppro.com/")
except:
    flag = False
    log_file.write(datetime.now().strftime("%b %d, %H:%M") + "  : Page request FAILED.")

if flag:
    try:
        form = driver.find_element_by_id('tbemail')
        form.clear()
        form.send_keys(email)
        form = driver.find_element_by_id('tbpassword')
        form.clear()
        form.send_keys(password)
        form.submit()

        log_file.write(datetime.now().strftime("%b %d, %H:%M") + ": New sign-in")
    except:
        pass

    time_now = datetime.now().time()
    time_of_login = datetime.strptime(time_of_login, '%H:%M').time()
    time_of_logout = datetime.strptime(time_of_logout, '%H:%M').time()
    last_time_of_login = datetime.strptime(last_time_of_login, '%H:%M').time()
    last_time_of_logout = datetime.strptime(last_time_of_logout, '%H:%M').time()

    if time_now>time_of_login and time_now<last_time_of_login:
        button = driver.find_element_by_id('timein')
        button.click()
        log_file.write(datetime.now().strftime("%b %d, %H:%M") + " - Login successful\n")
    elif time_now>time_of_logout and time_now<last_time_of_logout:
        button = driver.find_element_by_id('timeout')
        button.click()
        log_file.write(datetime.now().strftime("%b %d, %H:%M") + " - Logout successful\n\n")

log_file.close()
driver.close()
driver.quit()
