expected_version = "v1.0.0"

try:
    with open('version.txt', 'r') as f:
        current_version = f.read().strip()
        if (current_version == expected_version):
            print("Version Correct. Ready to deploy.")
        else:
            print(f"Version Mismatch! Found {current_version}, Expect: {expected_version}")
except FileNotFoundError:
    print("Error: File 'version.txt' not found.")