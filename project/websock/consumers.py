import json

from channels import Channel
from channels import Group


def ws_connect(message):
    # KeyError: text
    # print("ws_connect: ".format(message.content['text']))
    # 沒有顯示 type
    print("ws_connect: ", message.content['path'])

    

def ws_receive(message):
    # 原本的 js 提供的是月份！所以沒辦法解析 json, 會導致回傳的時候有錯誤
    # print("ws_receive: ", message.content['text'])
    
    # TODO 可以改成添加 message type 參數
    # 但是其他資訊也會被這個 channels 接收
    # 所以這裡的工作就是在做訊息的分配，將訊息分配給適當的 channel 處理
    
    try:
        receive_message_json = json.loads(message.content['text'])
        if receive_message_json['group'] != None: 
            Group(receive_message_json['group']).add(message.reply_channel) 

    except:
        # TODO 現在沒有這個 channel 了
        Channel("myapp.receive").send(message.content)
