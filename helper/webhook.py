import requests
import time

class Webhook:
  def __init__(self, products: list, webhook: str):
    self.logo: str = "https://cdn.discordapp.com/attachments/881529504231727104/881531718551621702/bot-2.png"
    self.name: str = "Blackbot.me | Vinted tool"
    self.sucess: int = 5822093
    self.webhook: str = webhook
    self.products: list = products
    self.fields: list = []

    for product in products:
      self.fields.append({
        "name": product.get('name'),
        "value": "size: {size}\nprice: {price} €\nstatus: {status}\ncountry: {country}\n[Link]({url})".format(size=product.get('size'), price=product.get('price'), status=product.get('status'), country=product.get('country'), url=product.get('link'))
      })

    self.ping()

  def ping(self):
    while True:
      res = requests.post(self.webhook,
        json = {
          "content": None,
          "embeds": [{
            "title": "{} product(s) found(s) !".format(str(len(self.products))),
            "color": 5822093,
            "fields": self.fields,
            "footer": {
              "text": self.name,
              "icon_url": self.logo
            },
            "thumbnail": {
              "url": "https://upload.wikimedia.org/wikipedia/fr/thumb/6/68/Vinted-logo.svg/1200px-Vinted-logo.svg.png"
            }
          }]
        }, 
        headers = {
          "Content-Type": "application/json"
        }
      )
      
      if res.status_code == 429:
        time.sleep(3)
        continue

      if res.status_code not in (200, 204, 304):
        return print("[Webhook] Error: {}".format(res.status_code))
      print("Webhook sent !")
      break