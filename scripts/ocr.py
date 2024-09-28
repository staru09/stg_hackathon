import os
from PIL import Image
import pytesseract

folder_path = r'C:\Users\91745\OneDrive\Desktop\stg_hackathon\data\form images'

output_folder = r'C:\Users\91745\OneDrive\Desktop\stg_hackathon\data\output'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(folder_path, filename)
        
        img = Image.open(image_path)
        
        extracted_text = pytesseract.image_to_string(img)
        
        output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        
        with open(output_file, 'w') as f_out:
            f_out.write(extracted_text)
        
        print(f"Text extracted and saved to {output_file}")

print("Text extraction complete for all images.")
