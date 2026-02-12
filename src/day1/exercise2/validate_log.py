import os

file_name = 'app.log'

if not os.path.exists(file_name):
    print("Error: File 'app.log' not found.")

elif os.path.getsize(file_name):
    print("Warning: Log file is empty.")

else: 
    with open('app.log', 'r') as f:
        log = f.read().strip()
        if(log == 'ERROR'):
            print("Alert: Error found in logs!")
        else:
            print("System Healthy.")