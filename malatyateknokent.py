import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('malatyateknokent')
    companies = []
    links = []

    driver.get('https://www.malatyateknokent.com.tr/Firmalar.jsp?sirket_id=-1')
    companies_count = driver.find_elements_by_xpath('//*[@id="portfolio"]/article')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'//*[@id="portfolio"]/article[{indx}]/div/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_info = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[2]/ul/li')
            for cinfo in company_info:
                if 'Şirket Adı: ' in cinfo.text:
                    company_name = cinfo.text.replace('Şirket Adı: ', '')
                    company['Name'] = company_name

                if 'Email:' in cinfo.text:
                    company_email = cinfo.text
                    if '@' in company_email:
                        company['Email'] = company_email.replace('Email:', '').replace(' ', '')
                        companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
