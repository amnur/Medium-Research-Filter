from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import stdiomask
import threading
import time
from login import login_medium, login_email
from checker import check_exists_by_xpath


print('\n::::::::: WELCOME TO MEDIUM RESEARCHER :::::::::\n')
mail = input('Mail:\t')
password = stdiomask.getpass()
topic = input('\nWhat do you want to search?\t')
pages = int(input('\nHow many pages do you want to open?\t'))

path = 'C:\Program Files\chromedriver.exe'

driver1 = webdriver.Chrome(path)
driver2 = webdriver.Chrome(path)

t1 = threading.Thread(target=login_medium, args=(mail, driver1))
t2 = threading.Thread(target=login_email, args=(mail, password, driver2))

t1.start()
t2.start()

t1.join()
t2.join()

search_xpath = '//*[@id="root"]/div/nav/div/div/div/div/div[2]/div/div[2]/a'

if check_exists_by_xpath(driver2, search_xpath):
    try:
        element = driver2.find_element_by_xpath(search_xpath)
        driver2.execute_script("arguments[0].click();", element)
        time.sleep(3)
    except ElementNotInteractableException as e:
        print('Error: ', e)
else:
    print('Error!')

new_page_index = 2

while topic != '':
    search = driver2.find_element_by_class_name('js-searchInput')
    search.clear()
    search.send_keys(topic)
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    xpath_upgrade = '//*[@id="paywall-subtitle-copy-fewer-clicks"]'
    all_articles = driver2.find_elements_by_link_text('Read more…')
    pages = pages if len(all_articles) > pages else len(all_articles)

    for i in range(pages):
        article = driver2.find_elements_by_link_text('Read more…')[i]
        key_code = Keys.CONTROL
        driver2.execute_script(f"window.open('{article.get_attribute('href')}');")
        main_page = driver2.window_handles[1]
        new_page = driver2.window_handles[new_page_index]
        driver2.switch_to.window(new_page)
        if check_exists_by_xpath(driver2, xpath_upgrade):
            new_page_index -= 1
            driver2.close()
        new_page_index += 1
        driver2.switch_to.window(main_page)

    topic = input('What do you want to search?\t')
