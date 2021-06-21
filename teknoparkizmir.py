import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    # links = []

    driver.get('https://teknoparkizmir.com.tr/tr/firma-listesi/')
    companies_count = driver.find_elements_by_xpath('/html/body/section[2]/div/div/div/div/div/div/div[3]/div')
    # for indx in range(1, len(companies_count)):
    #     company_link = driver.find_element_by_xpath(f'').get_attribute('href')
    #     links.append(company_link)

    for indx in range(1, len(companies_count) + 1):
        company = {}

        try:
            # driver.get(link)
            company_name = driver.find_element_by_xpath(f'/html/body/section[2]/div/div/div/div/div/div/div[3]/div[{indx}]/div/div/div/div/div/div[2]/a/h3').text
            company_email = driver.find_element_by_xpath(f'/html/body/section[2]/div/div/div/div/div/div/div[3]/div[{indx}]'
                                                         '/div/div/div/div/div/div[2]/div[3]/div[3]/a').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
