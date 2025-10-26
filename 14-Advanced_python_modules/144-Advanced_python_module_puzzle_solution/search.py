zz = "############################################################"
print(zz)

import re
pattern = r"(\d{3})-(\d{3})-(\d{4})"

def search(file, pattern=r"(\d{3})-(\d{3})-(\d{4})"):
    f = open(file, "r")
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        pass
import os
results = []
for folder, sub_folders, files in os.walk(os.getcwd()+"/extracted_content"):
    for f in files:
        full_path = folder+"/"+f
        results.append(search(full_path))
for r in results:
    if r != None:
        print(r.group())
print(zz)