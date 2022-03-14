import selenium as sl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

path = "chromedriver"

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
nav = webdriver.Chrome(path, options=options)

nav.get('https://br.tribalwars2.com/page#/')

waiting = True
while waiting:
    try:
        WebDriverWait(nav, 5).until(
            EC.title_contains("Tribal Wars 2 (")
        )
    except TimeoutException:
        print("Faça login e selecione um mundo")
        pass
    except WebDriverException:
        print("Exceção: chrome nr")
    else:
        waiting = False

# Espera fim do loading
waiting = True
while waiting:
    try:
        WebDriverWait(nav, 5).until(
            EC.invisibility_of_element_located((By.ID, 'screen-loading'))
        )
    except TimeoutException:
        print("Carregando...")
        pass
    else:
        waiting = False


print("Fim")