import os

for root, dirs, files in os.walk("./"):
    for name in files:
        if name.endswith("pdn"):
            os.remove(os.path.join(root, name))