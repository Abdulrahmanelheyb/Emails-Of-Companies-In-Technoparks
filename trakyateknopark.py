import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []

    driver.get('https://www.trakyateknopark.com.tr/firmalarimiz')
    companies_count = driver.find_elements_by_xpath('//*[@id="singlepg"]/div[2]/div/div/div')
    rlt = len(companies_count)
    for indx in range(1, len(companies_count) + 1):
        company_link = driver.find_element_by_xpath(f'//*[@id="singlepg"]/div[2]/div/div/div[{indx}]/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}

        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('//*[@id="singlepg"]/div[2]/div/div[1]/div[1]').text
            company_info = driver.find_element_by_xpath('//*[@id="singlepg"]/div[2]/div/div[2]/div/p[2]').text
            words_list = company_info.split(' ')

            for word in words_list:

                if '@' in word:
                    company_email = word

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
