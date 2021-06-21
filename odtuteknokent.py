import time
import base
from selenium.common.exceptions import *


def exceute() -> []:
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://odtuteknokent.com.tr/tr/firmalar/tum-firmalar')

    companies_count = driver.find_elements_by_xpath('/html/body/div[2]/section[1]/div/div/div[2]/section/ul/li')
    companies_count[0].click()
    for indx in range(1, len(companies_count) + 1):
        try:
            company_link = driver.find_element_by_xpath(f'/html/body/div[2]/section[1]/div/div/div[1]/div[1]/div[2]/div/div/a').get_attribute('href')
            driver.find_element_by_xpath('/html/body/div[2]/section[1]/div/div/div[1]/div[1]/div[2]/div/div/div/a[2]').click()
            links.append(company_link)
            print(f'Company: {indx}')
            time.sleep(2)

        except Exception:
            pass

    for link in links:
        company = {}

        try:
            driver.get(link)

            company_name = driver.find_element_by_xpath('/html/body/div[2]/section[1]/section/div/div/div[1]/div/p').text
            company_email = driver.find_element_by_xpath('/html/body/div[2]/section[1]/div/div[1]/div[2]/div[3]/div[1]/span/a').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
