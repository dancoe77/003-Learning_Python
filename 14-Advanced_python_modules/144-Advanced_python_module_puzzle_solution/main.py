zz = "###########################################################"
print(zz)

import zipfile
zip_obj = zipfile.ZipFile("unzip-me-for-instructions.zip", "r")
zip_obj.extractall("extracted_content")
zip_obj.close()

print("Extraction complete")
print(zz)