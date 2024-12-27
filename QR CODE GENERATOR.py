Here is the full code without comments:

python
import pyqrcode
import png
from tkinter import *

base = Tk()
base.geometry("400x200")
base.title("QR Code Generator")

data = StringVar()
dataEntry = Entry(textvariable=data, width=30)
dataEntry.place(x=80, y=50)

def get_code():
    data_var = data.get()
    qr = pyqrcode.create(str(data_var))
    qr.png('image1.png', scale=6)

generate_button = Button(base, text="Generate QR Code", command=get_code)
generate_button.place(x=140, y=100)

base.mainloop()
