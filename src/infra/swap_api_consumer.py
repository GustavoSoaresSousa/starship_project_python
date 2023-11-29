import requests

class SwapApiConsumer:
  
  @classmethod
  def get_starships(self, page: int) -> any:
    param = {'page': page}
    response = requests.get('https://swapi.dev/api/starships/', params=param)
    
    return response.json()