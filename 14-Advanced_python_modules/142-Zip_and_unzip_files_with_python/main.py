import os

zz = "####################################################################"
print(zz)

f = open("file1.txt", "w+")
f.write("One File")
f.close()

f = open("file2.txt", "w+")
f.write("Two Files")
f.close()

import zipfile
comp_file = zipfile.ZipFile("comp_file.zip", "w", zipfile.ZIP_DEFLATED)
comp_file.write("file1.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("file2.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content")
zip_obj.close()

import os
print(os.getcwd())
print(zz)

import shutil
dir_to_zip = "extracted_content"
ouput_filname = "example"
shutil.make_archive(ouput_filname, "zip", dir_to_zip)
shutil.unpack_archive("example.zip", "final_unzip", "zip")