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

data ={"name":listt,"prezzo":plistt,"piano":pilistt,"mq":mqlistt}
k=True
while(k):
    link= "https://www.casa.it/srp/?page="+str(i)+"&tr=vendita&exclude_auction=true&sortType=surface_asc&geopolygon={%22polygon%22:[[43.55615623790824,10.312495672887065],[43.55635061711003,10.312699520772197],[43.559367301940625,10.314759457295635],[43.55970939068563,10.314501965230205],[43.558418772988844,10.30888005513499],[43.5575635291655,10.309169733708599],[43.557097027418095,10.309470141118267],[43.557097027418095,10.310060227101543],[43.556109586806535,10.310489380543926]],%22bbox%22:[[43.56155197165589,10.30314012784312],[43.55426683939984,10.320499384587505]],%22zoom%22:17}&precision=7&propertyTypeGroup=case"
    driver.get(link)
    time.sleep(1)
    element = driver.find_elements(By.XPATH,"//a[@class = 'art-addr__txt art-addr__txt--a c-txt--f0 tp-w--m tp-s--m']")
    prezzo = driver.find_elements(By.XPATH,"//p[@class='c-txt--f0']")
    piano = driver.find_elements(By.XPATH,"//div[@class='grid info-features__feats grid grid--align-flex-end grid--gutters-l']/div[1]")
    mq = driver.find_elements(By.XPATH,"//div[@class='grid info-features__feats grid grid--align-flex-end grid--gutters-l']/div[2]")
    i = i+1                             

    for x in element:
        listt.append(x.text)
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)
    
    
         
    if(len(element) < 30):
        break
    
driver.close()
print(data)
print(len(listt))
print(len(plistt))
print(len(pilistt))
print(len(mqlistt))
#time.sleep(10)


