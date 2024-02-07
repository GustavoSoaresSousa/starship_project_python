from typing import Dict, Type
from src.presenters.interfaces.controllers import ControllersInterface
from src.domain.usecases.starship_information_colector import StarshipsInformationColectorInterface

class StarshipInformationColectorController(ControllersInterface):
  '''Controler to StarshipInformationController '''
  def __init__(self, starship_information_colector: Type[StarshipsInformationColectorInterface]) -> None:
    self.__use_case = starship_information_colector
    
  def handler(self, http_resquest: Dict):
    '''Handle to information colector controler'''
    
    starship_id = http_resquest['body']['starship_id']
    time = http_resquest['body']['time']
    
    starshihp_information = self.__use_case.find_starship(starship_id, time)
    http_response = {'status_code': 200, 'data': {'data': starshihp_information}}
    
    return http_response
  