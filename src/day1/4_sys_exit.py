"""
Note:
    Exit code 0: Success
    Exit code 1: Failure
"""


import sys

# Let say something we choosing
is_ready = False

if is_ready:
    print("System Ready!") # sys.exit(0) # default is 0 
else:
    print("System NOT Ready! Stopping pipeline...")
    sys.exit(1) # <--- Failure immediately! GitHub Actions found an Error
    
print("This message wouldn't print if the program do condition else")