import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('firatteknokent')
    companies = []
    links = []

    driver.get('https://www.firatteknokent.com.tr/firmalar')

    for indx in range(1, len(driver.find_elements_by_xpath('//*[@id="zc-map"]/area'))):
        lnk = driver.find_element_by_xpath(f'//*[@id="zc-map"]/area[{indx}]').get_attribute('href')
        if "http" in lnk:
            links.append(lnk)

    for link in links:
        company = {}
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div/div/h4/a').text
            company_infos = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div/div/div/div/p')
            for compinfo in company_infos:
                if 'E-Posta:' in compinfo.text:
                    if len(compinfo.text) > 9:
                        company_email = compinfo.text.replace('E-Posta: ', '')
                        company['Name'] = company_name
                        company['Email'] = company_email
                        companies.append(company)
                        break

        except NoSuchElementException:
            pass

    base.write_data(filename, companies)
    driver.close()
