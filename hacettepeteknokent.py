import time
import base
from selenium.common.exceptions import *
import pytesseract
import os
import cv2


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path('hacettepeteknokent')
    companies = []

    driver.get('https://www.hacettepeteknokent.com.tr/#!firma-rehberi')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="allcompanies"]').click()
    companies_count = driver.find_elements_by_xpath('//*[@id="firma-rehberi"]/div/div/div[4]/div[2]/div')
    for indx in range(1, len(companies_count)):
        company = {}

        try:
            driver.find_element_by_xpath(f'//*[@id="firma-rehberi"]/div/div/div[4]/div[2]/div[{indx}]').click()
            company_name = driver.find_element_by_xpath('//*[@id="firma-rehberi"]/div/div/div[5]/div/div/h4').text
            driver.find_element_by_xpath('//*[@id="firma-rehberi"]/div/div/div[5]/div/div/div[4]/img').screenshot(f'company-email-{indx}.png')
            img = cv2.imread(f'company-email-{indx}.png')
            company_email = str(pytesseract.image_to_string(img, config='--psm 7 --oem 2').replace('\n\f', '').replace(' ', ''))
            company['Name'] = company_name
            company['Email'] = company_email
            companies.append(company)

        except Exception as ex:
            print(ex)
        except NoSuchElementException:
            pass
        finally:
            try:
                os.remove(f'company-email-{indx}.png')
            except FileNotFoundError:
                pass

    base.write_data(filename, companies)
    driver.close()
