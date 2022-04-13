import json
import requests
import os, os.path
from datetime import datetime
import time

while True:
    api_url = "https://api.steampowered.com/IPlayerService/GetBadges/v1/?key=aaaaaaaaaaaaaaaaaaaaaaaaaaaaa&input_json={%22steamid%22:76561199187883490}"

    response = requests.get(api_url).json()

    files = len(os.listdir('./output'))

    try:
        response["response"]["badges"]
    
    except:
        print("API called failed, for some reason")
    
    else:
        with open(f"output/nr{files+1}_at_{str(datetime.now())}.json", "w") as f:
            json.dump(response["response"]["badges"], f)
        
    
    time.sleep(60)