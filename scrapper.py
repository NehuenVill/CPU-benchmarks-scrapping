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
    'Ranking': '/html/body/div[2]/div/div[6]/form/div[2]/table/tbody/tr[2]/td[1]/div',
    'Model'  : 'semi-strongs lighterblacktexts',
    'Price'  : 'mh-tc pybg spybr',
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
        
        print("")

        grr = Cards[0].find_element_by_class_name(Elements['Price'])

        print(grr)
        print("")

        for i in Cards:

            try:
                
                Ranking = i.find_element_by_xpath(Elements['Ranking']).text

                print(Ranking)

            except Exception:

                Ranking = "Not found."

            try:

                Price = i.find_element_by_class_name(Elements['Price']).text
                print(Price)

            except Exception:

                Price = "Not found."

            OutPut = {

                'Ranking': Ranking,
                'Brand and Model': i.find_element_by_class_name(Elements['Model']).text,
                'Price': Price,

            }

            Data.append(OutPut)

            time.sleep(0.06)

        NextBtn.click()

        time.sleep(0.5)

        NextBtn = driver.find_element_by_xpath(Elements['NextBtn'][1])

    return Data        


def Save(OP):

    df = pd.DataFrame(OP, columns=['Ranking', 'Brand and Model', 'Price'])
    df.to_excel('Cars List.xls', index=False, columns=['Ranking', 'Brand and Model', 'Price'])



Save(GetData())