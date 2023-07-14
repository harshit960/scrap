import random
def setproxy(chrome_options):
    # Check if the proxy.txt file exists
    try:
        with open("proxy.txt", "r") as file:
            proxies = file.readlines()  # Read all lines from the file
            proxy = random.choice(proxies).strip()  # Select a random proxy
    except FileNotFoundError:
        proxy = None  # Set proxy as None if file not found
    except Exception as e:
        print(f"An error occurred while reading the proxy file: {str(e)}")
        proxy = None  # Set proxy as None if there's an error

    if proxy:
        chrome_options.add_argument(f'--proxy-server=http://{proxy}')

