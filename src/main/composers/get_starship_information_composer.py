from src.infra.swap_api_consumer import SwapApiConsumer
from src.data.usecases.starship_information_colector import StarshipInformationColector
from src.presenters.controllers.starship_information_colector_controler import StarshipInformationColectorController

def get_starship_information_composer():
  infra = SwapApiConsumer()
  usecases = StarshipInformationColector(infra)
  controller = StarshipInformationColectorController(usecases)
  
  return controller 