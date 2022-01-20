from typing import Tuple
import random
import cloudscraper

'''Init client class'''
class Client(object):
    
  @property
  def client(self) -> Tuple[cloudscraper.CloudScraper, str]:
    platforms: list = [
      'ios',
      'android',
      'windows',
      'darwin',
      'linux'
    ]

    session: cloudscraper.CloudScraper = cloudscraper.create_scraper(
      browser={
        'browser': 'chrome',
        'mobile': True,
        'platform': random.choice(platforms)
      }
    )
    ua = session.headers['User-Agent']
    return session, ua

