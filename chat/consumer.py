import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = "group"

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data_point = json.loads(text_data)
        val = data_point['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'de_processing',
                'message': val
            }
        )

        print('>>>>', text_data)

    async def de_processing(self, event):
        val_other = event['message']
        await self.send(text_data=json.dumps({'message': val_other}))
