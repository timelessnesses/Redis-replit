import os
import shutil

with open("replit.nix") as fp: # Told nix about we need this specific version of python
    fp.write("""
{ pkgs }: {
    deps = [
        pkgs.python310
    ];
}
             """)

os.chdir("./redis-7.0-rc1/src") # Change Directory

for file in os.listdir(): # List all file and move them with conditions
    if "." not in file and file not in ("commands","modules","Makefile"):
        shutil.move(file,"../../bin")

print("Done")