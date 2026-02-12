import sys
import json
import os

file_name = 'build_config.json'

if not os.path.exists(file_name):
    print(f"Error: file '{file_name}' not found.")
    sys.exit(1)

try:
    with open(file_name, 'r') as f:
        config = json.load(f)
        environment = config.get('environment')
        valid_envs = ['production', 'development']

        if environment not in valid_envs:
            print("Wrong environment state!")
            sys.exit(1)

        retry_count = config.get('retry_count')
        # Ensure retry_count is numberic
        if not isinstance(retry_count, int):
            print("Error: 'retry_count' must be an integer")
            sys.exit(1)
        if retry_count <= 0:
            print(f"Error: Invalid retry_count {retry_count}. Must be greater than 0.")

        # All passed
        print("Build Config Valid.")
        
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from '{file_name}'. Please check the syntax.")
    sys.exit(1)
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
    sys.exit(1)