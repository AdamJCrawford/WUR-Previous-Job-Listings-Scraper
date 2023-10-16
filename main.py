from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
import csv


def main():
    url = "https://web.archive.org/web/*/https://www.wur.nl/en/vacancy/*"
    webdriver_path = "C:/Users/adamc/Downloads/chromedriver-win64/chromedriver-win64/chromedriver"
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.get(url)
    sleep(5)
    elements = [driver.find_elements(
        By.CLASS_NAME, 'even'), driver.find_elements(By.CLASS_NAME, 'odd')]

    # Process and print the extracted data
    next_button = driver.find_element(
        By.XPATH, '//*[@id="resultsUrl_next"]/a')

    with open("data.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(34):
            for class_name in elements:
                for element in class_name:
                    driver.implicitly_wait(2)
                    parts = element.get_attribute("innerText").split()
                    url = "https://web.archive.org/" + \
                        element.get_attribute('outerHTML').split('>')[
                            2][10:-1].replace('*', '')
                    first_date = "".join([parts[2]] + [' '] + parts[3:5])
                    second_date = "".join([parts[5]] + [' '] + parts[6:8])
                    writer.writerow([url, first_date, second_date])

            try:
                next_button.click()

            except StaleElementReferenceException:
                # Handle the exception by re-locating the element or retrying the click
                next_button = driver.find_element(
                    By.XPATH, '//*[@id="resultsUrl_next"]/a')
                next_button.click()
            elements = [driver.find_elements(
                By.CLASS_NAME, 'even'), driver.find_elements(By.CLASS_NAME, 'odd')]
    # Close the browser window
    driver.quit()


if __name__ == "__main__":
    main()
