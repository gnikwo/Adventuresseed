from channels.generic.websocket import AsyncWebsocketConsumer, JsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class GameConsumer(JsonWebsocketConsumer):
    #===== INHERITED METHODS =====
    def connect(self):
        print('connected')
        self.color = ''
        async_to_sync(self.channel_layer.group_add)('game', self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('game', self.channel_name)

    def receive_json(self, content):
        command = content.get('command', 'error')
        print(content)
        commands = {
            'take_sprite': self.take_sprite,
            'move_sprite': self.move_sprite,
            'release_sprite': self.release_sprite,
            'ping': self.ping,
            'message': self.message,
            'select_participation': self.select_participation,
            'select_map': self.select_map,
            'modify_layer_accessibility': self.modify_layer_accessibility,
        }
        try:
            commands[command](content)
        except Exception as e:
            print('Catched exception: ')
            print(e)
            self.send_json({'command': 'error', 'message': 'Server received an unknown command: ' + command})

    #===== GROUPS METHODS =====
    def send_to_all(self, data):
        t = {'type': 'send_command'}
        async_to_sync(self.channel_layer.group_send)('game', {**t, **data})

    def send_command(self, data):
        self.send(text_data=json.dumps(data))

    #===== HANDLERS =====
    def take_sprite(self, content):
        sprite_id = content.get('sprite_id', 0)
        color = Participation.objects.get(id=participation_id).player.color
        self.send_to_all({
            'command': 'take_sprite',
            'sprite_id': sprite_id,
            'color': color,
        })

    def move_sprite(self, content):
        sprite_id = content.get('sprite_id', 0)
        x = content.get('position-x', 0)
        y = content.get('position-y', 0)
        self.send_to_all({
            'command': 'move_sprite',
            'sprite_id': sprite_id,
            'position-x': x,
            'position-y': y,
        })

    def release_sprite(self, content):
        sprite_id = content.get('sprite_id', 0)
        self.send_to_all({
            'command': 'take_sprite',
            'sprite_id': sprite_id,
        })

    def ping(self, content):
        x = content.get('position-x', 0)
        y = content.get('position-y', 0)
        color = Participation.objects.get(id=participation_id).player.color
        self.send_to_all({
            'command': 'ping',
            'position-x': x,
            'position-y': y,
            'color': color,
        })

    def message(self, content):
        message = content.get('message', 'ERROR')
        self.send_to_all({'command': 'message', 'message': message})

    def select_participation(self, content):
        participation_id = content.get('participation_id', 0)
        self.participation_id = participation_id

    def select_map(self, content):
        map_id = content.get('map_id', 0)
        selected_map = Map.objects.get(id=map_id)
        Map.objects.filter(game=selected_map.game).update(active=False)
        selected_map.active = True
        selected_map.save()
        self.send_to_all({'command': 'update_map', 'map_id': map_id})

    def modify_layer_accessibility(self, content):
        layer_id = content.get('layer_id', 0)
        map_id = content.get('map_id', 0)
        accessiblity = content.get('accessibility', 0)
        Layer.objects.get(id=layer_id).update(player_accessibility=accessibility)
        self.send_to_all({'command': 'update_map', 'map_id': map_id})
