# from api.utils.other_request import Request

# globalPath = "http://auth_api:8000/api/auth"

# class LoginService():
#   request_login = Request(globalPath)
#   username = "bisaoonn"
#   password = "Abrenet123*"
#   token = None
#   header = None
#   retailer_id = None
#   retailer = None
#   agency_id = None
#   agency = None
#   jwt = None
#   def __init__(self):
#     self.login()
#     self.get_retailers()
#     self.get_agencies()
#     self.get_token()

#     pass
#   def get_token(self):
#     url=f"/useragency/get-roles"
#     try:
#       body = {
#         "agency_slug": self.agency["slug"],
#         "retailer_slug": self.retailer["slug"]
#       }
#       result = self.request_login.post(url=url, headers=self.header, data=body)
      
#       if(result):
#         response = result["response"]
#         jwt = response["jwt"]
#         self.header = {
#           "token": jwt
#         }
#       pass
#     except Exception as e:
#       pass
#   def get_agencies(self):
#     url=f"/agency/get-by-retailer/{self.retailer_id}"
#     try:
#       result = self.request_login.get(url=url, headers=self.header)
      
#       if(result):
#         response = result["response"]
#         agencies = response["agencies"]
#         self.agency = agencies[0]
#         self.agency_id = self.agency["id"]
#       pass
#     except Exception as e:
#       pass
#   def get_retailers(self):
#     url = "/retailer/get-retailers"
#     try:
#       result = self.request_login.get(url=url, headers=self.header)
#       if(result):
#         response = result["response"]
#         retailers = response['retailers']
#         self.retailer = retailers[0]
#         self.retailer_id = self.retailer['id']
#       pass
#     except Exception as e:
#       pass
#   def login(self):
#     url  = '/user/login'
#     try:
#       body = {
#         "username":self.username,
#         "password":self.password
#       }
#       result = self.request_login.post(url = url, data = body)
#       if(result):
#         response = result["response"]
#         self.token = response["token"]
#         self.header={
#           "token": self.token
#         }
#       pass
#     except Exception as e:
#       pass