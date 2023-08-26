from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
from selenium.webdriver.common.by import By

def site2(link):
    options = Options()
    options.add_argument('--proxy-server=socks5://127.0.0.1:9050')  # Use Tor's SOCKS proxy

    # Initialize the WebDriver with Chrome
    driver = webdriver.Chrome(options=options)

    # Example usage: open a website

    listt = []
    plistt = []
    blistt = []
    total=[]
    linkk=[]
    outdata = {}
    driver.get(link)
    time.sleep(1)
    input("Press Enter")
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

    # Do your automation tasks here

    # Close the browser when done
    driver.quit()
