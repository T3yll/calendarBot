from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from line import makeBetter
import time
import datetime

TOKEN = '5816366753:AAGPCAPy4TXwAZiamgYCTBxHkC_LCUh4Jxk'


def start(update, context):
    update.message.reply_text("""
Le bot a bien été lancé

Les commandes disponibles sont :
- /calendar pour obtenir le calendrier economique du jour
    """)


def calendar(context: CallbackContext):
    updater = Updater(TOKEN, use_context=True)
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

    with open(r"test.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])

    makeBetter()

    f = open("final.txt", "r")
    message = f.read()
    print(message)
    context.bot.send_message(5679547099,message)
    driver.quit()

def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(TOKEN, use_context=True)

    j = updater.job_queue
    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("calendar", calendar))
   
    job_daily = j.run_daily(calendar, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=10, minute=00, second=00))

    updater.start_polling()
    # Sert à lancer le bot

    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()

if __name__ == '__main__':
    main()