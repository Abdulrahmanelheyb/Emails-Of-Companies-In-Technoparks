import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('gbteknokent')
    companies = []
    links = []

    driver.get('http://gbteknokent.com/firmalarimiz/')
    companies_count = driver.find_elements_by_xpath('//*[@id="main"]/div[3]/div[1]/div/div/div/div')
    for indx in range(1, len(companies_count)):
        try:
            company_link = driver.find_element_by_xpath(f'//*[@id="main"]/div[3]/div[1]/div/div/div/div[{indx}]/div[1]/div[1]/a').get_attribute('href')
            links.append(company_link)
        except NoSuchElementException:
            pass

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div[2]/div/div[1]/h2').text.replace(' Hakkında', '')
            company_email = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div[1]/div/div[4]/div[1]/div/div/div/div[2]/p').text
            company['Name'] = company_name
            company['Email'] = company_email
            companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
