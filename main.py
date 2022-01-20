from helper.tool import Tool
import os
import platform
os.system('cls' if platform.system() == 'Windows' else 'clear')
'''
Product, ex: Jordan 1, Nike, Adidas, etc.
Maximum price, ex: 180 (for 180€)
Discord webhook url to be used for sending products founds, ex: https://discordapp.com/api/webhooks/...
Proxies, can be a list of proxies, a string, or None if you don't want to use proxy.
The Proxy helper will automatically convert to usable proxy.
proxies: str = ''
proxies: list = []
proxies = None

status
6 = new with label
1 = new without label
2 = Very good state
3 = Good state
4 = Medium state

multiple status seperated by comma (6,1,2)
'''

proxies = None
product: str = 'Air force 1 Off white'
maxPrice: int = 200
status: str = '6,1'
webhook: str = 'https://discord.com/api/webhooks/...'

Tool(product, maxPrice, webhook, proxies, status)
