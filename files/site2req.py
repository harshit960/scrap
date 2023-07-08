#from selectorlib import Extractor
import requests 
import re
from fake_headers import Headers as fakehead







def scrape(url):  
    headers = fakehead(
        # generate any browser & os headeers
        headers=True  # don`t generate misc headers
    )

    header=headers.generate()
    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=header)
    print(r.status_code,r.text)
    return r

link="https://www.idealista.it/aree/vendita-case/con-aste_no/lista-1?ordine=area-asc&shape=%28%28%7DnzhGul%7C%7D%40cGqb%40%7C%40%7B%40vOhJdAh%40h%40h%40FjLsDbAAbCsGzB%29%29"
print(scrape(link))
