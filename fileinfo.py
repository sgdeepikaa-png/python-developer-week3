import os
from datetime import datetime

path = input("Enter File Path: ")

if os.path.exists(path):

    size = os.path.getsize(path) / 1024

    modified = datetime.fromtimestamp(os.path.getmtime(path))

    print("File Name :", os.path.basename(path))
    print("Directory :", os.path.dirname(os.path.abspath(path)))
    print("Extension :", os.path.splitext(path)[1])
    print("Size :", round(size, 2), "KB")
    print("Modified :", modified.strftime("%Y-%m-%d %H:%M:%S"))

else:
    print("File Not Found")