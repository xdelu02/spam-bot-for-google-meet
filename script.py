from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


########################################

# THE SCRIPT WORKS ONLY WITHOUT ANY MICROPHONE CONNECTED

########################################

PATH = "C:\Program Files (x86)\chromedriver.exe"  #make sure to have the proper path setted
driver = webdriver.Chrome(PATH)
e = ""  #Insert email google
p = ""  #Insert password google


def auth():
    driver.get("https://accounts.google.com/signin")

    #input Email
    email = driver.find_element_by_id("identifierId")
    email.send_keys(e)
    email.send_keys(Keys.RETURN)

    time.sleep(2.5)
    #input Password
    password = driver.find_element_by_name("password")
    password.send_keys(p)
    password.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/header/h1'))
	)


def spamBot():
    driver.execute_script('''window.open("https://meet.google.com/wyg-gdiu-rfn","_blank");''')   #open new tab
    driver.switch_to.window(driver.window_handles[-1])   #switch to last tab
    time.sleep(2.5)
    join = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
    join.click()  #join to meet


if __name__ == "__main__":
    auth()
    for i in range(1,5):   #change 5 with the number of times that you want to access to meet
        spamBot()