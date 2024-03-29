from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validatior import get_pagination_validator
from src.validators.get_starship_information_validator import get_starship_information_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_information_composer import get_starship_information_composer
from src.presenters.errors.error_controller import handle_error
starships_routes = APIRouter()

@starships_routes.get('/api/starship/list')
async def get_starships_in_pagination(request: RequestFastApi):
  '''get_starships_in_pagination'''
  response = None
  controller = get_starships_in_pagination_composer()
    
  try:
    get_pagination_validator(request)
    response = await request_adapter(request, controller.handler)
  except Exception as e:
    response = handle_error(e)
  
  return JSONResponse(status_code=response['status_code'], content={'data': response['data']})

@starships_routes.post('/api/starship/information')
async def get_starship_information(request: RequestFastApi):
  'get_starship_information'
  response = None
  controller = get_starship_information_composer()
  
  try:
    await get_starship_information_validator(request)
    response = await request_adapter(request, controller.handler)
  except Exception as e:
    response = handle_error(e)
    
  return JSONResponse(
    status_code=response['status_code'],
    content=response['data']
  )