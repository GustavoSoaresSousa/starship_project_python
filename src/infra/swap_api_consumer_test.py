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

def test_get_starship_information(requests_mock):
  '''Testing get_information_method'''
  
  starship_id = 9
  swapi_api_consumer = SwapApiConsumer()
  # response = swapi_api_consumer.get_starships_information(starship_id)
  
  requests_mock.get(
    url='https://swapi.dev/api/starships/{}/'.format(starship_id),
    status_code = 200,
    json={'name': 'some', 'model': 'thing', 'MGLT': '123'}
  )
  
  starship_information = swapi_api_consumer.get_starship_information(starship_id)
  
  assert starship_information.request.method == 'GET'
  assert starship_information.request.url == 'https://swapi.dev/api/starships/{}/'.format(starship_id)
  assert starship_information.status_code == 200
  assert 'MGLT' in starship_information.response