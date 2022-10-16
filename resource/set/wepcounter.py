import os
import shutil

used_weps = set()

for root, dirs, files in os.walk("./stuff/"):
    for name in files:
        with open(os.path.join(root, name)) as f:
            for line in f:
                try:
                    hd = line.index("entity")
                    equipment = line[hd+7:].strip("}\"\n")
                    used_weps.add(equipment)
                except:
                    continue
print(sorted(used_weps))
for root, dirs, files in os.walk("../entity/inventory/-weapon"):
    for dir in dirs:
        if dir not in used_weps and "hun" not in dir:
            #shutil.rmtree(os.path.join(root, dir))
            print(dir)