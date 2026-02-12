import os
import json
import sys

folder_name = 'iam_policies'

# 1. Validation: Check if the folder exists first
if not os.path.exists(folder_name):
    print(f"Critical Error: Folder '{folder_name}' not found.")
    sys.exit(1)

# Move constant variable outside the loop for better performance
valid_effects = ['allow', 'deny']

print(f"Scanning policies in '{folder_name}'...")

for file_name in os.listdir(folder_name):
    if file_name.endswith('.json'):
        full_path = os.path.join(folder_name, file_name)
        
        # 2. Scope: Try-except block is now specific to file processing
        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
            
            # Use .get() to avoid KeyError if 'effect' is missing
            current_effect = data.get("effect")

            # 3. Validation Logic
            if current_effect not in valid_effects:
                # 4. Better Error Message: Shows WHICH file and WHAT value caused the error
                print(f"Validation Failed in '{file_name}': Found effect '{current_effect}', expected {valid_effects}.")
                sys.exit(1)

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON syntax in '{file_name}'.")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error processing '{file_name}': {e}")
            sys.exit(1)

print("Success: All policies passed validation.")