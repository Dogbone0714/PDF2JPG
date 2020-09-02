import tkinter as tk
import tempfile
from tkinter import filedialog
from tkinter import messagebox
from pdf2image import convert_from_path, convert_from_bytes

root = tk.Tk()
root.title("PDF To JPG By HHK")
canvas1 = tk.Canvas(root, width=300, height=250, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='PDF To JPG Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 50, window=label1)


def GetPDF():
    images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())


browseButton_PDF = tk.Button(text="      Import   PDF   File     ", command=getPDF, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 120, window=browseButton_PDF)

root.mainloop()
