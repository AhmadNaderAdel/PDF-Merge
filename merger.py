import os
import re
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()


files = os.listdir(os.curdir)

for file in files:
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)

merger.write("result.pdf")
merger.close()


