import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("URL Shortener")
root.configure(bg="#008000")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="URL Shortener v1.0", font="garamond").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Shortened URL", command=urlshortener).pack(pady=8)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command = copyurl).pack(pady=7)

root.mainloop()



