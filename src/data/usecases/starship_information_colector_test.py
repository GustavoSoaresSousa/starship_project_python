# from src.data.usecases.starship_information_colector import StarshipInformationColector
# from src.infra.test.swapi_api_consumer import SwapApiConsumerSpy
# def test_find_starship():
#   '''testing find_starship_method'''
  
#   api_consumer = SwapApiConsumerSpy()
#   starship_information_colector = StarshipInformationColector(api_consumer)
  
#   starship_id = 3
#   time = 4
  
#   response = starship_information_colector.find_starship(starship_id=starship_id,time=time)
#   assert api_consumer.get_starship_information_attributes['starship_id'] == starship_id
#   assert isinstance(response, dict)
#   assert 'MGLT' in response
#   assert 'distance_traveled' in response