from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'
# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)
# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)
URL = " https://qa-test-selectors.netlify.app/"
try:
    browser.get(URL)

    browser.implicitly_wait(10)

    elements_by_tag = browser.find_elements(By.TAG_NAME, "h1")
    print("Элементы с тегом h1:", len(elements_by_tag))

    elements_by_name = browser.find_elements(By.NAME, "incredible-hulk")
    print("Элементы с именем incredible-hulk:", len(elements_by_name))

    elements_by_class = browser.find_elements(By.CLASS_NAME, "imageContainer")
    print("Элементы с классом imageContainer:", len(elements_by_class))

    elements_by_id = browser.find_elements(By.ID, "thor")
    print("Элементы с ID thor:", len(elements_by_id))

    elements_by_selector = browser.find_elements(By.CSS_SELECTOR,'[data-type="heroes"]')
    print("Элементы с data-type heroes:", len(elements_by_selector))
finally:
    browser.quit()