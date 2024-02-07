from src.infra.swap_api_consumer import SwapApiConsumer
from src.data.usecases.starships_list_colector import StarshipsListColector
from src.presenters.controllers.starships_list_colector_controller import StarshipsListColectorController

def get_starships_in_pagination_composer():
  infra = SwapApiConsumer()
  usecases = StarshipsListColector(infra)
  controller = StarshipsListColectorController(usecases)
  
  return controller 