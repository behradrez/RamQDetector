import ocrmypdf


def ocr_file(file: str):
    name = 'OCR' + file.split('/')[-1]
    ocrmypdf.ocr(file, name, deskew=True)
    return name


if __name__ == "__main__":
    ocrmypdf.ocr('input.pdf', 'output.pdf', deskew=True)
