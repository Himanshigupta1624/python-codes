import PyPDF2
pdfiles=["himanshi gupta(resume).pdf","himanshi gupta 1.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')    