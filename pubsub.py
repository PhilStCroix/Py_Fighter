import websocket
import json
import time
import uuid

# Set your Twitch username and API key
username = "fkn_phil"
client_id = "y8k89wqya92gcn4iw3f9xtaobscdd8"
oauth_token = "hcwclplewahjgdpym0chnbnila1vzt"

# Set the URL to the Twitch PubSub server
url = "wss://pubsub-edge.twitch.tv"

# Define a function to connect to the Twitch PubSub server
def connect():
    ws = None
    retries = 5 # Number of times to retry connection
    while retries > 0 and not ws:
        try:
            ws = websocket.create_connection(url)
            message = {
                "type": "PING"
            }
            ws.send(json.dumps(message))
            message = ws.recv()
            message_data = json.loads(message)
            nonce = message_data["nonce"]
            message = {
                "type": "LISTEN",
                "nonce": nonce,
                "data": {
                    "topics": [
                        "channel-points." + username
                    ],
                    "auth_token": oauth_token
                }
            }
            ws.send(json.dumps(message))
            return ws
        except Exception as e:
            print(e)
            retries -= 1
            time.sleep(1)
    return None

# Define a function to handle incoming messages
def handle_message(message):
    try:
        message_data = json.loads(message)
        message_type = message_data["type"]
        if message_type == "MESSAGE":
            message_data = json.loads(message_data["data"]["message"])
            if message_data["type"] == "points_event":
                print("Bit cheer event received!")
                print("User: " + message_data["user_name"])
                print("Amount: " + str(message_data["bits_used"]))
    except Exception as e:
        print(e)

# Connect to the Twitch PubSub server
ws = connect()

# Listen for incoming messages
while True:
    try:
        message = ws.recv()
        handle_message(message)
    except Exception as e:
        print(e)
        time.sleep(1)
        ws = connect()