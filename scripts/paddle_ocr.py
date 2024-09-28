from paddleocr import PaddleOCR
import os
import fitz

def ocr_single_page_pdf(pdf_path, output_folder):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=1)
    result = ocr.ocr(pdf_path, cls=True)
    extracted_text = []
    for res in result:
        if res is None: 
            print(f"[DEBUG] Empty page detected, skipping.")
            continue
        for line in res:
            text = line[1][0] 
            extracted_text.append(text)

    pdf_filename = os.path.basename(pdf_path)
    txt_filename = f"{os.path.splitext(pdf_filename)[0]}.txt"
    txt_path = os.path.join(output_folder, txt_filename)

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(extracted_text))

    print(f"Processed and saved text for {pdf_filename} to {txt_filename}")


if __name__ == "__main__":
    pdf_path = r'C:\Users\91745\OneDrive\Desktop\Anaconda\ResumeScreening - PreRequisites\Sample Forms\Sample Forms\PEC Hackathon-1.pdf'  # Path to your PDF file
    output_folder = r'C:\Users\91745\OneDrive\Desktop\Anaconda\ResumeScreening - PreRequisites\Sample Forms\Sample Forms\PEC Hackathon-1.txt'  # Folder to save the .txt file

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ocr_single_page_pdf(pdf_path, output_folder)
