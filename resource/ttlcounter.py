import os

for root, dirs, files in os.walk("./"):
    for name in files:
        if name.endswith("psd"):
            os.remove(os.path.join(root, name))