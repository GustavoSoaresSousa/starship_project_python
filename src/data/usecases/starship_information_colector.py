from src.domain.usecases.starship_information_colector import StarshipsInformationColectorInterface
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface 
from typing import Dict, List, Type
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class StarshipInformationColector(StarshipsInformationColectorInterface):
  '''StarshipInformationColector usecase'''
  def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
    self.__api_consumer = api_consumer
    
  def find_starship(self, starship_id: int, time: str) -> Dict: 
    starship_information = self.__search_starship(starship_id)
    mglt = starship_information['MGLT']
    distance_traveled = self.__calculate_distance_traveled_to_spaceship(mglt, time)
    formated_response = self.__format_response(starship_information, distance_traveled)
    return formated_response
    
  
  def __search_starship(self, starship_id: int) -> Dict:
    api_response = self.__api_consumer.get_starship_information(starship_id)
    if api_response.response['MGLT'] == 'unknown':
      raise HttpUnprocessableEntityError('Unprocessible information for selected starship')
    else:
      return api_response.response
  
  @classmethod
  def __calculate_distance_traveled_to_spaceship(cls, mglt: str, time: str) -> int:
    distance_traveled = int(mglt) * int(time)
    return distance_traveled
  
  @classmethod
  def __format_response(cls, starship_information: Dict, distance_traveled:int) -> Dict:
    return {
      'starship': starship_information['name'],
      'model': starship_information['model'],
      'manufacturer': starship_information['manufacturer'],
      'max_atmosphering_speed': starship_information['max_atmosphering_speed'],
      'MGLT': starship_information['MGLT'],
      'distance_traveled': str(distance_traveled) + 'ML'
    }