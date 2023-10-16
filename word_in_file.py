import os
import glob
import shutil


def move_pdfs_with_word(keyword, destination_directory):
    # Use glob to get all files with .pdf extension
    pdf_files = glob.glob('pdfs/*.pdf')
    # Filter files based on the keyword in the name
    filtered_pdfs = [
        file for file in pdf_files if keyword.lower() in file.lower()]
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    # Move matching PDFs to the destination directory
    for pdf in filtered_pdfs:
        destination_path = os.path.join(destination_directory, pdf[5:])
        shutil.copy(pdf, destination_path)


keyword_to_search = 'professor'
destination_directory_path = 'professors'

move_pdfs_with_word(keyword_to_search, destination_directory_path)
