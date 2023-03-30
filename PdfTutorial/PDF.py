import PyPDF2

file = PyPDF2.PdfFileReader(open('CFD.pdf', 'rb'))
page = file.getPage(5)
page.rotateClockwise(180)
writer = PyPDF2.PdfFileWriter()
writer.addPage(page)
with open('tilt.pdf', 'wb') as new_file:
    writer.write(new_file)
