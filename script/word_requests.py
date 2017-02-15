import json
import requests
import time

payload = {
           "group":"display_word",
           "data":
                [{"word": "socket", "freq": 600},
                {"word": "hello", "freq": 700}]
           }

resp = requests.post("http://127.0.0.1:8000/notification/collect_data/", 
        data=json.dumps(payload),
        headers={'content-type':'application/json'})


time.sleep(3)

payload2 = {
           "group":"display_word",
           "data":
                [{"word": "Good", "freq": 600},
                {"word": "Night", "freq": 700}]
           }

resp = requests.post("http://127.0.0.1:8000/notification/collect_data/", 
        data=json.dumps(payload2),
        headers={'content-type':'application/json'})


