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
        if path not in used_texs and ("#1" not in path and "#d" not in path and "#burned" not in path):
            print("NOTIN:"+path)
            #os.remove(os.path.join(root, file))
            pass
        else:
            #print("IN:"+path)
            pass
#print("\n".join(sorted(used_texs)))

os.chdir("../../")
# local humanskin texs
used_texs_local = set()

for root, dirs, files in os.walk("./"):
    for name in files:
        if name.endswith(".mtl"): # we only care about material textures
            with open(os.path.join(root, name)) as f:
                for line in f:
                    try:
                        hd = line.index("\"")
                        tex = line[hd+1:].strip("}\"\n")
                        #print(tex)
                        if "$" not in tex:
                            used_texs_local.add(tex.lower())
                    except:
                        continue
#print("\n".join(sorted(used_texs_local)))
os.chdir("./entity")
for root, dirs, files in os.walk("./humanskin"):
    for file in files:
        orig_path = os.path.join(root, file).removeprefix(".").replace("\\", "/").lower()
        path = os.path.join(root, os.path.splitext(file)[0]).removeprefix(".").replace("\\", "/").lower()
        filename = os.path.splitext(file)[0]
        #print(path)
        if orig_path.endswith(".dds")  and filename not in used_texs_local and ("#1" not in path and "#d" not in path and "#burned" not in path):
            print("NOTIN2:"+orig_path)
            #os.remove(os.path.join(root, file))
            pass
        else:
            #print("IN2:"+path)
            pass