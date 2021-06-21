import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('gaziantepteknopark')
    companies = []

    driver.get('https://www.gaziantepteknopark.com.tr/firmalar.php')
    # companies_count = driver.find_elements_by_xpath('')
    # for indx in range(1, len(companies_count)):
    #     company_link = driver.find_element_by_xpath(f'').get_attribute('href')
    #     links.append(company_link)

    companies_elements = driver.find_elements_by_xpath('/html/body/section[2]/div/div[2]/div[4]/div')
    for indx in range(1, len(companies_elements)):
        company = {}
        try:
            company_name = driver.find_element_by_xpath(f'/html/body/section[2]/div/div[2]/div[4]/div[{indx}]/div/div/div/a[1]/h6').get_attribute('innerText')
            company_email = driver.find_element_by_xpath(f'/html/body/section[2]/div/div[2]/div[4]/div[{indx}]/div/div/div/a[1]/p').get_attribute('innerText')
            company_email = company_email.replace('➥ ', '')

            company['Name'] = company_name
            company['Email'] = company_email
            companies.append(company)

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
