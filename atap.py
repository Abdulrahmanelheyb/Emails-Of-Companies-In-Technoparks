import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('atap')
    companies = []
    links = []

    driver.get('https://www.atap.com.tr/portal/firmalar')
    companies_count = driver.find_elements_by_xpath('//*[@id="contentWrapper"]/div[2]/div/div[2]/div/div/div')
    for indx in range(1, len(companies_count)):
        company_link = driver.find_element_by_xpath(f'//*[@id="contentWrapper"]/div[2]/div/div[2]/div/div/div[{indx}]/article/div/div/h2/a')\
            .get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div[3]/div[2]/div[1]/div/span/span').text

            infos_count = driver.find_elements_by_xpath('//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div[3]/div[2]/div')
            for indx in range(1, len(infos_count)):
                element: str = driver.find_element_by_xpath(f'//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div[3]/div[2]/div[{indx}]/div/span/a').text
                if element.startswith("E-Posta"):
                    company_email_alltext: str = driver.find_element_by_xpath(f'//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div[3]/div[2]/div[{indx}]'
                                                                              '/div/span/span').text
                    comapny_email_domain = driver.find_element_by_xpath(f'//*[@id="contentWrapper"]/div[2]/div/div/div[1]/div[3]/div[2]/div[{indx}]/div'
                                                                        '/span/span/i').text
                    comapmny_email_subdomain = company_email_alltext.replace(f'{comapny_email_domain}', '')
                    company_email = f'{comapmny_email_subdomain}@{comapny_email_domain}'

                    company['Name'] = company_name
                    company['Email'] = company_email
                    companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
