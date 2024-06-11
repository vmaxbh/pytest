from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Importa as opções do Chrome
from selenium.webdriver.common.by import By
import time

def login(username, password):
    options = Options()  # Cria uma instância de opções
    options.add_argument("--headless")  # Adiciona a opção headless

    driver = webdriver.Chrome()#options=options
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")

    username_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
    password_field = driver.find_element(By.XPATH, "//*[@id='password']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    btnLogin = driver.find_element(By.XPATH, "//*[@id='login-button']")
    btnLogin.click()
    time.sleep(5)
    app_logo = driver.find_element(By.XPATH, "//*[@class='app_logo']")
    
    # Verifica se o elemento está visível
    assert app_logo.is_displayed(), "Componente.app_logo não está visível na página."

    return driver