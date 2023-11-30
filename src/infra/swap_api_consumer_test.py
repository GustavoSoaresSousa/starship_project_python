from .swap_api_consumer import SwapApiConsumer
from src.errors.http_request_error import Http_request_error

def test_get_starships(requests_mock):
  '''Testing get_starships method'''
  
  requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': 'thing', 'results': [{}]})
  
  swap_api_consumer = SwapApiConsumer()
  page = 1
  get_starships_response = swap_api_consumer.get_starships(page=page)
  
  assert get_starships_response.request.method == 'GET'
  assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
  assert get_starships_response.request.params == {'page': page}
  assert get_starships_response.status_code == 200
  assert isinstance(get_starships_response.response['results'], list)
  
def test_get_starships_http_error(requests_mock):
  '''Testing error in get_starships method'''
  requests_mock.get('https://swapi.dev/api/starships/', status_code=404, json={'detail': 'something'})

  swap_api_consumer = SwapApiConsumer()
  page = 1000
  
  try:
    swap_api_consumer.get_starships(page=page)
    assert True is False
  except Http_request_error as error:
    assert error.message is not None
    assert error.status_code is not None
    print(error)
  