import os
import shutil
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_pages(processed_folder):
    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            file_path = os.path.join('.', filename)  # Added for clarity
            with open(file_path, 'rb') as infile:
                reader = PdfReader(infile)
                num_pages = len(reader.pages)

                if num_pages > 1:
                    for i in range(num_pages):
                        writer = PdfWriter()
                        writer.add_page(reader.pages[i])

                        split_filename = f"split_{i+1}_{filename}"
                        split_filepath = os.path.join(processed_folder, split_filename)

                        with open(split_filepath, 'wb') as outfile:
                            writer.write(outfile)

            # Attempt to move the file after ensuring it's closed
            shutil.move(file_path, os.path.join(processed_folder, filename))

processed_folder = 'Processed'
split_pdf_pages(processed_folder)
