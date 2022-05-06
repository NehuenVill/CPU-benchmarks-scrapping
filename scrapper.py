from ast import Break
from cgi import print_directory
from logging import exception
from xml.dom.minidom import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pandas as pd

#Defining important variables.

#/html/body/div[2]/div/div[6]/form/div[2]/nav
#/html/body/div[2]/div/div[6]/form/div[2]/nav

Url = 'https://cpu.userbenchmark.com/'

Elements = {
    'Card'      : 'hovertarget',
    'Ranking'   : 'td',
    'Model'     : 'semi-strongs.lighterblacktexts',
    'Price'     : 'div',
    'NextBtn'   : ['/html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[2]/a', '/html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[3]/a'],
}    

driver = webdriver.Chrome()

driver.get(Url)

def GetData():

    Data = []

    element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, Elements['NextBtn'][0]))
    )

    NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][0])

    while NextBtn:

        Cards = driver.find_elements_by_class_name(Elements['Card'])

        print(Cards)

        counter = 1

        for i in Cards:

            try:
                
                Ranking = i.find_element_by_tag_name(Elements['Ranking']).text

            except Exception:

                Ranking = "Not found"

            try:

                PriceCard = driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/form/div[2]/table/tbody/tr[%s]/td[10]' % (counter))
                Price = PriceCard.find_element_by_tag_name(Elements['Price']).text

            except Exception:

                Price = "Not found"

            try:

                Brand = i.find_element_by_class_name(Elements['Model']).text
                
                if 'Compare' in Brand:

                    Brand = Brand.replace('Compare', '')
                    Brand = Brand.replace('\n', '')

            except Exception:

                Brand = 'Not found'

            OutPut = {

                'Ranking': Ranking,
                'Brand and Model': Brand,
                'Price': Price,

            }

            print("")

            Data.append(OutPut)

            print(OutPut)

            print("")

            counter += 1

            time.sleep(0.05)

        try:

            NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][0])
                
            if NextBtn.get_attribute('href'):

                NextBtn.click()

            else:

                NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][1])
                NextBtn.click()

            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, Elements['NextBtn'][1]))
            )

            NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][1])

        except Exception:

            break

    return Data        


def Save(OP):

    df = pd.DataFrame(OP, columns=['Ranking', 'Brand and Model', 'Price'])
    df.to_excel('CPUs.xls', index=False, columns=['Ranking', 'Brand and Model', 'Price'])



Save(GetData())