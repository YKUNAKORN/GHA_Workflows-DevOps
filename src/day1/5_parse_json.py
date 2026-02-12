"""
Note:
    Only one command that u have to remmember is "json.load(f)" | Read the Object file and then tranfrom to dictionary form

    json.load() VS json.loads()
        - json.load() => Use with file that you just open
        - json.loads() => Use with String long format

    Key error: If you call data["password"] but file desn't has that key, the program will crash
        To avoid this problem use ".get()" like you also use in environ.get()
"""


import json
import sys

file_name = 'config.json'

try:
    with open(file_name, 'r') as f:
        # 1. Tranform json to Python dictionary
        data = json.load(f)

        # 2. Get data from key
        print(f"Checking App: {data["app_name"]}")
        print(f"Version: {data["version"]}")

        # 3. Validation
        if data["version"] < 2.0:
            print("Version too old!")
            sys.exit(1)

except FileNotFoundError:
    print("Config file missiong!")
    sys.exit(1)

except json.JSONDecodeError:
    print("Invalid JSON format! Please check syntax.")
    sys.exit(1)