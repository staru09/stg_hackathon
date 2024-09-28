from PIL import Image
import pytesseract

image_path = r'C:\Users\91745\OneDrive\Desktop\Anaconda\ResumeScreening - PreRequisites\1st_form.jpg'
img = Image.open(image_path)

extracted_text = pytesseract.image_to_string(img)
extracted_text
