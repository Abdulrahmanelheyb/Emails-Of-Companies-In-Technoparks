import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    pagelinks = []

    driver.get('https://www.trabzonteknokent.com.tr/sirketler/?page=1')
    pages_count = driver.find_elements_by_xpath('/html/body/div[1]/div/section/div/div[2]/div')
    for indx in range(1, len(pages_count)):
        if indx == 1:
            continue
        page = driver.find_element_by_xpath(f'/html/body/div[1]/div/section/div/div[2]/div[{indx}]/a').get_attribute('href')
        pagelinks.append(page)

    for pagelink in pagelinks:
        links = []
        driver.get(pagelink)
        companies_count = driver.find_elements_by_xpath('/html/body/div[1]/div/section/div/div[1]/div')

        for indx in range(1, len(companies_count) + 1):
            company_link = driver.find_element_by_xpath(f'/html/body/div[1]/div/section/div/div[1]/div[{indx}]/a').get_attribute('href')
            links.append(company_link)

        for link in links:
            company = {}
            try:
                driver.get(link)
                company_name = driver.find_element_by_xpath('/html/body/div[1]/section[3]/div/div/div/article/h3').text
                company_email = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[1]/div/div[2]/div/p').text

                if '@' in company_email:
                    company['Name'] = company_name
                    company['Email'] = company_email
                    companies.append(company)

            except NoSuchElementException:
                pass

    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]
