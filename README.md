# Websocket Server Push using Django

## Introduction
這個專案是利用 Django + channels 實作 server push</br>
呈現的方式是用 d3 word cloud 文字雲的方式。

目前實作一種觸發的方法：</br>
HTTP request ---> Django Server --- websocket ---> client (display word cloud)

預計實作：</br>
websocket client ---> Django Server --- websocket ---> client


## How to use?
進入 /project</br>
` $ python3 manage.py runserver `

demo 頁面：</br>
` http://127.0.0.1:8000/wordcloud/demo`


## The Usage of Files
* script
這裏的 script 用來發送資料給 server，來觸發 server push
負責用來處理接收資料的 handler 位於 /project/data_pipeline/views.py 中

	* /topic_cloud:
	這次修改比較多為這個部分，讓使用者可以讀取多個 topic 的資料，動態產生多個文字雲
	每一個 topic 的資料像是：topic, word1, weight1, word2, weight2 ...
	可從 csv file 讀取
	
	經由 push_topic_word_data.py 就可以傳送到 server

* /project
	* /word_cloud: 跟 word cloud 顯示頁面有關，實作位於 views.py
	* /websock: 跟 websocket 有關，實作的 handler 是 consumers.py, 主要用來分派 websocket message
	* /data_pipeline: 處理 data 轉送，包含從 server 傳送 real-time data 到適當 channel
	* /project
		* /routing.py: route websocket channel


## Dependency Package
Websocket 的實作，使用 channels 這個套件。</br>
Channels: https://channels.readthedocs.io/en/latest/

## Endpoint
* /word_cloud/demo: demo 單一一個文字雲，搭配 script/word_requests.py 使用。
* /word_cloud/topic_cloud: 搭配 script/topic_cloud/push_topic_word_data.py 將資料傳送到雲端顯示。

## 獨立運作
我們設定如果是用 in-memory 的方式的話，views handler, channels worker 都會在同一個 process 中，對 scaling 是不利的。</br>

要將他們分散開來的話，可以更改 setting.py 將 Channel_Layer 配置為 redis 。並且新增 asgi.py 到專案目錄下。

在執行的時候就可以區分開來：
``` 
$ python3 manage.py runserver --noworker     # 開啟伺服器前端 (interface server, channel layer)
$ python3 manage.py runworker                # 針對 channels
```

