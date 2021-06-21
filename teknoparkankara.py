import time

import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.teknoparkankara.com.tr/Firmalar.html')
    # companies_count = driver.find_elements_by_xpath('//*[@id="da-thumbs"]/li')
    # for indx in range(1, len(companies_count)):
    #     company_link = driver.find_element_by_xpath(f'').get_attribute('href')
    #     links.append(company_link)

    for comp in driver.find_elements_by_xpath('//*[@id="da-thumbs"]/li'):
        company = {}

        try:
            # driver.get(link)
            comp.click()
            time.sleep(1)
            company_name = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/h2').text
            company_email = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[3]/div/div/a').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/button').click()

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
