import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = uc.ChromeOptions()
driver.add_argument("--blink-settings=imagesEnabled=false")
driver = uc.Chrome(options=driver)


def site1(link):
    i = 1
    listt = []
    blistt = []
    outdata = {}
    k = True

    # link="https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    # link2="https://www.immobiliare.it/search-list/?vrt=43.544699%2C10.304929%3B43.544123%2C10.304704%3B43.544131%2C10.304028%3B43.54648%2C10.304511%3B43.547179%2C10.304414%3B43.547498%2C10.306882%3B43.547397%2C10.309414%3B43.547164%2C10.310519%3B43.546495%2C10.310905%3B43.544893%2C10.305927%3B43.54466%2C10.305283%3B43.544699%2C10.304929&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    driver.get(link)
    time.sleep(1)
    element = driver.find_elements(By.CSS_SELECTOR, ".in-card__title")
    bagina = driver.find_elements(By.CSS_SELECTOR, ".nd-list .nd-list--pipe")

    for x in element:
        listt.append(x.text)
    for q in bagina:
        blistt.append(q.text)

    for i in range(len(listt)):
        temolistt = []
        temolistt.append(listt[i])

        b = blistt[i].split("\n")
        temolistt.extend(b)
        outdata[i] = temolistt

    # driver.close()
    return outdata


def site2(link):
    listt = []
    plistt = []
    pilistt = []
    mqlistt = []
    blistt = []

    outdata = {}
    k = True
    driver.get(link)
    time.sleep(1)
    element = driver.find_elements(By.CLASS_NAME, "item-link")
    prezzo = driver.find_elements(
        By.XPATH, "//div[@class='price-row']/span[@class='item-price h2-simulated']"
    )
    piano = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[1]")
    mq = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[2]")
    bagina = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[3]")

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

    # driver.close()

    for i in range(len(listt)):
        templistt = []
        templistt.append(listt[i])
        templistt.append(plistt[i])
        templistt.append(pilistt[i])
        templistt.append(mqlistt[i])
        templistt.append(blistt[i])
        outdata[i] = templistt
    return outdata


def site3(link):
    listt = []
    plistt = []
    pilistt = []
    mqlistt = []
    blistt = []

    outdata = {}
    k = True
    driver.get(link)
    time.sleep(1)
    element = driver.find_elements(
        By.XPATH,
        "//a[@class = 'art-addr__txt art-addr__txt--a c-txt--f0 tp-w--m tp-s--m']",
    )
    prezzo = driver.find_elements(By.XPATH, "//p[@class='c-txt--f0']")
    piano = driver.find_elements(
        By.XPATH,
        "//div[@class='grid info-features__feats grid grid--align-flex-end grid--gutters-l']/div[1]",
    )
    mq = driver.find_elements(
        By.XPATH,
        "//div[@class='grid info-features__feats grid grid--align-flex-end grid--gutters-l']/div[2]",
    )
    for x in element:
        listt.append(x.text)
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)

    # driver.close()

    for i in range(len(listt)):
        templistt = []
        templistt.append(listt[i])
        templistt.append(plistt[i])
        templistt.append(pilistt[i])
        templistt.append(mqlistt[i])
        templistt.append(blistt[i])
        outdata[i] = templistt
    return outdata


link1 = (
    "https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="
    + "1"
    + "&slau=1"
)
link2 = (
    "https://www.idealista.it/aree/vendita-case/con-aste_no/lista-"
    + "1"
    + "?ordine=area-asc&shape=%28%28%7DnzhGul%7C%7D%40cGqb%40%7C%40%7B%40vOhJdAh%40h%40h%40FjLsDbAAbCsGzB%29%29"
)

link3 = (
    "https://www.casa.it/srp/?page="
    + "1"
    + "&tr=vendita&exclude_auction=true&sortType=surface_asc&geopolygon={%22polygon%22:[[43.55615623790824,10.312495672887065],[43.55635061711003,10.312699520772197],[43.559367301940625,10.314759457295635],[43.55970939068563,10.314501965230205],[43.558418772988844,10.30888005513499],[43.5575635291655,10.309169733708599],[43.557097027418095,10.309470141118267],[43.557097027418095,10.310060227101543],[43.556109586806535,10.310489380543926]],%22bbox%22:[[43.56155197165589,10.30314012784312],[43.55426683939984,10.320499384587505]],%22zoom%22:17}&precision=7&propertyTypeGroup=case"
)
print(site1(link1))
print(site2(link2))
print(site3(link3))
