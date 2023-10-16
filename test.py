import os
from pdf2image import convert_from_path

# Path to the PDF file
folder_path = r"C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\23-07-09"
def convert_pdf_to_jpeg(filename):
    try:
        pages = convert_from_path(os.path.join(folder_path, filename), poppler_path=r'C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\poppler-0.68.0_x86\poppler-0.68.0\bin')

        for i, image in enumerate(pages):
            image.save(os.path.join(r'C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\images_2', f'{filename[:-4]}_{i+1}.jpg'), 'JPEG')

    except Exception as e:
        print(f"Error processing PDF file:  {filename}")
        print(f"Error message: {str(e)}")
        return
pdf_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".pdf")]

# Convert each PDF file in the list to a list of image pages using pdf2image
for filename in pdf_files:
    convert_pdf_to_jpeg(filename)