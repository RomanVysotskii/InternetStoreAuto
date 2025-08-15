from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
import time
from fake_useragent import UserAgent

#Основная информация для запроса
ua = UserAgent()
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", ua.firefox)
url = "https://www.saucedemo.com"
service = Service(executable_path="D:\\programming\\python\\Selenium\\Study\\MozillaDriver\\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)


try:
    driver.get(url=url)
    time.sleep(2)
    
    #Находим имя пользователя и пароль, и вводим
    username_input = driver.find_element(By.NAME, 'user-name')
    time.sleep(2)
    username_input.clear()
    password_input = driver.find_element(By.NAME, 'password')
    time.sleep(2)
    password_input.clear()

    username_input.send_keys("standard_user")
    time.sleep(2)
    password_input.send_keys("secret_sauce")
    time.sleep(3)

    password_input.send_keys(Keys.ENTER)

    cards = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    #Находим нужный товар и добавляем в корзину
    for card in cards:
        title = card.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
        if "Bike Light" in title:
            button = card.find_element(By.CLASS_NAME, "btn")
            time.sleep(2)
            button.click()
    
    #Сортируем, находим самый дешёвый товар, добавляем в корзину
    sort = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(sort)
    select.select_by_value("lohi")

    low_price = driver.find_element(By.CLASS_NAME, "btn")
    time.sleep(2)
    low_price.click()
	
	#Заходим в корзину "оплачиваем" и "покупаем"
    basket = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    time.sleep(2)
    basket.click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "checkout_button").click()
    time.sleep(2)

    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")
    post_code = driver.find_element(By.NAME, "postalCode")

    first_name.clear()
    time.sleep(1)
    last_name.clear()
    time.sleep(1)
    post_code.clear()
    time.sleep(2)

    first_name.send_keys("Roman")
    time.sleep(1)
    last_name.send_keys("Vysotskii")
    time.sleep(1)
    post_code.send_keys("20500")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "submit-button").click()
    time.sleep(2)

    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label")
    print(total_price.text)
    time.sleep(2)

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    driver.save_screenshot("Successfully.png")

    driver.find_element(By.CLASS_NAME, "btn").click()

except Exception as ex:
    print(ex)
finally:
    time.sleep(5)
    driver.close()