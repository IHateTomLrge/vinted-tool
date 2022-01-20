import random


class Proxy:

  def __init__(self, proxys):
    self.proxys = proxys
    isinstance(self.proxys, list)

  def format_proxy(self, proxy):
    try:
      ip, port, user, passw = proxy.split(':')
      return {
        'http': 'http://{}:{}@{}:{}'.format(user, passw, ip, port),
      }
    except ValueError:
      ip, port = proxy.split(':')
      return {
        'http': 'http://{}:{}'.format(ip, port),
        'https': 'https://{}:{}'.format(ip, port)
      }
  
  @property
  def proxy(self):
    return self.format_proxy(self.proxys) if isinstance(self.proxys, str) else self.format_proxy(random.choice(self.proxys))