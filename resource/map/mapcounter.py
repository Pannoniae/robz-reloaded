import os
import shutil

for root, dirs, files in os.walk("./"):
    for dir in dirs:
        print("-----------"+dir)
        for file in os.listdir(os.path.join(root, dir)):
            if file.endswith(".mi"):
                print(file)