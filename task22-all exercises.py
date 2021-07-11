'''from PIL import Image
img = Image.open('C:\\Users\\vaishnav\\Desktop\\ikigai.png')
img.show()
print(img.format)
print(img.mode)'''
# Exercise 2
from PyPDF2 import PdfFileMerger, PdfFileReader
mergedObject = PdfFileMerger()
for fileNumber in range(1, 117):
    mergedObject.append(PdfFileReader('C:\\Users\\vaishnav\\Desktop\\hpp' + str(fileNumber) + '.pdf', 'rb'))
mergedObject.write("mergedfilesoutput.pdf")
# Exercise 3


