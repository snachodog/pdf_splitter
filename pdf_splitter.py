import os
import shutil
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_pages(processed_folder):
    # Check if the processed folder exists in the current directory, if not, create it
    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    # Iterate over all PDF files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            # Read the PDF file
            with open(filename, 'rb') as infile:
                reader = PdfReader(infile)
                num_pages = len(reader.pages)
                
                # Check if PDF has more than 1 page
                if num_pages > 1:
                    # Split each page into a separate PDF
                    for i in range(num_pages):
                        writer = PdfWriter()
                        writer.add_page(reader.pages[i])
                        
                        # Generate new filename for the split PDF
                        split_filename = f"split_{i+1}_{filename}"
                        split_filepath = os.path.join(processed_folder, split_filename)
                        
                        # Write the split PDF to the processed folder
                        with open(split_filepath, 'wb') as outfile:
                            writer.write(outfile)
                
                # Move the original PDF to the processed folder after splitting or if it's single-paged
                shutil.move(filename, os.path.join(processed_folder, filename))

# Define the name of the processed folder
processed_folder = 'Processed'

# Run the function
split_pdf_pages(processed_folder)
