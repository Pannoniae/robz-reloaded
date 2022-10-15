import zipfile
import subprocess
import os
import shlex
from zipfile import *
import shutil

# delete git shit
try:
    shutil.rmtree(".git")
except:
    print("Couldn't delete git folder, remove it manually")

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
subprocess.call(shlex.split("D:/path/7z/7z.exe a entity.pak ./entity -mx=7 -mmt=16 -sdel -tzip"))
subprocess.call(shlex.split("D:/path/7z/7z.exe a map.pak ./map -mx=7 -mmt=16 -sdel -tzip"))
subprocess.call(shlex.split("D:/path/7z/7z.exe a sound.pak ./sound -mx=7 -mmt=16 -sdel -tzip"))
subprocess.call(shlex.split("D:/path/7z/7z.exe a texture.pak ./texture -mx=7 -mmt=16 -sdel -tzip"))
subprocess.call(shlex.split("D:/path/7z/7z.exe a game.pak ./interface -i!./properties -i!./script -i!./set -mx=7 -mmt=16 -sdel -tzip"))
#zip_dir("entity", "entity.pak")
#zip_dir("map", "map.pak")
#zip_dir("sound", "sound.pak")
#zip_dir("texture", "texture.pak")
#zip_dir(["interface", "properties", "script", "set"], "game.pak")