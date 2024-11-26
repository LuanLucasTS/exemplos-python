#Faz o scraping em sites que contem tabelas

import pandas as pd
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
url = 'https://br.investing.com/equities/brazil'

request = requests.get(url, headers=header)

df = pd.read_html(request.text)
print(df)