import sys
from tkinter import filedialog
import tkinter as tk
from src import ExcelReader, RamQDetector


def functions():
    path_to_file = filedialog.askopenfilename(title="RamQ Complete 1.0")
    if ".xlsx" in path_to_file[-5:]:
        print('Summarizing Yearly Patient Visits Excel File')
        ExcelReader.alt_main(path_to_file)
    elif ".txt" in path_to_file[-4:]:
        print("Listing Daily Patient Visits Text File")
        RamQDetector.TEXT_to_TEXT(path_to_file)
    elif ".pdf" in path_to_file[-4:]:
        print("Listing Daily Patient Visits from PDF")
        RamQDetector.PDF_to_TEXT(path_to_file)
    elif len(path_to_file) == 0:
        sys.exit()
    else:
        print("Invalid File, Choose Another File")
        functions()
    print("Function Complete!")


def main():
    window = tk.Tk()
    window.title("RamQ Functions: Complete Edition")
    window.minsize(400, 400)
    window.maxsize(400, 400)

    start_button = tk.Button(master=window, command=functions, text='Start', pady=30, padx=30, fg='White', bg='Green')
    start_button.place(x=150, y=150)

    window.mainloop()


if __name__ == '__main__':
    main()
