from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

# Configurações do navegador
options = Options()
options.add_argument("--start-maximized")

# Credenciais
username = "usuario"
password = "senha"

# Inicia o navegador com as opções
driver = webdriver.Chrome(options=options)

# Acessa a página de login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Faz login
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
time.sleep(7)

# Acessa a postagem
driver.get("https://www.instagram.com/p/DLtF-S8x9rw/")
time.sleep(10)

# Usa o pyautogui para clicar onde fica o campo de comentário
# Aguarda alguns segundos para garantir que a página está pronta
time.sleep(3)
pyautogui.click(x=1343, y=927)
time.sleep(1)

# Digita "oi"
pyautogui.write("oi", interval=0.05)
time.sleep(1)

# Pressiona Enter para enviar
pyautogui.press("enter")

time.sleep(30)
