import os

os.environ['CONFIG_DIR'] = 'ad2fadIASD9jJ3'
config_dir = os.environ.get('CONFIG_DIR')
print(config_dir)


file_name = 'prod_config.json'
full_path = os.path.join(config_dir, file_name)
print(f"Checking path: {full_path}")
if os.path.exists(full_path):
    print(f"Found config file at: {full_path}")
else:
    print("Config file missing!")