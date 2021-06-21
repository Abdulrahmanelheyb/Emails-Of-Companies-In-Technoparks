import base
from selenium.common.exceptions import *


def execute():
    driver = base.get_driver()
    filename = base.get_file_path('atateknokent')
    companies = []

    driver.get('https://www.atateknokent.com.tr/firmalar')
    companies_elements = driver.find_elements_by_xpath('//*[@id="apps"]/main/div[2]/div/section/div[1]/div')
    links = []
    for indx in range(1, len(companies_elements)):
        company_link = driver.find_element_by_xpath(f'//*[@id="apps"]/main/div[2]/div/section/div[1]/div[{indx}]/ul/div/a[1]')
        links.append(company_link.get_attribute('href'))

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('//*[@id="apps"]/main/div[1]/div/h5').text
            driver.find_element_by_xpath('//*[@id="apps"]/main/div[2]/div/div/aside/div/section/ul/li[2]/a').click()
            company_infos = driver.find_elements_by_xpath('//*[@id="apps"]/main/div[2]/div/article/div/div/div/div/div/div[1]/div/div/div/p')
            for info in company_infos:
                if "@" in info.text:
                    company_email = info.text
                    company['Name'] = company_name
                    company['Email'] = company_email
                    companies.append(company)
                    break

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
