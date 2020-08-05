import json
import socket
import re
import os


def _post_is_right(POST, keys):
    """Проверка POST-запроса по необходимым в запросе ключам"""

    keys_is_available = [True if key in POST else False for key in keys ]
    if all(keys_is_available):
        return True
    else:
        return False


def lambda_handler(event, context):

    if _post_is_right(event,["channel", "word", "num_of_winners"]):
        TOKEN = os.environ.get('BOT_TOKEN')
        USERNAME = os.environ.get('BOT_USERNAME')
        CHANNEL = event['channel']
        WORD = event['word']
        NUM_OF_WINNERS = int(event['num_of_winners'])
    else:
        return {
            'statusCode': 200,
            'body': {
                'error': 'NotEnoughParameters'
            }
        }

    connection = ('irc.chat.twitch.tv', 6667)
    server = socket.socket()
    server.connect(connection)
    server.send(bytes(f'PASS {TOKEN}\r\n', 'utf-8'))
    server.send(bytes(f'NICK {USERNAME}\r\n', 'utf-8'))
    server.send(bytes(f'JOIN #{CHANNEL}\r\n', 'utf-8'))

    winners = []
    while len(winners) < NUM_OF_WINNERS:
        response = server.recv(2048).decode('utf-8')
        response = response.split('\r\n')
        for user_message in response:
            if user_message:
                match = re.findall(r':(\w+)!.*:([\S\s]+)', user_message)
                if match:
                    if WORD.lower() == match[0][1].lower() and len(winners) < NUM_OF_WINNERS:
                        winners.append(match[0][0])

    if winners:
        return {
            'statusCode': 200,
            'body': {
                'winners': winners
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': {
                'error': 'NotFound'
            }
        }
