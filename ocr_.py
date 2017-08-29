from asprise_ocr_api import *

ocr = Ocr()
ocr.start_engine("eng")  # deu, fra, por, spa - more than 30 languages are supported
text = ocr.recognize(
"teste.pdf",  # gif, jpg, pdf, png, tif, etc.
OCR_PAGES_ALL,  # the index of the selected page
-1, -1, -1, -1,  # you may optionally specify a region on the page instead of the whole page
OCR_RECOGNIZE_TYPE_TEXT,  # recognize type: TEXT, BARCODES or ALL
OCR_OUTPUT_FORMAT_PLAINTEXT  # output format: TEXT, XML, or PDF
)
print("Result: ", text)

# ocr.recognize(more_images...)

ocr.stop_engine()
