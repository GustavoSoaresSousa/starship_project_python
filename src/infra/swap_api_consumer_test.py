from .swap_api_consumer import SwapApiConsumer

def test_get_starships(requests_mock):
  '''Testing get_starships method'''
  
  requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing'})
  
  swap_api_consumer = SwapApiConsumer()
  response = swap_api_consumer.get_starships(page=1)
  
  print(response)