import os
import sys
from PIL import Image

JPG_folder = sys.argv[1]
output_folder = sys.argv[2]
file_exist = os.path.exists(output_folder)

if not file_exist:
    os.makedirs(output_folder)

for JPG_file in os.listdir(JPG_folder):
    if JPG_file.endswith(".jpg"):
        img = Image.open(f'{JPG_folder}{JPG_file}')
        clean_name = os.path.splitext(JPG_file)[0]
        img.save(f'{output_folder}{clean_name}.png', 'png')
        print('all done')
