from tkinter import filedialog
import PyPDF2
from utils import AddOCR

def scan_and_write(text_sample):
    num_id = 0
    written_file_name = ''
    for range_text in range(60):
        year = text_sample[29 + range_text:33 + range_text]
        old_date = text_sample[32:33 + range_text]
        if str.isdigit(year):
            date = old_date.replace(" ", "_")
            written_file_name = "NAM_Facturation_" + date
    new_text = text_sample.replace(" ", "")

    w = open(written_file_name + ".txt", "w")
    w.write(written_file_name + '\n' * 2)

    for i in range(len(new_text)):
        name = new_text[i:i + 4]
        numbers = new_text[i + 4:i + 12]
        if str.isalpha(name) and str.isdigit(numbers):
            w.write(new_text[i:i + 12] + "," + "\n")
            num_id += 1

    w.write("\n#" + str(num_id) + " RAMQ IDs")
    w.close()

    return written_file_name


def PDF_to_TEXT(path_to_file=None):
    if path_to_file is None:
        path_to_file = filedialog.askopenfilename(title='RamQ Detector 5.0: Choose a PDF File')

    pdf_File = PyPDF2.PdfReader(path_to_file)
    pages = pdf_File.pages

    text_sample = ""
    for page in pages:

        text = page.extract_text()
        text_sample += text

    if text_sample=="":
        name = AddOCR.ocr_file(path_to_file)
        return PDF_to_TEXT(name)

    return scan_and_write(text_sample)


def TEXT_to_TEXT(path_to_file=None):
    if path_to_file is None:
        path_to_file = filedialog.askopenfilename(title='RamQ Detector 4.0,سلام پدرجان عزیزم , الله اکبر')

    f = open(path_to_file, "r")
    text_sample = f.read()
    f.close()

    '''num_id = 0
    written_file_name=''
    for range_text in range(60):
        year = text_sample[29+range_text:33+range_text]
        old_date = text_sample[32:33+range_text]
        if str.isdigit(year):
            date = old_date.replace(" ", "_")
            written_file_name = "NAM_Facturation_" + date
    new_text = text_sample.replace(" ","")

    w = open(written_file_name+".txt", "w")
    w.write(written_file_name+'\n'*2)
    
    for i in range(len(new_text)):
        name = new_text[i:i+4]
        numbers = new_text[i+4:i+12]
        if str.isalpha(name) and str.isdigit(numbers):
            w.write(new_text[i:i+12] + "," + "\n")
            num_id += 1
    
    w.write("\n#"+ str(num_id) + " RAMQ IDs")
    w.close()
    '''
    return scan_and_write(text_sample)
