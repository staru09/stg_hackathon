from pdf2image import convert_from_path
import os

def pdf_to_jpg(input_folder, output_folder, dpi=300):
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, pdf_file)
            images = convert_from_path(pdf_path, dpi=dpi)

            for i, image in enumerate(images):
                jpg_path = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_page_{i + 1}.jpg")
                image.save(jpg_path, 'JPEG')
                print(f"Saved {jpg_path}")

if __name__ == "__main__":
    input_folder = '/home/aru/Desktop/stg_hackathon/data/sample forms'
    output_folder = '/home/aru/Desktop/stg_hackathon/data/form images'
    
    pdf_to_jpg(input_folder, output_folder)
