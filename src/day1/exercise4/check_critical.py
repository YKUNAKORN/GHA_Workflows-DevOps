import os
import sys

file_name = 'deploy.txt'

if os.path.exists(file_name):
    print("key found. Proceeding...")
else:
    print("Critical Error: Deploy key missing!")
    sys.exit(1)