from typing import Type, Tuple, Dict
from abc import ABC, abstractmethod
from requests import Request

class SwapiApiConsumerInterface(ABC):
  '''API consumer interface'''
  
  @abstractmethod
  def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
    '''Must implement'''
    raise Exception ('Must implement get_starships')
  
  @abstractmethod
  def get_starship_information(self, starship_id: int) -> Tuple[int, Type[Request], Dict]:
    '''Must implement'''
    raise Exception ('Must implement get_starship_information')
    
    