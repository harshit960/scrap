import time
import pandas as pd
from proxymaker import setproxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


def read_excel_file(filename):
    # Read the Excel file
    df = pd.read_excel(filename)

    # Create a dictionary to store the lists
    column_lists = {}

    # Iterate over the columns
    for column in df.columns:
        # Get the column data as a list
        column_data = df[column].tolist()
        # Add the list to the dictionary using the column name as the key
        column_lists[column] = column_data

    return column_lists


def out(listt):
    f = open("out.txt", "w+")
    for i in listt:
        f.write(str(i))
    f.close()


options = uc.ChromeOptions()
options.add_argument("--blink-settings=imagesEnabled=false")
setproxy(options)
driver = uc.Chrome(options=options)


def site1(link):
    i = 1
    listt = []
    blistt = []
    prezzos=[]
    linkk=[]
    outdata = {}
    # link="https://www.immobiliare.it/search-list/?vrt=43.54805%2C10.311828%3B43.548385%2C10.311527%3B43.547864%2C10.310111%3B43.547693%2C10.310959%3B43.547374%2C10.311184%3B43.547125%2C10.31054%3B43.546518%2C10.310873%3B43.547047%2C10.312589%3B43.547856%2C10.312032%3B43.54805%2C10.311828&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    # link2="https://www.immobiliare.it/search-list/?vrt=43.544699%2C10.304929%3B43.544123%2C10.304704%3B43.544131%2C10.304028%3B43.54648%2C10.304511%3B43.547179%2C10.304414%3B43.547498%2C10.306882%3B43.547397%2C10.309414%3B43.547164%2C10.310519%3B43.546495%2C10.310905%3B43.544893%2C10.305927%3B43.54466%2C10.305283%3B43.544699%2C10.304929&idContratto=1&idCategoria=1&tipoProprieta=1&criterio=superficie&ordine=asc&noAste=1&__lang=it&pag="+str(i)+"&slau=1"
    driver.get(link)
    time.sleep(1)
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
            dictt={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
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
            dictt[7]=b[3]
            dictt[9]=b[-1]
            dictt[13]=linkk[i]
            outdata[i]=dictt
    # driver.close()
    
    return outdata


def site2(link):
    listt = []
    plistt = []
    pilistt = []
    mqlistt = []
    blistt = []
    total=[]
    linkk=[]
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
    container = driver.find_elements(By.CSS_SELECTOR, ".item-info-container")
    
    for x in element:
        listt.append(x.text)
        linkk.append(x.get_attribute("href"))
    for y in prezzo:
        plistt.append(y.text)
    for z in piano:
        pilistt.append(z.text)
    for p in mq:
        mqlistt.append(p.text)
    for q in bagina:
        blistt.append(q.text)
    for r in container:
        rawTxt=r.text
        
        total.append(rawTxt.split("\n"))
    #print(total)
    # driver.close()
    #print(len(listt))
    #print(blistt)
    if len(listt)==len(total):
        for i in range(len(listt)):
            templistt = []
            templistt.append(listt[i])
            #templistt.append(plistt[i])
            #templistt.append(pilistt[i])
            #templistt.append(mqlistt[i])
            #templistt.append(blistt[i])
            templistt.append(total[i][1])
            templistt.append(total[i][2])
            templistt.append(linkk[i])
            outdata[i] = templistt
    return outdata


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
    container = driver.find_elements(By.XPATH, "//div[@class='art-infos is-clickable']")

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
            dictt={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}

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
            dictt[8]=linkk[i]
            outdata[i]=dictt
    return outdata


filename = "./files/input.xlsx"

# Call the function to read the Excel file
result = read_excel_file(filename)

# print(result["Link 1"])
outList = []

for i in range(len(result["Link 1"])):
    outList.append(site1(result["Link 1"][i]))
    print("site 1 done")
for i in range(len(result["Link 2"])):
    outList.append(site2(result["Link 2"][i]))
    print("site 2 done")
for i in range(len(result["Link 3"])):
    outList.append(site3(result["Link 3"][i]))
    print("site 3 done")



u_df=[]
for i in outList:
    df = pd.DataFrame(list(i.values()))
    u_df.append(df)

u_df = pd.concat(u_df,axis=0)
u_df.to_excel('file'+str(time.time())+'.xlsx',index=False)