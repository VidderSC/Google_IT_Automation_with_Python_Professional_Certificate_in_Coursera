#!/usr/bin/env python3

import os
from PIL import Image


def is_image(file_path):
    # We check if the file is an image and return
    # True if it is,
    # False if it's not.
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False


def process_images(source_folder, destination_folder):
    # We process the images and save them as .jpg,
    # at a size of 128x128,
    # rotated 90 degrees clockwise.

    # We get the list of images, since the files in the source folder don't have an extension, we check each file to make sure that it's an image before adding them to the list.
    image_files = [f for f in os.listdir(
        source_folder) if is_image(os.path.join(source_folder, f))]

    # We process each file inside the source folder.
    for image_file in image_files:
        input_path = os.path.join(source_folder, image_file)
        output_path = os.path.join(
            destination_folder, image_file + '.jpg')

        with Image.open(input_path) as img:

            if img.mode != 'RGB':
                img = img.convert('RGB')

            img = img.rotate(-90)
            img = img.resize((128, 128))

            img.save(output_path, 'JPEG')


# Variables with the relative paths to folders
source_folder = 'images'
destination_folder = '/opt/icons'

# We obtain the absolute paths to the folders
source_folder = os.path.abspath(source_folder)
destination_folder = os.path.abspath(destination_folder)

# We create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# We call the function to process the images.
process_images(source_folder, destination_folder)
