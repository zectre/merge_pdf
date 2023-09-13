import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(input_folder, output_file):
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]
    pdf_files.sort()  # Sort the files to merge them in a specific order; remove this line if unnecessary

    if not pdf_files:
        print(f"No PDF files found in the specified folder: {input_folder}")
        sys.exit()

    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(os.path.join(input_folder, pdf))

    merger.write(output_file)
    merger.close()

    print(f"Merged {len(pdf_files)} PDFs into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <input_folder> <output_file>")
        sys.exit()

    input_folder = sys.argv[1]
    output_file = sys.argv[2]

    merge_pdfs_in_folder(input_folder, output_file)
