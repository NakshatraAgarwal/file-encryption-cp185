from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title = "Select File", filetypes = (("Text Files", "*.txt"),))
    print(text_file)
    read_file = open(text_file,'r')
    para = read_file.read()
    result = hashlib.md5(para.encode())
    new_result = result.hexdigest()
    md5_file = open('md5.txt','w')
    md5_file.write(new_result)
    print(new_result)
    md5_file.close()

    
    
def apply_sha256():
    print("SHA function")  
    text_file = fd.askopenfilename(title = "Select File", filetypes = (("Text Files", "*.txt"),))
    print(text_file)
    read_file = open(text_file,'r')
    para = read_file.read()
    result = hashlib.sha256(para.encode())
    new_result = result.hexdigest()
    sha256_file = open('sha256.txt','w')
    sha256_file.write(new_result)
    print(new_result)
    sha256_file.close()
    
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()