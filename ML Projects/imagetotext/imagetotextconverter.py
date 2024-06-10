import logging
import aspose.words as aw
import os

from PIL import Image
from pytesseract import pytesseract

# Creating an object
logging.basicConfig(level=logging.INFO)
img = "1.png"
file_name = "test1.docx"

def process_images():
    files = [f for f in os.listdir("input") if os.path.isfile(os.path.join("input", f))]
    print(files)
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    font = builder.font
    font.size = 14
    for fx in files:
        print(fx)        
        text=read_images(os.path.join("input", fx))
        builder.write(text)
        #create_wordfile(text, file_name)
    doc.save(file_name)


def read_images(img):
    logging.info("Image Reading Started")    
    return pytesseract.image_to_string(Image.open(img))


def create_wordfile(text, file_name):
    logging.info("Word Processing start")
    # logging.info(text)

    # create document object
    doc = aw.Document()

    # create a document builder object
    builder = aw.DocumentBuilder(doc)

    # create font
    font = builder.font
    font.size = 14

    # add text to the document
    builder.write(text)

    # save document
    doc.save(file_name)

    logging.info("::::COMPILITED:::::")
    return


#text = read_images(img)
#create_wordfile(text, file_name)
process_images()
