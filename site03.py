import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = uc.ChromeOptions()
PROXY = "158.255.196.165:8080"

# driver.add_argument('--proxy-server=%s' % PROXY)

# driver.add_argument("--disable-dev-shm-usage")
# driver.add_argument("--no-sandbox")
# driver.add_argument("--window-size=1920,1080")
# driver.add_argument(f'user-agent={user_agent}')
driver.add_argument("--blink-settings=imagesEnabled=false")
driver = uc.Chrome(headless=False, options=driver)

# driver.execute_cdp_cmd("Network.setUserAgentOverride", USER_AGENT)
# driver.implicitly_wait(3)


i = 1
listt = []
plistt = []
pilistt = []
mqlistt = []
linkk=[]
outdata = {}
data = {"name": listt, "prezzo": plistt, "piano": pilistt, "mq": mqlistt}
k = True
while k:
    link = (
        "https://www.casa.it/srp/?page="
        + str(i)
        + "&tr=vendita&exclude_auction=true&sortType=surface_asc&geopolygon={%22polygon%22:[[43.55615623790824,10.312495672887065],[43.55635061711003,10.312699520772197],[43.559367301940625,10.314759457295635],[43.55970939068563,10.314501965230205],[43.558418772988844,10.30888005513499],[43.5575635291655,10.309169733708599],[43.557097027418095,10.309470141118267],[43.557097027418095,10.310060227101543],[43.556109586806535,10.310489380543926]],%22bbox%22:[[43.56155197165589,10.30314012784312],[43.55426683939984,10.320499384587505]],%22zoom%22:17}&precision=7&propertyTypeGroup=case"
    )
    driver.get(link)
    # time.sleep(25)
    element = driver.find_elements(
        By.XPATH,
        "//a[@class='csaSrpcard__det__title--a c-txt--f0']",
    )
    prezzo = driver.find_elements(By.XPATH, "//div//span[@class='csaSrpcard__det__feats--price tp-w--l']")
    piano = driver.find_elements(
        By.XPATH,
        "//div[@class='grid info-features__feats grid grid--align-flex-end grid--gutters-l']/div[1]",
    )
    mq = driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'grid-item grid-item grid-item--behavior-fixed')]/p[@class='csaSrpcard__det__feats__text csaSrpcard__det__feats__items tp-s--m tp-w--s c-txt--f0']",
    )
    i = i + 1

    for x in element:
        listt.append(x.text)
        linkk.append(x.get_attribute("href"))
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)
    for i in range(10):
        driver.execute_script("window.scrollBy(0,400)", "")
        time.sleep(0.1)
    time.sleep(3)
    if len(element) < 20:
        break

driver.close()
# print(data)
# print(len(listt))
# print(len(plistt))
# print(len(pilistt))
# print(len(mqlistt))
# # time.sleep(10)
for i in range(len(listt)):
    templistt = []
    templistt.append(listt[i])
    templistt.append(plistt[i])
    templistt.append(pilistt[i])
    templistt.append(mqlistt[i])
    templistt.append(linkk[i])
    # templistt.append(blistt[i])
    outdata[i] = templistt

print(outdata)
