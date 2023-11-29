from .swap_api_consumer import SwapApiConsumer

def test_get_starships():
  '''Testing get_starships'''
  swap_api_consumer = SwapApiConsumer()
  response = swap_api_consumer.get_starships(page=1)
  
  print(response)