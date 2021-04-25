from selenium.webdriver.common.keys import Keys
import time


def login_medium(mail, driver):
    driver.get('https://medium.com/')
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/button").click()
    time.sleep(2)
    driver.find_element_by_link_text("Sign In").click()
    time.sleep(2)
    driver.find_element_by_id("email-susi-button-clickable").click()
    time.sleep(2)
    search = driver.find_element_by_xpath('//*[@id="susi-modal-background"]/div/div/div[3]/div/div[1]/div/div/div[2]/div/p/input')
    search.send_keys(mail)
    search.send_keys(Keys.RETURN)
    driver.quit()


def login_email(mail, password, driver):
    driver.get('https://outlook.live.com/owa/')
    driver.find_element_by_link_text("Accedi").click()
    time.sleep(2)
    search = driver.find_element_by_id("i0116")
    search.send_keys(mail)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    search = driver.find_element_by_id("i0118")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Pivot23-Tab1"]/span/div/div/span/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Pivot23-Tab1"]/span/div/div/span/span').click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[text()='Medium']").click()
    time.sleep(2)
    driver.find_element_by_link_text("Sign in to Medium").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
