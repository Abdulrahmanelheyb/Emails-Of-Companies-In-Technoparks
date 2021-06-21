import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.yildizteknopark.com.tr/tr/firmalar#')
    companies_count = driver.find_elements_by_xpath('/html/body/div[1]/div/div[7]/div')

    for indx in range(1, len(companies_count) + 1):
        company_link = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[7]/div[{indx}]/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}

        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/h1').text
            company_email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/div[4]/span/a').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
