import os
import PyPDF2

def is_pdf_openable(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Attempt to determine the number of pages
            num_pages = len(pdf_reader.pages)
        return True  # PDF was successfully opened
    except Exception as e:
        print(f"Error opening PDF '{pdf_path}': {str(e)}")
        return False  # PDF could not be opened

def delete_unopenable_pdfs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            if not is_pdf_openable(pdf_path):
                print(f"Deleting unopenable PDF: {pdf_path}")
                os.remove(pdf_path)

if __name__ == "__main__":
    current_folder = os.getcwd()
    print(f"Searching for unopenable PDFs in the current folder: {current_folder}")
    
    delete_unopenable_pdfs(current_folder)
    print("Unopenable PDFs have been deleted.")
