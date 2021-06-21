import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.pauteknokent.com.tr/firmalar.php')
    companies_count = driver.find_elements_by_xpath('//*[@id="firmalar"]/tr')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'//*[@id="firmalar"]/tr[{indx}]/td[2]/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}

        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('//*[@id="box_wrapper"]/section[1]/div/div/div/h1').text
            company_email = driver.find_element_by_xpath('//*[@id="box_wrapper"]/section[2]/div[2]/div/div[2]/div[1]/div[6]/a/div/span[3]').text

            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
