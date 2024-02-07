from typing import Dict 
from abc import ABC, abstractmethod

class ControllersInterface(ABC):
  '''Interface to controllers'''
  @abstractmethod 
  def handler(self, http_resquest: Dict):
    raise 'Should implement handler method'