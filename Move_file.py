import os
import shutil

from_dir="C:/Users/shaan/Downloads"
to_dir="C:/Users/shaan/Desktop/python/dowload"

list_of_file=os.listdir()
print(list_of_file)

for file_name in list_of_file:
    name,extension= os.path.splitext(file_name)
    print(name)
    print(extension)