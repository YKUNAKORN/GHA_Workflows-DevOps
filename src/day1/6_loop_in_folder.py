"""
Note:
    - os.listdir()
    - for loop
"""


import os

folder_path = 'policies'

# Loop files in the folder
for file_name in os.listdir(folder_path):
    
    # 1. Filter: Is it .json?
    if file_name.endswith('.json'):
        
        # 2. Construct Path: buid full path of file
        full_path = os.path.join(folder_path, file_name) # output: policies/file1.json
        print(f"Checking file: {full_path}...")
        
        # 3. Process: ส่งไปฟังก์ชันตรวจสอบ (ที่เราเขียนไว้ในบทก่อนๆ)
