import os

for root, dirs, files in os.walk("./"):
    for name in files:
        if name == "smock.dds":
            os.remove(os.path.join(root, name))