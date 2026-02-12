import os
import sys

env = os.environ.get('DEPLOY_TARGET', 'PROD')

if (env == 'PROD'):
    print("Deploying to Production Server")
elif (env == 'TEST'):
    print("Deploying to Test Server")
else: 
    print("No target specified!")
    sys.exit(1)