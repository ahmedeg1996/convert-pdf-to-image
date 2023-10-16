import os
from pdf2image import convert_from_path
import multiprocessing as mp

# Set the folder path where the PDF files are located
folder_path = r"C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\23-07-09"

def convert_pdf_to_jpeg(filename):
   
    # Convert the PDF file to a list of image pages using pdf2image
    pages = convert_from_path(os.path.join(folder_path, filename), poppler_path=r'C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\poppler-0.68.0_x86\poppler-0.68.0\bin')
    
    # Your image processing code...
    # Save each page of the PDF as a separate image file
    for i, image in enumerate(pages):
        # image_size = image.size
        # image_input = PrepareImage(image)
        # predicted = np.where(Model.predict(image_input) > 0.9, 255, 0)
        # mask_predicted = np.array(np.squeeze(predicted[0]), dtype='uint8')
        # mask_predicted = cv2.resize(mask_predicted, (image_size[1], image_size[0]), interpolation=cv2.INTER_LINEAR)
        # elements_count = collections.Counter(predicted[0].reshape(1, 256*256)[0])
        # print(elements_count[255])
        # if elements_count[255] > 350:
        #     image.save(os.path.join(r'C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\IDs_2', f'{filename[:-4]}_{i+1}.jpg'), 'JPEG')
        # else:
        image.save(os.path.join(r'C:\Users\v23ASayed2\Desktop\Vodafone\National_IDs_splitting\images', f'{filename[:-4]}_{i+1}.jpg'), 'JPEG')



pdf_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".pdf")]

# Convert each PDF file in the list to a list of image pages using pdf2image
for filename in pdf_files:
    convert_pdf_to_jpeg(filename)
