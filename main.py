import time
import pandas as pd
import re
import math
from proxymaker import setproxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
# from selenium import webdriver
from zyte_smartproxy_selenium import webdriver
from pathlib import Path


import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()  

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
    
    p_no=1
    wait = WebDriverWait(driver, 120)
    newLink = link+"&pag=1" 
    outdata = {}
    # Original URL
    # You can modify the 'pag' parameter in the URL to change the page number
    

    
    driver.get(newLink)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.nd-list .nd-list--pipe')))
    itemss= driver.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div[1]/div[1]/div[1]')
    print(itemss.text[0:2])
    if int(itemss.text[0:2])%25 != 0:
        noOfPage=  int(int(itemss.text[0:2])/25)+1
    else:
        noOfPage= int(int(itemss.text[0:2])/25)
    print(noOfPage)

    for page in range(noOfPage):
        listt = []
        blistt = []
        prezzos=[]
        linkk=[]
        
        new_page_number = page+1
        url_parts = newLink.split('&pag=')
        new_url = url_parts[0] + f'&pag={new_page_number}' + '&' + url_parts[1] if len(url_parts) > 1 else ''


        driver.get(new_url)
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.nd-list .nd-list--pipe')))

        

        element = driver.find_elements(By.CSS_SELECTOR, ".in-reListCard__title")
        bagina = driver.find_elements(By.CSS_SELECTOR, ".nd-list .nd-list--pipe")
        prezzo = driver.find_elements(By.CSS_SELECTOR,'.in-reListCardPrice')
        for x in element:
            # print(x.text)
            listt.append(x.text)
            linkk.append(x.get_attribute("href"))
        for q in bagina:
            blistt.append(q.text)
        for p in prezzo:
            prezzos.append(p.text)
        print(len(prezzos))
        print(len(listt))
        print(len(blistt))
        print(len(linkk))
        temodict = {}
        if len(listt)==len(blistt):
            for i in range(len(listt)):
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
                dictt[3]=prezzos[i].replace('.000','').replace('€','')
                if len(b)>=4 :
                    dictt[9]=b[3]
                
                if len(b) >= 5:
                    dictt[7]=b[4]
                
                dictt[13]=linkk[i]
                temodict[i+(page*25)]=dictt
                
                
        else:
            print(len(listt))
            print(len(blistt))
        
        outdata.update(temodict)
    # driver.close()
    driver.execute_script("window.stop();")
    return outdata


def site2(link):
    outdata = {}
    wait = WebDriverWait(driver,120)
    # link = link.replace('/con-aste_no/', '/con-aste_no/lista-'+ str(n) )
    driver.get(link)
    time.sleep(1) 
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='item-detail-char']/span[2]")))
    totalItems = driver.find_element(By.XPATH,'//*[@id="h1-container"]')
    print(totalItems.text.split()[0])
    
    if int(totalItems.text.split()[0])%30 != 0:
        noOfPage=  int(int(totalItems.text.split()[0])/30)+1
    else:
        noOfPage= int(int(totalItems.text.split()[0])/30)
    print(noOfPage)

    for l in range(noOfPage):
        listt = []
        plistt = []
        blistt = []
        total=[]
        linkk=[]
        wait = WebDriverWait(driver,120)
        nlink = link.replace('/con-aste_no/', '/con-aste_no/lista-'+ str(l + 1) )
        driver.get(nlink)
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
            t=rawTxt.find('%')
            e=rawTxt.find('€')
            if t != -1:
                r1=rawTxt[:e+1]
                r2=rawTxt[t+1:]
                rawTxt = r1 + r2
                
                # print("1:" + rawTxt)
            # else:
                # print("2:" + rawTxt)
            total.append(rawTxt.split("\n"))
        tempDist ={}
        print(len(listt))
        print(len(total))
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
                print(total[i][2])
                pat=r"(\w+)\s+m2(.*)"
                mq=re.search(pat,total[i][2])
                # print(mq)
                # if mq:
                #     templistt.append(mq.group(1))
                #     templistt.append(mq.group(2))
                # templistt.append(linkk[i])
                # outdata[i] = templistt

                dictt[1]=listt[i]
                dictt[3]=total[i][1].replace('.000€','')
                if mq:
                    dictt[2]=mq.group(1)
                    dictt[7]=mq.group(2)
                    dictt[8]=mq.group(2)
                dictt[13]=linkk[i]
                tempDist[i+(l*30)]=dictt

            # return outdata
            outdata.update(tempDist)
        else:
        
            print(len(listt))
            print(len(blistt))

    driver.execute_script("window.stop();")
    return outdata


def site3(link):


    outdata = {}
    wait = WebDriverWait(driver, 120)
    driver.get(link)
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='grid csaSrpcard__det__cont grid grid--direction-column']")))
    
    totalItems = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[1]/h1')
    print(totalItems.get_attribute('data-count'))
    
    if int(totalItems.get_attribute('data-count'))%20 != 0:
        noOfPage=  int(int(totalItems.get_attribute('data-count'))/20)+1
    else:
        noOfPage= int(int(totalItems.get_attribute('data-count'))/20)
    print(noOfPage)

    for l in range(noOfPage):


        listt = []
        plistt = []
        pilistt = []
        mqlistt = []
        blistt = []
        floorlist = []
        elevatlist = []
        linkk=[]
        total = []

        k = True
        wait = WebDriverWait(driver, 120)
        nlink = link + "&page=" + str(l+1)
        driver.get(nlink)
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
            "//div//p[@class='csaSrpcard__det__feats__text csaSrpcard__det__feats__items tp-s--m tp-w--s c-txt--f0']/span[1]/font[1]/font[@style='vertical-align: inherit;']",
        )
        elevator = driver.find_elements(
            By.XPATH,
            "//div//p[@class='csaSrpcard__det__feats__text csaSrpcard__det__feats__items tp-s--m tp-w--s c-txt--f0']/span[3]"
        )

        floor = driver.find_elements(
            By.XPATH,
            "//div//p[@class='csaSrpcard__det__feats__text csaSrpcard__det__feats__items tp-s--m tp-w--s c-txt--f0']/span[4]"
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
        for a in elevator:
            elevatlist.append(a.text)
        for o in floor:
            floorlist.append(o.text)
        for r in container:
            rawTxt=r.text
            # print(rawTxt)
            total.append(rawTxt.split("\n"))
        tempDict={}

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
                priccc=total[i][4].split()
                dictt[2]=priccc[0]
                dictt[3]=math.trunc(float(total[i][3]))
                dictt[7]=str(total[i][7])
                dictt[9]=str(total[i][6])
                dictt[13]=linkk[i]
                tempDict[i+(l*25)]=dictt

            outdata.update(tempDict)
            # driver.execute_script("window.stop();")
            
        else:
        
            print(len(listt))
            print(len(blistt))
        
    return outdata


filename = "./files/input.xlsx"
timee=str(slugify(time.ctime(time.time())))
# Call the function to read the Excel file
result = read_excel_file(filename)
#print(result)
# print(result["Link 1"])



for i in range(len(result)):
    outList = []
    st=1
    try:
        # outList.append(site1(result[i]["Link 1"]))
        print("site 1 done")
    except Exception as e:
        print("missing1")
        print(e)
    
    st=2
    driver.quit()
    driver=resetdriver()
    
    outList.append(site2(result[i]["Link 2"]))
    print("site 2 done")
        
    # except Exception as e:
    #     print("missing2")
    #     print(e)

    try:
        # outList.append(site3(result[i]["Link 3"]))
        print("site 3 done")
    except Exception as e:
        print("")
        print("missing3")
        print(e)

    st=1
    dataOut(outList,i)  
    driver.quit()
    if i != len(result)-1:
        driver=resetdriver()




