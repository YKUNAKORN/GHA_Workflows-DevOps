"""
Note:
    In Python when we want to call eviroment varible, we use os.environ.get()
"""


import os

## Get ENV
os.environ['DEPLOY_ENV'] = 'PRODUCTION' 

env_name = os.environ.get('DEPLOY_ENV', 'DEVELOPMENT') # If not found DEPLOY_ENV then replace by DEVELOPERMENT

print(f"Current Environment: {env_name}")

if env_name == 'PRODUCTION':
    print("Deploying to Production Server...")
else:
    print("Deploying to Test Server...")


## Join
folder = "logs"
file = "error.log"

# Python will connect between 2 paths automaticly
full_path = os.path.join(folder, file) 

print(f"Path ที่ถูกต้อง: {full_path}")