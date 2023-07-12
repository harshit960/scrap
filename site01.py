import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.ChromeOptions()
driver.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=driver)
#driver.implicitly_wait(3)


i=1
listt=[]
plistt=[]
pilistt=[]
mqlistt=[]
blistt=[]
data ={"name":listt,"prezzo":plistt,"piano":pilistt,"mq":mqlistt,"bagina":blistt}
k=True
while(k):
    link="https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    link2="https://www.immobiliare.it/search-list/?vrt=43.544699%2C10.304929%3B43.544123%2C10.304704%3B43.544131%2C10.304028%3B43.54648%2C10.304511%3B43.547179%2C10.304414%3B43.547498%2C10.306882%3B43.547397%2C10.309414%3B43.547164%2C10.310519%3B43.546495%2C10.310905%3B43.544893%2C10.305927%3B43.54466%2C10.305283%3B43.544699%2C10.304929&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    driver.get(link2)
    time.sleep(1)
    element = driver.find_elements(By.CSS_SELECTOR, '.in-card__title')
    prezzo = driver.find_elements(By.CLASS_NAME,'in-realEstateListCard__features--main')
    piano = driver.find_elements(By.CSS_SELECTOR,"li[aria-label='piano'] div[class='in-feat__data']")
    mq = driver.find_elements(By.CSS_SELECTOR,"li[aria-label='superficie'] div[class='in-feat__data']")
    bagina =driver.find_elements(By.CSS_SELECTOR,".nd-list .nd-list--pipe")
    i += 1     
    #for j in range(len(element)):
    #    temp_list=[]
        
        #print(element[0].text)
    for x in element:
        listt.append(x.text)
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)
    for q in bagina:
        blistt.append(q.text)
    
        
        
    if(len(element) < 25 ):
        break
    
driver.close()
#print(data)
print(len(listt))
print(len(plistt))
print(len(pilistt))
print(len(mqlistt))
print(len(blistt))

print(blistt)

#time.sleep(10)


#dis={1:[Appartamento via dei Carrozzieri,€ 90.000,T,]}



link3="https://www.immobiliare.it/search-list/?vrt=43.557941%2C10.316151%3B43.55941%2C10.315325%3B43.559387%2C10.314724%3B43.55962%2C10.314521%3B43.559994%2C10.3148%3B43.560444%2C10.314928%3B43.560685%2C10.315711%3B43.561152%2C10.318061%3B43.561245%2C10.31878%3B43.560312%2C10.318898%3B43.560071%2C10.318&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)