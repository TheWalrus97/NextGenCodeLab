import requests
import json
BASE = "http://127.0.0.1:5000/"
ff = {"Command": "greeting", "name": "alex"}


response = requests.post(BASE, json = ff)