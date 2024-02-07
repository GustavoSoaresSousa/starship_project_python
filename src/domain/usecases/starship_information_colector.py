from abc import ABC, abstractmethod
from typing import Dict, List

class StarshipsInformationColectorInterface(ABC):
  '''Starships Information Colector Interface'''
  @abstractmethod
  def find_starship(self, starship_id: int, time: str) -> Dict:
    '''Must Implement'''
    raise Exception('Must implement find_starship method')