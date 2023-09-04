import random
import requests
import json
def setproxy(chrome_options):
    # # Check if the proxy.txt file exists
    # try:
    #     with open("proxy.txt", "r") as file:
    #         proxies = file.readlines()  # Read all lines from the file
    #         proxy = random.choice(proxies).replace('\n','').strip()  # Select a random proxy
    # except FileNotFoundError:
    #     proxy = None  # Set proxy as None if file not found
    # except Exception as e:
    #     print(f"An error occurred while reading the proxy file: {str(e)}")
    #     proxy = None  # Set proxy as None if there's an error

    # if proxy:
    response = requests.get(
    "https://httpbin.org/get",
    proxies={
        "http": "http://a200d06ff02746e1a379f93870d05b6c:@proxy.crawlera.com:8011/",
        "https": "http://a200d06ff02746e1a379f93870d05b6c:@proxy.crawlera.com:8011/",
    },
    verify=r'C:\Users\rajha\Desktop\zyte-proxy-ca.crt' 
)
    # print(response.text)
    jsonn = json.loads(response.text)
    proxy = str(jsonn["origin"])
    print("using proxy ",proxy)
    chrome_options.add_argument(f"--proxy-server={proxy}")



