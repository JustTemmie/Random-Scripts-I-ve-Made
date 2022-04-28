import os 

path = "print_me.py"
print(os.open(path, os.O_RDONLY))