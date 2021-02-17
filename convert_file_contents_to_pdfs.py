from os import walk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.backends.backend_pdf
from fpdf import FPDF
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
if __name__ == '__main__':
    f = []
    pdf = FPDF()
    pdf1_filename = "bbd16.pdf"
    for (dirpath, dirnames, filenames) in walk("docs_to_convert"):
        for image in filenames:
            if image.split(".")[-1] =="png":
                rgba = Image.open(f"{dirpath}/{image}")
                rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
                rgb.paste(rgba, mask=rgba.split()[3]) 
                draw = ImageDraw.Draw(rgb)
                draw.text((20, 20), f'{image}',fill=(0,0,0))
                f.append(rgb)
        break
    rgb.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=f)