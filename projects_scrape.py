import os
import time
import shutil
import requests
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
driver.maximize_window()

finalString = ".. raw:: html\r\n\r\n\t<table>\r\n\t\t"

for i in range(1, 10):
    driver.get("https://www.hackster.io/hardwario/projects?page="+ str(i))

    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hckui__layout__flex:nth-child(1) .project_card__title__3pebx")))
    except:
        finalString += "</table>"
        print(finalString)
        exit(-1)

    projects = driver.find_elements(By.CSS_SELECTOR, '.hckui__layout__flex')

    for project in projects:
        try:
            name = project.find_element(By.CSS_SELECTOR, " .project_card__title__3pebx")

            for x in range(1, 10):
                name.send_keys(Keys.DOWN)
        except:
            exit(-1)

        try:
            description = project.find_element(By.CSS_SELECTOR, " .hckui__typography__bodyS")
        except:
            print("no description")

        try:
            image = project.find_element(By.CSS_SELECTOR, " .lazy_image__image__hVuzg")

            """response = requests.get(image.get_attribute("src"), stream = True)

            with open(os.getcwd() + '\\source\\_static\\projects\\' + name.text + '_image.png', 'wb') as f:
                shutil.copyfileobj(response.raw, f)"""

        except:
            print("no image")

        try:
            url = project.find_element(By.CSS_SELECTOR, " .project_card__imageContainer__1cw7g")
        except:
            print("no url")


        finalString += "<tr>\r\n\t\t\t<td>\r\n\t\t\t\t<div>\r\n\t\t\t\t\t"
        finalString += "<p style=\"float: left;\"><img src=\"" + image.get_attribute("src") +"\" width=\"70%\"></p>\r\n\t\t\t\t\t"
        finalString += "<h3><a href=\"" + url.get_attribute("href") + "\">" + name.text + "</a></h3>\r\n\t\t\t\t\t"
        finalString += "<p>" + description.get_attribute('innerHTML') + "</p>\r\n\t\t\t\t"
        finalString += "</div>\r\n\t\t\t"
        finalString += "</td>\r\n\t\t</tr>\r\n\r\n\t\t"
