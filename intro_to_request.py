import requests

post_code_req=requests.get("http://api.postcodes.io/postcodes/se120nb")
print(post_code_req.content)
