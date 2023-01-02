from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time



def scrapingInvestx():
    options = Options()
    #options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("https://fr.investing.com/economic-calendar/")

    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    driver.find_element(By.ID, "filterStateAnchor").click()
    time.sleep(3)
    driver.find_element(By.ID, "importance3").click()
    driver.find_element(By.ID, "ecSubmitButton").click()
    time.sleep(3)
    table = driver.find_element(By.ID, "economicCalendarData")

    f = open("test.txt", "w")
    f.write(table.text)
    f.close()

    driver.quit()