import zipfile
import os
from zipfile import *

# go in resource
os.chdir("resource")

def zip_dir(dirpath, zippath):
    if isinstance(dirpath, str):
        fzip = zipfile.ZipFile(zippath, 'x', zipfile.ZIP_DEFLATED, compresslevel=4)
        basedir = os.path.dirname(dirpath) + '/' 
        for root, dirs, files in os.walk(dirpath):
            #if os.path.basename(root)[0] == '.':
            #    continue #skip hidden directories        
            dirname = root.replace(basedir, '')
            for f in files:
                fzip.write(root + '/' + f, dirname + '/' + f)
        fzip.close()
        print(f"Written {zippath} to disk!")
    elif isinstance(dirpath, list):
        fzip = zipfile.ZipFile(zippath, 'x', zipfile.ZIP_DEFLATED, compresslevel=4)
        for dir in dirpath:
            basedir = os.path.dirname(dir) + '/' 
            for root, dirs, files in os.walk(dir):
                #if os.path.basename(root)[0] == '.':
                #    continue #skip hidden directories        
                dirname = root.replace(basedir, '')
                for f in files:
                    fzip.write(root + '/' + f, dirname + '/' + f)
        fzip.close()
        print(f"Written {zippath} to disk!")
    else:
        raise ValueError("invalid dirpath")

# paks
zip_dir("entity", "entity.pak")
zip_dir("map", "map.pak")
zip_dir("sound", "sound.pak")
zip_dir("texture", "texture.pak")
zip_dir(["interface", "properties", "script", "set", "SKINCHANGES", "WIP"], "game.pak")