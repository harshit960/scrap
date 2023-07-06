import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
i=1
listt=[]
data ={"name":listt}
while(True):
    driver.get("https://www.immobiliare.it/search-list/?vrt=43.556122%2C10.310873%3B43.556106%2C10.310401%3B43.557031%2C10.310036%3B43.557218%2C10.309381%3B43.557506%2C10.309156%3B43.558384%2C10.308856%3B43.559698%2C10.314488%3B43.559387%2C10.3148%3B43.556091%2C10.31245%3B43.556122%2C10.310873&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1")
    element = driver.find_elements(By.CSS_SELECTOR, '.in-card__title')
    try:
        #print(element[0].text)
        if(element[0].text == ""):
            break
            i += 1
        else:
            for i in element:
                listt.append(i.text)
    except:
        break

print(data)
#time.sleep(10)
driver.close()

