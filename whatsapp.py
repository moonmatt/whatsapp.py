# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Uncomment if you want to load strings from text file
# filepath = 'Iliad.txt' # Change the file name


# START ! COMMENT THIS ALL IF YOU WANT TO LOAD STRINGS FROM TEXT FILE

# Input of the chat name
target = input("Target: ")
target = '"' + target + '"'

# Input of the message content
string = input("Content of the message: ")

# Input of the number of total messages
mNumber = int(input("Number of messages: "))

# Input of the seconds to wait between messages
mWait = int(input("Seconds to wait between messages: "))

# END ! COMMENT THIS ALL IF YOU WANT TO LOAD STRINGS FROM TEXT FILE


# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//body'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))


# Uncomment if you want to load strings from text file
#with open(filepath) as fp:
#    string = fp.readline()
#    cnt = 0
#    while string:
#        string = fp.readline()
#        cnt += 1
#        input_box.send_keys("    " + str(string) + Keys.ENTER)
#        time.sleep(300) # Change the seconds interval (300 is 5 minutes)

# START ! COMMENT THIS ALL IF YOU WANT TO LOAD STRINGS FROM TEXT FILE

for i in range(mNumber):
    input_box.send_keys("    " + string + Keys.ENTER)
    time.sleep(mWait)

# END ! COMMENT THIS ALL IF YOU WANT TO LOAD STRINGS FROM TEXT FILE