import json
import requests
import time

from preprocess import transfer_topic_csv_to_pyobj


def upload_data(payload):
    destination = "http://127.0.0.1:8000/data_pipeline/collect_data/"
    
    resp = requests.post(
            destination, 
            data=json.dumps(payload),
            headers={'content-type':'application/json'}
    )

    return resp



def push_data(data_list):
#    data_list 的格式:
#    [
#     {
#      "title": "your topic name",
#      "data" : [
#                 {
#                   "word": "cloud_word",
#                   "weight: "weight_for_word_size"
#                 },
#                 ...
#                 ...
#                 ...
#                ]
#     },
#     {
#      "title": "your topic name",
#      "data" : ...
#     },
#     ...
#     ...
#     ...
#    ]
    for index, topic_data in enumerate(data_list):
        
        payload = {
               # group is used for recognized the group of websocket
               "group": "topic_word" + str(index+1),
               "topic": topic_data["title"],
               "data": topic_data["data"],
        }

    resp = upload_data(payload)
    return resp


if __name__ == "__main__":
    topic_cloud_json_data = transfer_topic_csv_to_pyobj("./data/LDA_Doc_dummyA.csv")
    push_data(transfer_topic_csv_to_pyobj)


