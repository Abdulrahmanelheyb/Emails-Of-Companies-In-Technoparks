import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('konyateknokent-tarimsal-teknoloji-sektoru')
    companies = []
    links = []

    # you can change link to get other sectors data easy !
    driver.get('https://www.konyateknokent.com.tr/tr-TR/Firm/Sector/tarimsal-teknoloji')
    companies_count = driver.find_elements_by_xpath('/html/body/div/div/section[2]/div/div[2]/div')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'/html/body/div/div/section[2]/div/div[2]/div[{indx}]/div/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div/div/div/div/h1').text
            company_email = driver.find_element_by_xpath('/html/body/div/div/section/div/div/div[2]/div/div[1]/div[2]/a[2]/span').text
            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
