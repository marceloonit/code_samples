from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

fp = open('teste.txt', 'w')

tool = pyocr.get_available_tools()[0]
#lang = tool.get_available_languages()[1]


req_image = []
final_text = []


image_pdf = Image(filename="./teste.pdf", resolution=300)
image_jpeg = image_pdf.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

for img in req_image: 
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
#        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    print(txt, file=fp)
#    final_text.append(txt)

fp.close()

#import code
#code.interact(local=locals())
