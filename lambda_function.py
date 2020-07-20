import json
import socket
import re

def lambda_handler(event, context):

    TOKEN = event['token']
    USERNAME = event['username']
    CHANNEL = event['channel']
    MAX_TRY_COUNT = int(event['max'])
    WORD = event['word']
    NUM_OF_WINNERS = int(event['num_of_winners'])

    connection = ('irc.chat.twitch.tv', 6667)
    server = socket.socket()
    server.connect(connection)
    server.send(bytes(f'PASS {TOKEN}\r\n', 'utf-8'))
    server.send(bytes(f'NICK {USERNAME}\r\n', 'utf-8'))
    server.send(bytes(f'JOIN #{CHANNEL}\r\n', 'utf-8'))

    num_of_attemps = 0
    winners = []
    while num_of_attemps < MAX_TRY_COUNT:
        response = server.recv(2048).decode('utf-8')
        response = response.split('\r\n')
        for user_message in response:
            if user_message:
                match = re.findall(r':(\w+)!.*:([\S\s]+)', user_message)
                if match:
                    if WORD in match[0][1] and len(winners) < NUM_OF_WINNERS:
                        winners.append(match[0][0])
        num_of_attemps += 1

    if winners:
        return {
            'statusCode': 200,
            'body': winners
        }
    else:
        return {
            'statusCode': 200,
            'body': 'not found'
        }
