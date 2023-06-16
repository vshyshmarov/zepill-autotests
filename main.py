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

# Наведение мыши на элемент, чтобы открыть всплывающее окно
drop_down = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapwrap > header > div:nth-child(3) > div > div.menu-bars.element-container.d-none.d-lg-block > a > span"))
)

# Создание экземпляра класса ActionChains и наведение на элемент
actions = ActionChains(driver)
actions.move_to_element(drop_down).perform()

# Наведение мыши на элемент во всплывающем окне
additives = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapwrap > header > div:nth-child(3) > div > div.menu-bars.element-container.d-none.d-lg-block > div > div > div > div:nth-child(1) > a"))
)
actions.move_to_element(additives).perform()

# После наведения мыши на элемент, кнопка станет доступной
vitamins = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapwrap > header > div:nth-child(3) > div > div.menu-bars.element-container.d-none.d-lg-block > div > div > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > a"))
)
actions.move_to_element(vitamins).click().perform()

item_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#products_grid > div:nth-child(1) > form > div"))
)
item_1.click()

sleep(3)

add_button_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.row > div:nth-child(2) > div.quantity-block > div.quantity-block-input.css_quantity.input-group.oe_website_spinner > div.input-group-append > a"))
)
add_button_1.click()
add_button_1.click()

add_to_cart_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.js-product-sell-control > a"))
)
add_to_cart_1.click()

breadcrumb_1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_detail > div:nth-child(1) > div > ol > li:nth-child(3) > a"))
)
breadcrumb_1.click()

item_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#products_grid > div:nth-child(2) > form > div"))
)
item_2.click()

add_to_cart_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.js-product-sell-control > a"))
)
add_to_cart_2.click()

breadcrumb_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_detail > div:nth-child(1) > div > ol > li:nth-child(3) > a"))
)
breadcrumb_2.click()

item_3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#products_grid > div:nth-child(4) > form > div"))
)
item_3.click()

sleep(3)

add_button_3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.row > div:nth-child(2) > div.quantity-block > div.quantity-block-input.css_quantity.input-group.oe_website_spinner > div.input-group-append > a"))
)
add_button_3.click()

add_to_cart_3 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.js-product-sell-control > a"))
)
add_to_cart_3.click()

cart = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapwrap > header > nav > div > div.main-menu-container.page-element > div > div.control-container > div.shopping-cart-container"))
)
actions.move_to_element(cart).perform()

sleep(3)

basket = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#wrapwrap > header > nav > div > div.main-menu-container.page-element > div > div.control-container > div.shopping-cart-container > div > div > div > div.text-center > a.btn.btn-orange"))
)
actions.move_to_element(basket).click().perform()

# Найдите элемент с ценой товара
price_element_1 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(1) > td.text-center.td-price-unit")

# Получите текст или значение элемента
price_value_1 = float(price_element_1.text.replace('₴', '').replace(',', '.'))

# Найдите элемент с количеством товара
amount_element_1 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(1) > td.text-center.td-qty > div.css_quantity.input-group.mx-auto.oe_website_spinner > input")

# Получите значение количества товара
amount_value_1 = int(amount_element_1.get_attribute("value"))

# Вычислите ожидаемую общую сумму
expected_total_amount_1 = price_value_1 * amount_value_1

# Найдите элемент с ценой товара
price_element_2 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(2) > td.text-center.td-price-unit")

# Получите текст или значение элемента
price_value_2 = float(price_element_2.text.replace('₴', '').replace(',', '.'))

# Найдите элемент с количеством товара
amount_element_2 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(2) > td.text-center.td-qty > div.css_quantity.input-group.mx-auto.oe_website_spinner > input")

# Получите значение количества товара
amount_value_2 = int(amount_element_2.get_attribute("value"))

# Вычислите ожидаемую общую сумму
expected_total_amount_2 = price_value_2 * amount_value_2

# Найдите элемент с ценой товара
price_element_3 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(3) > td.text-center.td-price-unit")

# Получите текст или значение элемента
price_value_3 = float(price_element_3.text.replace('₴', '').replace(',', '.'))

# Найдите элемент с количеством товара
amount_element_3 = driver.find_element(By.CSS_SELECTOR, "#cart_products > tbody > tr:nth-child(3) > td.text-center.td-qty > div.css_quantity.input-group.mx-auto.oe_website_spinner > input")

# Получите значение количества товара
amount_value_3 = int(amount_element_3.get_attribute("value"))

# Вычислите ожидаемую общую сумму
expected_total_amount_3 = price_value_3 * amount_value_3

expected_total_amount = sum([expected_total_amount_1,expected_total_amount_2,expected_total_amount_3])

# Найдите элемент с отображаемой общей суммой на странице
total_amount_element = driver.find_element(By.CSS_SELECTOR, "#order_total > td.text-xl-right > strong > span")

# Получите текст или значение элемента
total_amount_displayed = float(total_amount_element.text.replace('₴', '').replace(',', '.').replace(' ', ''))

# Сравните полученную общую сумму с отображаемой суммой
assert expected_total_amount == total_amount_displayed, f"Неправильная общая сумма товаров в корзине. " \
                                                       f"Получено: {total_amount_displayed}, " \
                                                       f"Ожидаемо: {expected_total_amount}"
print(f"Ожидаемая общая сумма: {expected_total_amount}")
print(f"Отображаемая общая сумма: {total_amount_displayed}")