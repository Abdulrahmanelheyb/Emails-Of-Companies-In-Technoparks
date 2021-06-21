import base
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


def execute():
    driver = base.get_driver()
    driver.set_window_size(1400, 1000)
    companies = []
    links = []

    driver.get("https://www.ankarateknokent.com/firmalarimiz/")

    companies_elements = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div')
    for indx in range(1, len(companies_elements)):
        link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[{indx}]/div/div[1]/div/a')
        links.append(link.get_attribute('href'))

    for link in links:
        driver.get(link)

        try:
            company = {}
            name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[1]/div[1]/div/div/div/h1')
            company['Name'] = name.text
            email = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[5]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]'
                                                  f'/div[2]/div[2]/div/div[2]/div[2]')
            company['Email'] = email.text
            companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(base.get_file_path('anakarateknokent'), companies)
    driver.close()
