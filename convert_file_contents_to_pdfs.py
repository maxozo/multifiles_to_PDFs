from os import walk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.backends.backend_pdf
from fpdf import FPDF
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import shutil
from PyPDF2 import PdfFileMerger
if __name__ == '__main__':
    os.mkdir('tmp')
    merger = PdfFileMerger()
    pdf1_filename = "QCs1.pdf"
    for (dirpath, dirnames, filenames) in walk("/Users/mo11/work/Documents/Stephens_exp/QC/QCs1"):
        count=0
        for image in filenames:
            count+=1
            if image.split(".")[-1] =="png":
                f = []
                rgba = Image.open(f"{dirpath}/{image}")
                rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
                rgb.paste(rgba, mask=rgba.split()[3]) 
                draw = ImageDraw.Draw(rgb)
                # draw.text((20, 20), f'{image}',fill=(0,0,0))
                f.append(rgb)
                rgb.save(f"tmp/{image}.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=f)
                merger.append(f"tmp/{image}.pdf",bookmark=f"{dirpath}/{image}", import_bookmarks=True)
            # if count>=4:
            #     break
        break
    merger.write(pdf1_filename)
    merger.close()
    shutil.rmtree('tmp')

    