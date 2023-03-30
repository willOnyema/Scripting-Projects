import PyPDF2

watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
file = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()
for i in range((file.getNumPages())):
    page = file.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)
    with open(f'watermarked.pdf', 'wb') as fp:
        writer.write(fp)
