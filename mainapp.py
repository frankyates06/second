import streamlit as st
from PyPDF2 import PdfFileReader, PdfFileMerger
import io

st.title('PDF Merger')

# Allow users to upload PDF files
pdf_file1 = st.file_uploader("Choose the first PDF file", type=["pdf"])
pdf_file2 = st.file_uploader("Choose the second PDF file", type=["pdf"])

if pdf_file1 and pdf_file2:
    # Read the uploaded PDF files
    pdf1 = PdfFileReader(pdf_file1)
    pdf2 = PdfFileReader(pdf_file2)

    # Initialize PdfFileMerger object
    merger = PdfFileMerger()

    # Append the PDF files
    merger.append(pdf1)
    merger.append(pdf2)

    # Write out the merged PDF to a bytes buffer
    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merged_pdf.seek(0)

    # Let the user download the merged PDF
    st.download_button(
        label="Download Merged PDF",
        data=merged_pdf,
        file_name="merged.pdf",
        mime="application/pdf"
    )
