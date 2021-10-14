import requests
from bs4 import BeautifulSoup

def parse_ssr():
    response = requests.get('https://coinmarketcap.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('a',{'href':'/currencies/dogecoin/markets/'}).text
    return  data
print('doge',parse_ssr())
def parse_csr():
    repsonse = requests.get('https://www.blockchain.com/prices/api/coin-list-page?limit=20&page=0&tsym=USD')
    data = repsonse.json()
    for i in range(20):
        try:
            s=[x for x in data['Data'][i]['CoinInfo']['FullName']]
            r=[x for x in data['Data'][i]['DISPLAY']['USD']['PRICE']]
            print(*s, ' ', *r, sep='')
        except:
            pass

parse_csr()