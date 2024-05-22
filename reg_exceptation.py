import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'
# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)
# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)
URL = "https://qa-course.netlify.app/registration-form"
try:
 # Открытие веб-страницы
    browser.get(URL)
 # Неявное ожидание для загрузки элементов страницы
    browser.implicitly_wait(10)
 # Выбор первого встреченного input по тегу
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Vladas")
 # Выбор элемента по имени
    input2 = browser.find_element(By.NAME, "lastName")
    input2.send_keys("Gechis")
 # Выбор третьего элемента, найденного по названию класса
    input3 = browser.find_elements(By.CLASS_NAME, "formControl")[2]
    input3.send_keys("Lithuania")
 # Выбор элемента ввода, найденного по XPath
    input4 = browser.find_element(By.XPATH, "//input[@name='city']")
    input4.send_keys("Vilnius")
 # Выбор элемента ввода, найденного по XPath
    input5 = browser.find_element(By.XPATH, "//input[@name='email']")
    input5.send_keys("vvladas@bk.ru")
 # Выбор элемента ввода, найденного по XPath
    input6 = browser.find_element(By.NAME, "phone")
    input6.send_keys("+79237772288")

 # Выбор элемента, найденного по CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click() # Нажатие кнопки
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
 # Задержка перед закрытием браузера
    time.sleep(5)
 # закрываем браузер после всех манипуляций
    browser.quit()
