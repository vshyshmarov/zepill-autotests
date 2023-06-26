from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.action_chains import ActionChains

# инициализация WebDriver
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.maximize_window()

# открытие веб-сайта
driver.get("https://zepill.com/")

#указываем нужный слайд
slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(("xpath", "/html/body/div/main/div/div[3]/div[1]/div"))
)

# Прокрутите страницу до слайдера
actions = ActionChains(driver)
actions.move_to_element(slider).perform()

# Найдите кнопку, которую хотите нажать
scroll_button = driver.find_element("xpath", "/html/body/div/main/div/div[3]/div[1]/div/div[2]/button[2]")

# Взаимодействие с кнопкой
scroll_button.click()
scroll_button.click()

# выбор категории "Нервная система"
nervous_system = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                "#wrap > div.categories-slider-band.mb40 > div.catigories-slider-container.d-none.d-sm-block > div > div.owl-stage-outer > div > div:nth-child(22) > a > div > span"))
)
nervous_system.click()

# выбираем для сравнения первый элемент
select_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#products_grid > div:nth-child(1) > form > div > section > div.product_price > button"))
)
select_1.click()

# выбираем для сравнения второй элемент
select_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#products_grid > div:nth-child(2) > form > div > section > div.product_price > button"))
)
select_2.click()

# выбираем для сравнения третий элемент
select_3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#products_grid > div:nth-child(3) > form > div > section > div.product_price > button"))
)
select_3.click()

sleep(3)

# кнопка сравнения
compare_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div[2]/div[5]/div/div[2]/div[2]/a"))
)
compare_button.click()

sleep(10)

# Закрытие браузера
driver.quit()
