## Clase para la conexion a los servicios publicados en los otros microservicios
# from api.utils.other_request import Request
# from services.loginService import LoginService

# globalPath = "http://auth_api:8000/api/optativo"

# class DeService(LoginService):
#   request = Request(globalPath)
#   def getValidateUser(self, data, headers:dict):
#     final_header = {**self.header, **headers}
#     result = self.request.post(url='/user/validate/session/', headers=final_header)
#     if(result):
#       return True, result.get("response", None)
#     return False, None
  
#   request = Request("")
#   def __init__(self):
#     super().__init__()
#     pass
  