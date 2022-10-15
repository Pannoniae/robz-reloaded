import os
import shutil

used_skins = set()

for root, dirs, files in os.walk("./"):
    for name in files:
        with open(os.path.join(root, name)) as f:
            for line in f:
                try:
                    hd = line.index("head")
                    equipment = line[hd+5:].strip("}\"\n")
                    used_skins.add(equipment)
                except:
                    continue
print(sorted(used_skins))
#for root, dirs, files in os.walk("../../../entity/inventory/-equipment/head/"):
#    for dir in dirs:
#        if dir not in used_skins and len(dir) > 6:
#            shutil.rmtree(os.path.join(root, dir))