import sys
import os
from PIL import Image

# grab 1st and 2nd argument
image_folder= sys.argv[1]
output_folder= sys.argv[2]

#check if new/ exists ,if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the pokedox
for file in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{file}')
    clean_name=os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png','png')





