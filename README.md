# Websocket Server Push using Django

## Introduction
這個專案是利用 Django + channels 實作 server push
demo 的方式是用 d3 word cloud 文字雲的方式。

目前實作一種觸發的方法：
1. HTTP request ---> Django Server --- websocket ---> client (display word cloud)
2. websocket client ---> Django Server --- websocket ---> client (預計實作項目)

## How to use?
進入 /project
`$ python3 manage.py runserver`

開啟網頁：
`http://127.0.0.1:8000/wordcloud/`

## The Usage of Files
* /notification_script
這裏的 script 用來發送資料給 server，來觸發 server push

* /project
	* /word_cloud: 跟 word cloud 顯示頁面有關，實作位於 views.py
	* /websock: 跟 websocket 有關，實作的 handler 是 consumers.py, 主要用來分派 websocket message
	* /notification: 處理跟 notification 有關的資訊，包含從 server 傳送 real-time data 到適當 channel
	* /project
		* /routing.py: route websocket channel


## Dependency Package
Websocket 的實作，使用 channels 這個套件。
Channels: https://channels.readthedocs.io/en/latest/

## 獨立運作
我們設定如果是用 in-memory 的方式的話，views handler, channels worker 都會在同一個 process 中。
這對 scaling 是不利的。
如果要將他們分散開來的話，可以更改 setting.py 將 Channel_Layer 配置為 redis
並且新增 asgi.py 到專案目錄下。

在執行的時候就可以區分開來：
``` 
$ python3 manage.py runserver --noworker     # 開啟伺服器前端(interface server, channel layer)
$ python3 manage.py runworker                # 針對 channels
```
