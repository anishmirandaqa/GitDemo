import requests
import json

url=""
payload = {"":""

}

response = requests.post(url,json=payload)
if response.status_code==200
	respose_data=json.loads(response.text)
	