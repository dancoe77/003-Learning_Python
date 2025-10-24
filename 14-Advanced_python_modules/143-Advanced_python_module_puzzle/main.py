zz = "####################################################################"
print(zz)

import shutil
dir_to_zip = "extracted_content"
ouput_filname = "unzip-me-for-instructions"
shutil.make_archive(ouput_filname, "zip", dir_to_zip)

import zipfile
comp_file = zipfile.ZipFile("unzip-me-for-instructions.zip")
comp_file.extractall("first_unzip")
comp_file.close()
print("Extraction completed")
print(zz)

shutil.unpack_archive("unzip-me-for-instructions.zip", "final_unzip", "zip")
print("Second Extraction completed")
print(zz)