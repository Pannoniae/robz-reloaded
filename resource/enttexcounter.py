import os
import shutil

used_texs = set()

for root, dirs, files in os.walk("./"):
    for name in files:
        if name.endswith(".mtl"): # we only care about material textures
            with open(os.path.join(root, name)) as f:
                for line in f:
                    try:
                        hd = line.index("$")
                        tex = line[hd+1:].strip("}\"\n")
                        #print(tex)
                        used_texs.add(tex.lower())
                    except:
                        continue
#print("\n".join(sorted(used_texs)))
os.chdir("./texture/common")
for root, dirs, files in os.walk("./humanskin"):
    for file in files:
        path = os.path.join(root, os.path.splitext(file)[0]).removeprefix(".").replace("\\", "/").lower()
        #print(path)
        if path not in used_texs and "#" not in path:
            print("NOTIN:"+path)
            os.remove(os.path.join(root, file))
            pass
        else:
            #print("IN:"+path)
            pass
#print("\n".join(sorted(used_texs)))