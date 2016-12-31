from channels.routing import route
from websock.consumers import ws_connect, ws_receive

channel_routing = [
     route("websocket.connect", ws_connect),
     route("websocket.receive", ws_receive, path=r'/receive'),
]
