from cerberus import Validator
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

def get_pagination_validator(request: any):
  '''Pagination validator'''
  query_param_validator = Validator({
    'page': {'type': 'string', 
             'allowed':  ['1', '2', '3', '4'],
             'required': True
            }
  })
  response = query_param_validator.validate(request.query_params)
  if response is False:
    raise HttpUnprocessableEntityError(query_param_validator.errors)