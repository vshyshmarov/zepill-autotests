from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Инициализация WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Открытие веб-сайта
driver.get("https://zepill.com/")

# Поиск товара
search_box = driver.find_element(By.CSS_SELECTOR, "#headerSearch")
search_box.send_keys("Mega multi, для жінок")
search_box.submit()

# Открытие страницы товара
product_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#products_grid > div > form > div"))
)
product_link.click()

# Добавление товара в корзину
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_details > form > div > div.js-product-sell-control > a"))
)
add_to_cart_button.click()

# Переход в корзину
view_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#wrapwrap > header > nav > div > div.main-menu-container.page-element > div > div.control-container > div.shopping-cart-container > a > span"))
)
view_cart_button.click()

# Оформление товара
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#wrap > div.container.oe_website_sale.py-2 > div.row.order-checkout > div.col-12.col-xl-8.oe_cart > div > div > a.btn.btn-primary.float-right.d-none.d-xl-inline-block"))
)
checkout_button.click()

# Ввод информации о покупателе и оформление заказа
name_input = driver.find_element(By.CSS_SELECTOR, "#div_name > input")
name_input.send_keys("Test")

email_input = driver.find_element(By.CSS_SELECTOR, "#div_email > input")
email_input.send_keys("test@test.com")

mobile_input = driver.find_element(By.CSS_SELECTOR, "#div_mobile > input")
mobile_input.send_keys("1111111111")

next_button_1 = driver.find_element(By.CSS_SELECTOR, "#submit-contacts > div.button-container > a")
next_button_1.click()

#выбор способа доставки
select_delivery = driver.find_element(By.CSS_SELECTOR, "#pickup-delivery-tab")
select_delivery.click()

next_button_2 = driver.find_element(By.CSS_SELECTOR, "#submit-shipping-pickup > div.button-container > a")
next_button_2.click()

#выбор способа оплаты
select_payment = driver.find_element(By.CSS_SELECTOR, "#submit-payment > div.card.mb16 > div:nth-child(4) > label > input[type=radio]")
select_payment.click()

next_button_3 = driver.find_element(By.CSS_SELECTOR, "#submit-payment > div.button-container > a")
next_button_3.click()

#кнопка заказа товара
confirm_button = driver.find_element(By.CSS_SELECTOR, "#wrap > div > div.row.order-checkout > div.col-12.col-xl-8.oe_cart > div > div > div.d-none.d-xl-block.mt8 > a.btn.btn-primary.float-right.js-submit-order > span:nth-child(1)")
confirm_button.click()

#распечатать накладную
print_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#wrap > div.container.oe_website_sale.confirmation-container.py-2 > div.row > div.col-12.col-xl > div > div.thanks_msg > span > a"))
)
print_button.click()

sleep(30)

driver.quit()