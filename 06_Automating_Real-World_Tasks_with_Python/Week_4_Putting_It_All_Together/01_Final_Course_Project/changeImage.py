#!/usr/bin/env python3

import os
from PIL import Image


def is_image(file_path):
    """Check if the file is a valid image."""
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False


def process_images(source_folder):
    """
    Process images in the source folder.
    
    Convert images to RGB format, resize them to 600x400 pixels,
    and save them as JPEG files.
    """
    image_files = [f for f in os.listdir(
        source_folder) if is_image(os.path.join(source_folder, f))]

    # We process each file inside the source folder.
    for image_file in image_files:
        input_path = os.path.join(source_folder, image_file)

        # Replace the extension with .jpeg.
        filename, _ = os.path.splitext(image_file)
        output_path = os.path.join(source_folder, filename + '.jpeg')

        with Image.open(input_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize((600, 400))
            try:
                img.save(output_path, 'JPEG')
            except Exception as e:
                print(f"Error saving {output_path}: {e}")


# Variable with the relative path to folder
source_folder = 'supplier-data/images'

# We obtain the absolute path to the folder
source_folder = os.path.abspath(source_folder)

# We call the function to process the images.
process_images(source_folder)
