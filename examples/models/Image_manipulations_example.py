"""
example_image_processing.py

This script demonstrates how to perform various image processing tasks using 
the Pillow and OpenCV libraries. The tasks include reading and saving images in 
different color spaces, resizing images using different algorithms, and basic 
image manipulations like rotate, flip, grayscale conversion, brightness, and 
contrast adjustments.

Requirements:
- Pillow
- OpenCV
- NumPy

Install required packages:
pip install pillow opencv-python numpy
"""

from PIL import Image, ImageEnhance, ImageOps
import cv2
import os

# --------------------------------------------
# Example Usage with Pillow (PIL) Library
# --------------------------------------------

# 1. Read and Save Image in Different Color Spaces
image_path = "../resources/Skyline-Chicago.jpg"
output_dirpath = "./output/"
os.makedirs(output_dirpath, exist_ok=True)

try:
    # Read an image in RGB
    image_rgb = Image.open(image_path).convert("RGB")
    image_rgb.save(os.path.join(output_dirpath, "output_rgb_pillow.jpg"))
    print("Saved RGB image using Pillow.")

    # Read an image in RGBA
    image_rgba = Image.open(image_path).convert("RGBA")
    image_rgba.save(os.path.join(output_dirpath, "output_rgba_pillow.png"))
    print("Saved RGBA image using Pillow.")

    # Read an image in CMYK
    image_cmyk = Image.open(image_path).convert("CMYK")
    image_cmyk.save(os.path.join(output_dirpath, "output_cmyk_pillow.jpg"))
    print("Saved CMYK image using Pillow.")

except Exception as e:
    print(f"Error handling image with Pillow: {e}")

# 2. Image Resizing with Different Algorithms
try:
    # Resize image using different algorithms
    image_resized_nearest = image_rgb.resize((200, 200), Image.NEAREST)
    image_resized_nearest.save(os.path.join(output_dirpath, "resized_nearest_pillow.jpg"))

    image_resized_lanczos = image_rgb.resize((200, 200), Image.LANCZOS)
    image_resized_lanczos.save(os.path.join(output_dirpath, "resized_lanczos_pillow.jpg"))
    print("Resized images using different algorithms with Pillow.")

except Exception as e:
    print(f"Error resizing image with Pillow: {e}")

# 3. Basic Image Manipulations
try:
    # Rotate the image
    image_rotated = image_rgb.rotate(90)
    image_rotated.save(os.path.join(output_dirpath, "rotated_pillow.jpg"))

    # Flip the image
    image_flipped = ImageOps.mirror(image_rgb)
    image_flipped.save(os.path.join(output_dirpath, "flipped_pillow.jpg"))

    # Convert to grayscale
    image_gray = ImageOps.grayscale(image_rgb)
    image_gray.save(os.path.join(output_dirpath, "grayscale_pillow.jpg"))

    # Adjust brightness
    enhancer_brightness = ImageEnhance.Brightness(image_rgb)
    image_bright = enhancer_brightness.enhance(1.5)
    image_bright.save(os.path.join(output_dirpath, "brightness_pillow.jpg"))

    # Adjust contrast
    enhancer_contrast = ImageEnhance.Contrast(image_rgb)
    image_contrast = enhancer_contrast.enhance(1.5)
    image_contrast.save(os.path.join(output_dirpath, "contrast_pillow.jpg"))
    print("Performed basic manipulations using Pillow.")

except Exception as e:
    print(f"Error manipulating image with Pillow: {e}")

# --------------------------------------------
# Example Usage with OpenCV Library
# --------------------------------------------

# 1. Read and Save Image in Different Color Spaces
try:
    # Read an image in BGR (OpenCV default)
    image_bgr = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert to RGB
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(output_dirpath, "output_rgb_opencv.jpg"), cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
    print("Saved RGB image using OpenCV.")

    # Convert to RGBA
    image_rgba = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGBA)
    cv2.imwrite(os.path.join(output_dirpath, "output_rgba_opencv.png"), image_rgba)
    print("Saved RGBA image using OpenCV.")

    # OpenCV does not natively support CMYK; if needed, use Pillow to convert to CMYK
except Exception as e:
    print(f"Error handling image with OpenCV: {e}")

# 2. Image Resizing with Different Algorithms
try:
    # Resize image using different algorithms
    image_resized_nearest = cv2.resize(image_rgb, (200, 200), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(
        os.path.join(output_dirpath, "resized_nearest_opencv.jpg"),
        cv2.cvtColor(image_resized_nearest, cv2.COLOR_RGB2BGR),
    )

    image_resized_lanczos = cv2.resize(image_rgb, (200, 200), interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite(
        os.path.join(output_dirpath, "resized_lanczos_opencv.jpg"),
        cv2.cvtColor(image_resized_lanczos, cv2.COLOR_RGB2BGR),
    )
    print("Resized images using different algorithms with OpenCV.")

except Exception as e:
    print(f"Error resizing image with OpenCV: {e}")

# 3. Basic Image Manipulations
try:
    # Rotate the image
    image_rotated = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(output_dirpath, "rotated_opencv.jpg"), cv2.cvtColor(image_rotated, cv2.COLOR_RGB2BGR))

    # Flip the image
    image_flipped = cv2.flip(image_rgb, 1)
    cv2.imwrite(os.path.join(output_dirpath, "flipped_opencv.jpg"), cv2.cvtColor(image_flipped, cv2.COLOR_RGB2BGR))

    # Convert to grayscale
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(os.path.join(output_dirpath, "grayscale_opencv.jpg"), image_gray)

    # Adjust brightness and contrast (brightness with beta, contrast with alpha)
    image_bright = cv2.convertScaleAbs(image_rgb, alpha=1.0, beta=50)  # Brightness adjustment
    cv2.imwrite(os.path.join(output_dirpath, "brightness_opencv.jpg"), cv2.cvtColor(image_bright, cv2.COLOR_RGB2BGR))

    image_contrast = cv2.convertScaleAbs(image_rgb, alpha=1.5, beta=0)  # Contrast adjustment
    cv2.imwrite(os.path.join(output_dirpath, "contrast_opencv.jpg"), cv2.cvtColor(image_contrast, cv2.COLOR_RGB2BGR))
    print("Performed basic manipulations using OpenCV.")

except Exception as e:
    print(f"Error manipulating image with OpenCV: {e}")
