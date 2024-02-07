from typing import Type, Tuple, Dict
import requests
from requests import Request
from collections import namedtuple
from src.errors.http_request_error import Http_request_error
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface

class SwapApiConsumer(SwapiApiConsumerInterface):
  '''Class to consume swapi api with http requests'''
  def __init__(self) -> None:
    self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')
    self.get_starships_information_response = namedtuple('GET_Starship_Info', 'status_code request response')
    

  def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
    '''
      request starships in pagination
      :param - page: on with page of navegation
      :return - Tuple with status_code, request, response attributes
    '''
    request = requests.Request(
      method='GET',
      url='https://swapi.dev/api/starships/',
      params={'page': page}
    )
    request_prepared = request.prepare()
    response = self.__send_http_request(request_prepared)
    
    status_code = response.status_code
    if(status_code >= 200 and status_code <= 299):
      return self.get_starships_response(
        status_code=status_code, 
        request=request, 
        response=response.json()
        )
    else:
        raise Http_request_error(
                                 message=response.json()['detail'], 
                                 status_code=status_code
                                 )
        
  def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
    '''
      request starships information
      :param - starships_id: int with id of selected starship
      :return - Tuple with status_code, request, response attributes
    '''
    request = requests.Request(
      method='GET',
      url='https://swapi.dev/api/starships/{}/'.format(starship_id),
    )
    request_prepared = request.prepare()
    response = self.__send_http_request(request_prepared)
    
    status_code = response.status_code
    if(status_code >= 200 and status_code <= 299):
      return self.get_starships_information_response(
        status_code=status_code, 
        request=request, 
        response=response.json()
        )
    else:
        raise Http_request_error(
                                 message=response.json()['detail'], 
                                 status_code=status_code
                                 )
    
  @classmethod
  def __send_http_request(cls, request_prepared: Type[Request]) -> any:
    '''
      Prepare session and send htto request
      :param - req_prepared: request Object with all params
      :response - Http response RAW
    '''
    http_session = requests.Session()
    response = http_session.send(request_prepared)
    return response