from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Time
time_next_checkpoint = 7
timeout = time.time() + 60*5
checkpoint = time.time() + time_next_checkpoint

# Setting up selenium
chrome_driver_path = '/Users/sznaz/Desktop/Web development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# Opening the webpage
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# Finds the cookie
cookie = driver.find_element_by_css_selector("#cookie")


#Variable
paths = {
    0: '//*[@id="buyCursor"]',
    1: '//*[@id="buyGrandma"]',
    2: '//*[@id="buyFactory"]',
    3: '//*[@id="buyMine"]',
    4: '//*[@id="buyShipment"]',
    5: '//*[@id="buyAlchemy lab"]',
    6: '//*[@id="buyPortal"]',
    7: '//*[@id="buyTime machine"]'
}


# Loop to continuously click the cookie
while True:

    cookie.click()

    # Breaks the loop once it has been 5 minutes
    if time.time() > timeout:
        print('Breaking the loop')
        final_score = driver.find_element_by_css_selector('#cps')
        print(final_score.text)
        break
    elif time.time() >= checkpoint:
        print('checkpoint')
        # Keeps track of the score.
        score = driver.find_element_by_css_selector("#money")
        print(score.text)
        current_score = int(score.text.replace(",","").strip())
        checkpoint = time.time() + time_next_checkpoint

        # Finds the options available
        options = driver.find_elements_by_css_selector("#store div b")
        option_amount = []
        for i in range(0, len(options) - 1, 1):
            option_amount.append(int(options[i].text.split("-")[1].replace(",", "").strip()))

        # Runs a loop to see which option is the best
        highest_price_available = 0
        highest_index = 0
        for amount in option_amount:
            if current_score >= amount:
                highest_price_available = amount
                highest_index = option_amount.index(highest_price_available)
        print(f'the index is {highest_index}')

        selector = driver.find_element_by_xpath(paths[highest_index])
        selector.click()



