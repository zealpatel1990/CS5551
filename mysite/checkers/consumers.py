# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import logging
from .checkers_game_engine import *
logger = logging.getLogger("mylogger")



class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'game_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        logger.info('connected to websocket')
        board = play_display_checkers(UserPlayer, UserPlayer, upper_color=State.WHITE)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': board
            }
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        logger.info('DISconnected to websocket')

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message
            }
        )
        logger.info(text_data)

    # Receive message from room group
    def game_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
        logger.info('game_message funcion')
        logger.info(event)