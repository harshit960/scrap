import time
import pandas as pd
import re
import keyboard
from proxymaker import setproxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
# from selenium import webdriver
from zyte_smartproxy_selenium import webdriver
from pathlib import Path


import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"

st = 1

def read_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            api_key = file.readline().strip()
            return api_key
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

file_path = "key.txt"  # Change this to the path of your API key file
    
api_key = read_api_key(file_path)


def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

def dataOut(outList,t):
    u_df=[]
    
    Path(timee).mkdir(parents=True, exist_ok=True)
    for i in outList:
        df = pd.DataFrame(list(i.values()))
        u_df.append(df)

    u_df = pd.concat(u_df,axis=0)
    u_df.to_excel(timee+'/'+str(t)+'-file-'+timee+'.xlsx',index=False)

def read_excel_file(filename):
    # Read the Excel file
    df = pd.read_excel(filename)
    #print(df)
    # Create a dictionary to store the lists
    
    data_list = df.to_dict(orient='records')

    return data_list
    
def out(listt):
    f = open("out.txt", "w+")
    for i in listt:
        f.write(str(i))
    f.close()

def init_uc_browser():
        options: uc.ChromeOptions = uc.ChromeOptions() 
        # options.headless = True
        prefs = {
            "profile.password_manager_enabled": False, 
            "credentials_enable_service": False,
            }
        # setproxy(options)
        options.page_load_strategy = 'none'
        options.add_experimental_option("prefs", prefs)
        driver = uc.Chrome(use_subprocess=True, options=options)
        return driver


options = webdriver.ChromeOptions()
# options.add_argument("--blink-settings=imagesEnabled=false")
# setproxy(options)
#name=input("Enter name: ")
options.page_load_strategy = 'none'
options.add_argument('--disable-blink-features=AutomationControlled')
#userdatadir = f'C:/Users/{name}/AppData/Local/Google/Chrome/User Data'
#options.add_argument(f"--user-data-dir={userdatadir}")
options.add_argument("--window-size=1025,1080")

def resetdriver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--blink-settings=imagesEnabled=false")
    # setproxy(options)
    options.page_load_strategy = 'none'
    options.add_argument('--disable-blink-features=AutomationControlled')
    #userdatadir = f'C:/Users/{name}/AppData/Local/Google/Chrome/User Data'
    #options.add_argument(f"--user-data-dir={userdatadir}")
    options.add_argument("--window-size=1025,1080")
    if st == 2:
        driver =webdriver.Chrome(spm_options={'spm_apikey': api_key},options=options)
    else:
        options.add_argument("--blink-settings=imagesEnabled=false")
        driver =webdriver.Chrome(options=options)
    return driver
driver = resetdriver()
def site1(link):
    i = 1
    listt = []
    blistt = []
    prezzos=[]
    linkk=[]
    outdata = {}
    # link="https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    # link2="https://www.immobiliare.it/search-list/?vrt=43.544699%2C10.304929%3B43.544123%2C10.304704%3B43.544131%2C10.304028%3B43.54648%2C10.304511%3B43.547179%2C10.304414%3B43.547498%2C10.306882%3B43.547397%2C10.309414%3B43.547164%2C10.310519%3B43.546495%2C10.310905%3B43.544893%2C10.305927%3B43.54466%2C10.305283%3B43.544699%2C10.304929&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    
    wait = WebDriverWait(driver, 120)
    driver.get(link)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.nd-list .nd-list--pipe')))

    
    element = driver.find_elements(By.CSS_SELECTOR, ".in-card__title")
    bagina = driver.find_elements(By.CSS_SELECTOR, ".nd-list .nd-list--pipe")
    prezzo = driver.find_elements(By.CSS_SELECTOR,'.in-realEstateListCard__priceOnTop')
    for x in element:
        listt.append(x.text)
        linkk.append(x.get_attribute("href"))
    for q in bagina:
        blistt.append(q.text)
    for p in prezzo:
        prezzos.append(p.text)
    # print(len(prezzos))
    # print(len(listt))
    # print(len(blistt))
    if len(listt)==len(blistt):
        for i in range(len(listt)):
            temolistt = []
            dictt={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:""}
            b = blistt[i].split("\n")
            # temolistt.append(listt[i])
            # temolistt.append(prezzos[i])
            # temolistt.extend(b)
            # print(b)
            # temolistt.append(linkk[i])
            # outdata[i] = temolistt
            dictt[1]=listt[i]
            dictt[2]=b[1]
            dictt[3]=prezzos[i]
            dictt[9]=b[3]
            
            if len(b) >= 5:
                dictt[7]=b[4]
            
            dictt[13]=linkk[i]
            outdata[i]=dictt
    else:
        print(len(listt))
        print(len(blistt))
    # driver.close()
    driver.execute_script("window.stop();")
    return outdata


def site2(link):
    listt = []
    plistt = []
    blistt = []
    total=[]
    linkk=[]
    outdata = {}
    wait = WebDriverWait(driver,120)
    driver.get(link)
    time.sleep(1) 
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='item-detail-char']/span[2]")))

    


    element = driver.find_elements(By.CLASS_NAME, "item-link")
    prezzo = driver.find_elements(
        By.XPATH, "//div[@class='price-row']/span[@class='item-price h2-simulated']"
    )
    piano = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[1]")
    mq = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[2]")
    bagina = driver.find_elements(By.XPATH, "//div[@class='item-detail-char']/span[3]")
    container = driver.find_elements(By.CSS_SELECTOR, ".item-info-container")
    
    for x in element:
        listt.append(x.text)
        linkk.append(x.get_attribute("href"))
    for y in prezzo:
        plistt.append(y.text)
    for r in container:
        rawTxt=r.text
        total.append(rawTxt.split("\n"))
            
    if len(listt)==len(total):
        for i in range(len(listt)):
            templistt = []
            dictt={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:""}
            
            #dictt={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
            #templistt.append(listt[i])
            #templistt.append(plistt[i])
            #templistt.append(pilistt[i])
            #templistt.append(mqlistt[i])
            # #templistt.append(blistt[i])
            # templistt.append(total[i][1])
            # templistt.append(total[i][2])
            pat=r"(\w+)\s+m2(.*)"
            mq=re.search(pat,total[i][2])
            # print(mq)
            # if mq:
            #     templistt.append(mq.group(1))
            #     templistt.append(mq.group(2))
            # templistt.append(linkk[i])
            # outdata[i] = templistt

            dictt[1]=listt[i]
            dictt[3]=total[i][1]
            if mq:
                dictt[2]=mq.group(1)
                dictt[7]=mq.group(2)
                dictt[8]=mq.group(2)
            dictt[13]=linkk[i]
            outdata[i]=dictt

        return outdata
    else:
        
        print(len(listt))
        print(len(blistt))
    driver.execute_script("window.stop();")


def site3(link):
    listt = []
    plistt = []
    pilistt = []
    mqlistt = []
    blistt = []
    linkk=[]
    total = []

    outdata = {}
    k = True
    wait = WebDriverWait(driver, 120)
    driver.get(link)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='grid csaSrpcard__det__cont grid grid--direction-column']")))

    

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
        "//div//p[@class='csaSrpcard__det__feats__text csaSrpcard__det__feats__items tp-s--m tp-w--s c-txt--f0']/span[1]",
    )
    container = driver.find_elements(By.XPATH, "//div[@class='grid csaSrpcard__det__cont grid grid--direction-column']")

    for x in element:
        listt.append(x.text)
        linkk.append(x.get_attribute("href"))
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)
    for r in container:
        rawTxt=r.text
        
        total.append(rawTxt.split("\n"))

    # driver.close()

    # for i in range(len(listt)):
    #     templistt = []
    #     templistt.append(listt[i])
    #     templistt.append(linkk[i])
    #     templistt.append(plistt[i])
    #     templistt.append(pilistt[i])
    #     templistt.append(mqlistt[i])
    #     outdata[i] = templistt

    if len(listt)==len(total):
        for i in range(len(listt)):
            templistt = []
            #dictt={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
            dictt={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:"",13:""}

            # templistt.append(listt[i])
            #templistt.append(plistt[i])
            #templistt.append(pilistt[i])
            #templistt.append(mqlistt[i])
            #templistt.append(blistt[i])
            # templistt.append(str(total[i][0])+" "+str(total[i][1]))
            # templistt.append(total[i][2])
            # templistt.append(linkk[i])
            # outdata[i] = templistt
            dictt[1]=listt[i]
            dictt[2]=total[i][2]
            dictt[3]=str(total[i][0])+" "+str(total[i][1])
            dictt[13]=linkk[i]
            outdata[i]=dictt
        # driver.execute_script("window.stop();")
        
        return outdata
    else:
        
        print(len(listt))
        print(len(blistt))


filename = "./files/input.xlsx"
timee=str(slugify(time.ctime(time.time())))
# Call the function to read the Excel file
result = read_excel_file(filename)
#print(result)
# print(result["Link 1"])



for i in range(len(result)):
    outList = []
    st=1
    outList.append(site1(result[i]["Link 1"]))
    print("site 1 done")
    st=2
    driver.quit()
    driver=resetdriver()
    outList.append(site2(result[i]["Link 2"]))
    print("site 2 done")
    outList.append(site3(result[i]["Link 3"]))
    print("site 3 done")
    st=1
    dataOut(outList,i)  
    driver.quit()
    if i != len(result)-1:
        driver=resetdriver()




