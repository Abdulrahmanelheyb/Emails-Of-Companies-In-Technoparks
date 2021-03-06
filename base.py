import os
from selenium.webdriver import Edge
from xlsxwriter import Workbook
import pytesseract
from win10toast import ToastNotifier

"""
import base
from selenium.common.exceptions import *


def exceute():
    driver = base.get_driver()
    filename = base.get_file_path(f'{__name__}')
    companies = []
    links = []
    
    driver.get('')
    companies_count = driver.find_elements_by_xpath('')
    for indx in range(1, len(companies_count) + 1):
        company_link = driver.find_element_by_xpath(f'').get_attribute('href')
        links.append(company_link)

    for link in links:
        company = {}
        
        try:
            driver.get(link)
            company_name = driver.find_element_by_xpath('').text
            company_email = driver.find_element_by_xpath('').text
            
            if '@' in company_email:
                company['Name'] = company_name
                company['Email'] = company_email
                companies.append(company)
            
        except NoSuchElementException:
            pass
    
    base.write_data(filename, companies)
    driver.close()
    return [True, __name__]

"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\abdul\AppData\Local\Tesseract-OCR\tesseract.exe'
trueMsg = "Successfuly"
falseMsg = "Failed"


def get_file_path(filename) -> str:
    outputfilename = f'data/{filename}.xlsx'
    return outputfilename


def notify(status: bool, filename: str, duration: int = 3):
    notifier = ToastNotifier()
    if status:
        msg = f'{filename} Scraping is successfully completed.'
    else:
        msg = f'{filename} Scraping is failed complete!'

    notifier.show_toast('Data scraping', msg, duration=duration)


def kill_web_driver_edge():
    try:
        os.system('taskkill /f /im MicrosoftWebDriver.exe')
    except Exception as ex:
        print(ex)


def get_driver():
    return Edge('C:\\DevSoftwares\\WebDrivers\\MicrosoftWebDriver.exe')


def write_data(filename, companyies):
    row = 0
    workbook = Workbook(filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(row, 0, "Firma Adi")
    worksheet.write(row, 1, "Firma Mail")

    worksheet.set_column("A:B", 100)

    for company in companyies:
        if "Name" in company:
            worksheet.write(row, 0, company["Name"])
        if "Email" in company:
            worksheet.write(row, 1, company["Email"])

        row += 1

    if not os.path.exists('data'):
        os.mkdir('data')

    if os.path.exists(filename):
        os.remove(filename)

    workbook.close()
