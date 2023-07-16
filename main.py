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
        outdata[i] = templistt
    return outdata


filename = "./files/input.xlsx"

# Call the function to read the Excel file
result = read_excel_file(filename)

# print(result["Link 1"])
outList = []
outSite1=[]
outSite2=[]
outSite3=[]
for i in range(len(result["Link 1"])):
    outSite1.append(site1(result["Link 1"][i]))
    print("site 1 done")
for i in range(len(result["Link 2"])):
    outSite2.append(site2(result["Link 2"][i]))
    print("site 2 done")
for i in range(len(result["Link 3"])):
    outSite3.append(site3(result["Link 3"][i]))
    print("site 3 done")

outList.extend(outSite1)
outList.extend(outSite2)
outList.extend(outSite3)

u_df=[]
for i in outList:
    df = pd.DataFrame(list(i.values()))
    u_df.append(df)

u_df = pd.concat(u_df,axis=0)
u_df.to_excel('file.xlsx',index=False)