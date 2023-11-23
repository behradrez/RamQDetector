from src import FileHandler
from tkinter import filedialog


def main_program(file_path=None):
    file_Name = input("Save new EXCEL file as: ")
    while len(file_Name) == 0:
        file_Name = input("Enter a file name\nSave new EXCEL file as: ")

    path_to_file = filedialog.askopenfilename(title="RAMQ Excel Sorter 1.0")

    FileHandler.FileHandler(path_to_file, file_Name)


def alt_main(with_path):
    file_Name = input("Save new Excel File as: ")
    while len(file_Name) == 0:
        file_Name = input("Enter a file name\nSave new EXCEL file as: ")

    FileHandler.FileHandler(with_path, file_Name)


if __name__ == '__main__':
    main_program()
