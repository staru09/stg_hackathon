from pdf2image import convert_from_path
import os

def pdf_to_jpg(pdf_path, output_folder, dpi=300):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = convert_from_path(pdf_path, dpi=dpi)

    for i, image in enumerate(images):
        jpg_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        image.save(jpg_path, 'JPEG')
        print(f"Saved {jpg_path}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\91745\OneDrive\Desktop\Anaconda\ResumeScreening - PreRequisites\Sample Forms\Sample Forms\PEC Hackathon-2.pdf'
    output_folder = r'C:\Users\91745\OneDrive\Desktop\Anaconda\output_images\hack2.jpg'
    
    pdf_to_jpg(pdf_path, output_folder)
