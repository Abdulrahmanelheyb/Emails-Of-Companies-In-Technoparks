import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('kirikkaleteknopark')
    companies = []
    links = []

    driver.get('https://www.kirikkaleteknopark.com/firma-rehberi/')
    companies_count = driver.find_elements_by_xpath('//*[@id="content"]/article/div/div/div/div/div/div/div/article')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'//*[@id="content"]/article/div/div/div/div/div/div/div/article[{indx}]/div/a').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/h1').text
            company_info_elements = driver.find_elements_by_xpath('//*[@id="content"]/article/div[1]/div[2]/div[2]/p')
            if len(company_info_elements) > 0:
                for comp_info_element in company_info_elements:
                    if '\n' in comp_info_element.text:
                        company_info_list = comp_info_element.text.split('\n')
                        if len(company_info_list) > 0:
                            for comp_info in company_info_list:
                                if 'Eposta:' in comp_info:
                                    company_email = comp_info.replace('Eposta:', '').replace('•', '')
                                    company['Name'] = company_name
                                    company['Email'] = company_email
                                    companies.append(company)

        except NoSuchElementException:
            pass

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/h1').text
            company_info = driver.find_elements_by_xpath('//*[@id="content"]/article/div[1]/div[2]/div[2]/ul/li')
            if len(company_info) > 0:
                for comp_info in company_info:
                    if 'E-Posta: ' in comp_info.text:
                        company_email = comp_info.text.replace('E-Posta: ', '')
                        company['Name'] = company_name
                        company['Email'] = company_email
                        companies.append(company)
        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
