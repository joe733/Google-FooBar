from base64 import b64decode
import json

"""
If you care about having fun with encryption at all, I highly, highly recommend you turn back now!
"""

config_data = open('configs/identity.json').read()
config = json.loads(config_data)

code = config["secret"]
key = config["uname"]

len = len(key)
message = [chr(c ^ ord(key[i % len])) for i, c in enumerate(b64decode(code))]
message = ''.join(message)

print(message)