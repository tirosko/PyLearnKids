from PIL import Image
import os
import sys
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True  # Fixes truncated image loading issues


def fix_image_srgb_profile(file_path):
    img = Image.open(file_path)
    img.save(file_path, icc_profile=None)


fix_image_srgb_profile(os.path.join(
    os.path.dirname(__file__), 'catgirl.png'))
