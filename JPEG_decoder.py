from PIL import Image
import os


for fig in os.listdir("compressed_JPEG"):
  if not fig.endswith(".png"):
    continue
  f = Image.open(f'compressed_JPEG/{fig}')
  f = f.save(f'recon_JPEG/{fig[11:]}')