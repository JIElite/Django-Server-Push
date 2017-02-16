# This demo is related to /word_cloud/demo

import json
import requests
import time

payload = {
           "group":"display_word",
           "words":
                [{"word": "socket", "freq": 600},
                {"word": "hello", "freq": 700}]
           }

payload2 = {
           "group":"display_word",
           "words":
                [{"word": "Good", "freq": 600},
                {"word": "Night", "freq": 700}]
           }


resp = requests.post("http://127.0.0.1:8000/data_pipeline/collect_data/", 
        data=json.dumps(payload),
        headers={'content-type':'application/json'})

time.sleep(3)

resp = requests.post("http://127.0.0.1:8000/data_pipeline/collect_data/", 
        data=json.dumps(payload2),
        headers={'content-type':'application/json'})


