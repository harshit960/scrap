from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
# List of proxy configurations
proxy_configurations = [
    "2.56.119.93:5074@avzjgtnd:07agodaitzyp",
    "185.199.229.156:7492@avzjgtnd:07agodaitzyp",
    "185.199.228.220:7300@avzjgtnd:07agodaitzyp",
    "185.199.231.45:8382@avzjgtnd:07agodaitzyp",
    "188.74.210.207:6286@avzjgtnd:07agodaitzyp",
    "188.74.183.10:8279@avzjgtnd:07agodaitzyp",
    "188.74.210.21:6100@avzjgtnd:07agodaitzyp",
    "45.155.68.129:8133@avzjgtnd:07agodaitzyp",
    "154.95.36.199:6893@avzjgtnd:07agodaitzyp",
    "45.94.47.66:8110@avzjgtnd:07agodaitzyp"
]

for config in proxy_configurations:
    proxy_parts = config.split('@')
    proxy_address, credentials = proxy_parts[0], proxy_parts[1]

    # Extracting credentials
    username, password = credentials.split(':')

    # Set up Chrome WebDriver with the proxy
    chrome_options = webdriver.ChromeOptions()

    # Add proxy settings
    proxy_string = f"{username}:{password}@{proxy_address}"
    chrome_options.add_argument(f'--proxy-server=http://{proxy_string}')
    chrome_options.add_argument(f'--proxy-server=https://{proxy_string}')

    # Create WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    # Now, navigate to the target website
    driver.get("https://example.com")
    time.sleep(30)
    # You may need to add additional code here to handle any authentication prompts that the proxy doesn't handle automatically.
    
    # Don't forget to quit the WebDriver instance when you're done
    driver.quit()