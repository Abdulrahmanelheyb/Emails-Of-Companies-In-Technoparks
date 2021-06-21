import time

import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('entertech')
    companies = []
    links = []

    driver.get('https://www.entertech.com.tr/firmalar/')
    companies_count = driver.find_elements_by_xpath('//*[@id="portfolio"]/article')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'//*[@id="portfolio"]/article[{indx}]/div/div/a[2]').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        try:
            driver.get(link)
            time.sleep(2)
            company_name = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/div[1]').text
            company_email = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/div[2]/ul/li[2]/a[1]').text
            company['Name'] = company_name
            if company_email:
                company['Email'] = company_email
            else:
                continue
            companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
