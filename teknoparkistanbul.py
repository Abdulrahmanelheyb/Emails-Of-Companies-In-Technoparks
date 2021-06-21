import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.teknoparkistanbul.com.tr/firmalar')
    companies_count = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[{indx}]/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}

        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]').text
            company_name = company_name.replace(driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/i').text, '')\
                .replace(' ', '').replace('\n', '')
            company_email = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[6]/div/b/a').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
