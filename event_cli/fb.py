from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from event_cli.config import SELENIUM_DRIVER_LOCATION

binary = FirefoxBinary(SELENIUM_DRIVER_LOCATION)
driver = webdriver.Firefox(firefox_binary=binary)


def login_to_fb(driver, usr, pwd):
    driver.get("http://www.facebook.org")
    assert "Facebook" in driver.title
    email_input = driver.find_element_by_id("email")
    email_input.send_keys(usr)
    password_input = driver.find_element_by_id("pass")
    password_input.send_keys(pwd)
    password_input.send_keys(Keys.RETURN)


def move_to_create_event_modal(driver):
    driver.get("https://www.facebook.com/hackerspacetrojmiasto/")
    sleep(randint(1, 3))
    driver.get("https://www.facebook.com/pg/hackerspacetrojmiasto/events/?ref=page_internal")
    sleep(randint(6, 11))
    create_event = driver.find_element_by_xpath("//*[contains(text(), 'Create Event')]")
    create_event.click()


def fill_data(driver, title, description):
    sleep(randint(5, 8))
    title_input = driver.find_element_by_xpath("//input[@placeholder='Add a short, clear name']")
    title_input.click()
    title_input.send_keys(title)
    sleep(randint(8, 14))
    description_input = driver.find_element_by_xpath("//input[@placeholder='Tell people more about the event']")
    description_input.click()
    description_input.send_keys(description)


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


def choose_month_in_calendar(driver, desired_month):
    sleep(randint(5, 8))
    for month in months:
        if driver.find_element_by_xpath("//*[contains(text(), " + month + ")]").is_displayed():
            currently_choosed_month = driver.find_element_by_xpath("//*[contains(text(), " + month + ")]")
    previous_month = driver.find_element_by_xpath("//button[contains(@title,'Previous month')]")
    next_month = driver.find_element_by_xpath("//button[contains(@title,'Next month')]")
    while True:
        if desired_month == currently_choosed_month:
            break
        if months.index(currently_choosed_month) < months.index(desired_month):
            next_month.click()
            sleep(randint(5, 8))
            previous_month = driver.find_element_by_xpath("//button[contains(@title,'Previous month')]")
            next_month = driver.find_element_by_xpath("//button[contains(@title,'Next month')]")
        if months.index(currently_choosed_month) > months.index(desired_month):
            previous_month.click()
            sleep(randint(5, 8))
            previous_month = driver.find_element_by_xpath("//button[contains(@title,'Previous month')]")
            next_month = driver.find_element_by_xpath("//button[contains(@title,'Next month')]")


def main():
    login_to_fb(driver, 'xxx', 'xxx')
    sleep(randint(5, 8))
    move_to_create_event_modal(driver)
    sleep(randint(5, 8))
    fill_data(driver, "Cool tytuł", "Ciekawy opis")
    sleep(randint(5, 8))
    choose_month_in_calendar(driver, months[1])


if __name__ == '__main__':
    main()
