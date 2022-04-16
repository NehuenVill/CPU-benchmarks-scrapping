from xml.dom.minidom import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pandas as pd

#Defining important variables.


#initial xpath = /html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[2]/a
#Second xpath  = /html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[3]/a


Url = 'https://cpu.userbenchmark.com/'

Elements = {
    'Card'   : 'hovertarget',
    'Ranking': 'td',
    'Model'  : "//tr[@class='hovertarget']/td[2]/div/div[2]/span",
    'Price'  : "//tr[@class='hovertarget']td[10]/div[1]",
    'NextBtn': ['/html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[2]/a', '/html/body/div[2]/div/div[6]/form/div[2]/nav/ul/li[3]/a'],
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

        for i in Cards:

            try:
                
                Ranking = i.find_element_by_tag_name(Elements['Ranking']).text

            except Exception:

                Ranking = "Not found"

            finally:
                print(Ranking)

            try:

                Price = i.find_element_by_xpath(Elements['Price']).text

            except Exception:

                Price = "Not found"

            finally:
                print(Price)

            try:

                Brand = i.find_element_by_xpath(Elements['Model']).text

            except Exception:

                Brand = 'Not found'

            finally:
                print(Brand)

            OutPut = {

                'Ranking': Ranking,
                'Brand and Model': Brand,
                'Price': Price,

            }

            Data.append(OutPut)

            time.sleep(0.06)

        NextBtn.click()

        time.sleep(0.8)

        NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][1])

    return Data        


def Save(OP):

    df = pd.DataFrame(OP, columns=['Ranking', 'Brand and Model', 'Price'])
    df.to_excel('CPUs.xls', index=False, columns=['Ranking', 'Brand and Model', 'Price'])



Save(GetData())