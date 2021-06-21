import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.ostimteknopark.com.tr/firma-arsiv')
    companies_count = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[2]/div[{indx}]/div/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}

        try:
            driver.get(link)
            company_info = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/span').text
            company_info = company_info.replace('\n', ' ')
            company_info = company_info.split(' ')
            for comp_info in company_info:
                if '@' in comp_info:
                    company_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/h1').text
                    company_email = comp_info.lstrip()

                    if '@' in company_email:
                        company['Name'] = company_name
                        company['Email'] = company_email
                        companies.append(company)
                        break

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
