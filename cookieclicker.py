from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://orteil.dashnet.org/cookieclicker/'
# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# open the browser
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(5)

# accept cookies
cookies = driver.find_element(By.CLASS_NAME, value='cc_btn_accept_all').click()

# choose language
cookies = driver.find_element(By.CLASS_NAME, value='langSelectButton').click()

# find the cookie
time.sleep(8)
click = True

while click:
    # how many cookies bot has
    number_of_cookies = driver.find_element(By.ID, value='cookies').text.split(' ')[0]
    driver.find_element(By.ID, value='bigCookie').click()

    # invest in cookie production
    for i in range(19, -1, -1):
        # click with big cookies pointer
        driver.find_element(By.ID, value='bigCookie').click()
        try:
            # click with big cookies pointer
            driver.find_element(By.ID, value='bigCookie').click()

            # check each product
            product = f'product{i}'
            driver.find_element(By.ID, value=product).click()
        except Exception as e:
            print(e)
            # click with big cookies pointer
            driver.find_element(By.ID, value='bigCookie').click()

# close the browser
driver.quit()