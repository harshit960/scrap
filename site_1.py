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
    # link="https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    link2= "https://www.idealista.it/aree/vendita-case/con-aste_no/lista-"+str(i)+"?ordine=area-asc&shape=%28%28%7DnzhGul%7C%7D%40cGqb%40%7C%40%7B%40vOhJdAh%40h%40h%40FjLsDbAAbCsGzB%29%29"
    driver.get(link2)
    time.sleep(1)
    element = driver.find_elements(By.CLASS_NAME, 'item-link')
    prezzo = driver.find_elements(By.XPATH,"//div[@class='price-row']/span[@class='item-price h2-simulated']")
    piano = driver.find_elements(By.XPATH,"//div[@class='item-detail-char']/span[1]")
    mq = driver.find_elements(By.XPATH,"//div[@class='item-detail-char']/span[2]")
    bagina =driver.find_elements(By.XPATH,"//div[@class='item-detail-char']/span[3]")
    i = i+1                                       
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
    
         
    if(len(element) < 30):
        break
    
driver.close()
print(data)
print(len(listt))
print(len(plistt))
print(len(pilistt))
print(len(mqlistt))
print(len(blistt))

#time.sleep(10)


