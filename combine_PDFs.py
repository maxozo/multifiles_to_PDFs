
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
from os import walk
import shutil
import os
from pdf2image import convert_from_path, convert_from_bytes 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

if __name__ == '__main__':
    pdf1_filename = "QCs3.pdf"
    merger = PdfFileMerger()
    writer = PdfFileWriter()
    try:
        shutil.rmtree('tmp')
    except:
        _=""
    os.mkdir('tmp')
    for (dirpath, dirnames, filenames) in walk("/Users/mo11/work/Documents/Stephens_exp/QC/QCs2"):
        count=0
        for image in filenames:

            if image.split(".")[-1] =="pdf":
                # pages = PdfFileReader(f"{dirpath}/{image}")
                # for page in range(pages.getNumPages()):
                #     input_page = pages.getPage(page)
                #     input_page.scaleBy(0.5)
                #     writer.addPage(input_page)       
                # count+=1
                # if count>4:
                #     break
                merger.append(f"{dirpath}/{image}",bookmark=f"{dirpath}/{image}", import_bookmarks=True)
            elif image.split(".")[-1] =="png":
                f = []
                rgba = Image.open(f"{dirpath}/{image}")
                rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
                rgb.paste(rgba, mask=rgba.split()[3]) 
                draw = ImageDraw.Draw(rgb)
                # draw.text((20, 20), f'{image}',fill=(0,0,0))
                f.append(rgb)
                rgb.save(f"tmp/{image}.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=f)
                merger.append(f"tmp/{image}.pdf",bookmark=f"{dirpath}/{image}", import_bookmarks=True)
        break
    merger.write(pdf1_filename)
    merger.close()
    shutil.rmtree('tmp')