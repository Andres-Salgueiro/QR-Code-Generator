import qrcode
from tkinter import *

#      2. EXE

#Function
def Generate():
   qr = qrcode.QRCode(box_size=20,
                      border=2)
   qr.add_data(link.get())
   qr.make(fit=True)
   img = qr.make_image()
   img.save("qr.png")


#Window
window = Tk()
window.title("QR Code Generator")
window.geometry("480x60")

#Link Entry
link = Entry(window,
             width="50")
link.pack()

#Button
Generate = Button(window,
                  text="Generate",
                  command=Generate)
Generate.pack()


window.mainloop()