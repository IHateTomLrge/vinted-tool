# Blackbot.me | Vinted tool

Small tool for [Vinted](https://www.vinted.com/) to get the best deals on your favorite products.

## Installation

```sh
git clone https://github.com/IHateTomLrge/vinted-tool.git
```

## Requirements

```sh
pip install -r requirements.txt
```

## Usage

```py
from helper.tool import Tool

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
```