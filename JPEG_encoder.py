from PIL import Image
import os

def compress_image(input_path, output_path, quality=75):
    """
    Opens an image, compresses it using the specified JPEG quality,
    and saves it to a new path.

    :param input_path: Path to the source image file.
    :param output_path: Path for the compressed output file.
    :param quality: An integer from 1 (worst) to 95 (best). Default is 75.
    """
    try:
        with Image.open(input_path) as img:
            # The 'save' method handles the compression
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            print(f"Image successfully compressed and saved to {output_path}")
            print(f"Original size: {os.path.getsize(input_path)} bytes")
            print(f"Compressed size: {os.path.getsize(output_path)} bytes")
    except IOError as e:
        print(f"Error processing image: {e}")

# Example Usage:
# Replace 'original_image.jpg' with your actual image file path
# The quality is set to 50 for a noticeable compression


for fig in os.listdir("recon_JPEG"):
  os.remove(f'recon_JPEG/{fig}')
for fig in os.listdir("compressed_JPEG"):
  os.remove(f'compressed_JPEG/{fig}')



for fig in os.listdir("valid"):
  input_file = f'valid/{fig}'
  output_file = f'compressed_JPEG/compressed_{fig}'
  compress_image(input_file, output_file, quality=5)