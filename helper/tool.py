try:
  '''Helpers'''
  from helper.client import Client
  from helper.webhook import Webhook
  from helper.proxy import Proxy

  '''Librarys'''
  from bs4 import BeautifulSoup
  import time
  import sys
  import os
  import platform

  '''Clear console output'''
  os.system('cls') if platform.system() == 'Windows' else os.system('clear')
except Exception as e:
  '''Throw exception'''
  import sys
  print("Blackbot.me | Vinted tool threw an exception: {}".format(str(e)))
  sys.exit()


class Tool():

  def __init__(self, product: str, maxPrice: int, webhook: str, proxies, status: str):
    self.product = product
    self.maxPrice = maxPrice
    self.webhook = webhook
    self.status = status
    self.client, self.ua = Client().client
    if proxies != None:
      self.client.proxies.update(Proxy(proxies).proxy)
    self.products: list = []
    self.getToken()
    self.monitor()

    print('Sending webhook...')
    Webhook(self.products, self.webhook)

  def getToken(self):
    while True:
      print("Getting token...")
      try:
        page = self.client.get('https://www.vinted.fr/vetements',
          headers={
            'User-Agent': self.ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'If-None-Match': 'W/"ea0d0f228dd938672c6458ac905280a5"'
          },
          params={
            'search_text': self.product
          }
        )
      except Exception:
        print("Error while requesting token !")
        time.sleep(3)
        continue
      try:
        scraper = BeautifulSoup(page.text, 'lxml')
        self.token: str = scraper.find('meta', {'name': 'csrf-token'}).get('content')
      except Exception:
        print("Error while parsing token !")
        time.sleep(3)
        continue
      if self.token:
        break

  def monitor(self):
    while True:
      print("Getting products...")
      try:
        res = self.client.get('https://www.vinted.fr/api/v2/items',
          headers={
            'User-Agent': self.ua,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fr',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'X-CSRF-Token': self.token,
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'If-None-Match': 'W/"25f63f1f7dbd361aeddf0c541570bf1d"',
            'TE': 'trailers'
          },
          params={
            'search_text': self.product,
            'catalog_ids': '',
            'color_ids': '',
            'brand_ids': '',
            'size_ids': '',
            'material_ids': '',
            'status_ids': self.status,
            'is_for_swap': '0',
            'page': '1',
            'per_page': '99999'
          }
        )
      except Exception:
        print("Error while requesting products !")
        time.sleep(3)
        continue
      
      if res.status_code == 401:
        print("Token expired !")
        self.getToken()
        continue

      try:
        scraper = res.json()
        for item in scraper.get('items'):
          name = item.get('title')
          price = item.get('price_numeric')
          size = item.get('size')
          link = "https://www.vinted.fr" + item.get('path')
          status = item.get('status')
          country = item.get('country')
          if self.maxPrice > float(price):
            self.products.append({
              'name': name,
              'price': price,
              'size': size,
              'link': link,
              'status': status,
              'country': country
            })
      except Exception:
        print("Error while parsing products !")
        time.sleep(3)
        continue
      break