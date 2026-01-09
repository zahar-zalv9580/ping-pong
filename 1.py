import os
from pygame import *
import json

window = display.set_mode(400, 600)
display.set_caption("aojjfOKfkakgka")
file_name = 'stg.json'
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
        