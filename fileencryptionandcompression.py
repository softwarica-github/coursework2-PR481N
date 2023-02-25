'''This is the program for encryption and decryption of file using python using GUI'''
# Author : Prabin Subedi
# Date : 2023/02/04

# imports 
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet

# permanent key for encryption and decryption 
key='lnTv6Mo7j4i5zhFLpqvD1KjTfVIo49F-7TPZuJWitCg='
keyfernet = Fernet(key)

# for encryption 
def encryptt():
    root1 = Tk()
    root1.withdraw()

    filepath =filedialog.askopenfilename()

    print(filepath)
    with open(filepath,'rb') as f:
        contents =f.read()
    encrypted =keyfernet.encrypt(contents)
    
    with open(f'{filepath}.encrypt','wb') as f:
        f.write(encrypted)
    
    result.config(text=f"Encryption Successfull. Please check filepath \n{filepath}.encrypt")

# for decryption 
def decryptt():
    root1 = Tk()
    root1.withdraw()

    filepath =filedialog.askopenfilename()

    
    with open(filepath,'rb') as f:
        contents =f.read()
    decrypted =keyfernet.decrypt(contents)
    
    filepath=filepath.split('.encrypt')
    

    with open(filepath[0],'wb') as f:
        f.write(decrypted)
    
    result.config(text=f"Decryption Successfull. Please check filepath \n{filepath[0]}")
    
# gui for encryption and decryption 
root = Tk()
root.geometry("900x450+150+100") # screen size
root.title("File Encryptor/Decryptor")

title = Label(root, text="Do you want to encrypt or decrypt the file: ", font=("Calibri",20), fg = "red")
title.pack(pady=20)


# frame under root 
frame = Frame(root)
frame.pack(pady=20)


# for encrypt 
encrypt= Button(frame, text= "Encrypt", width= 15, font = 20, bg = "yellow", fg = "red",command=encryptt)
encrypt.pack(pady=10)

# for decrypt 
decrypt= Button(frame, text= "Decrypt", width= 15, font = 20, bg = "yellow", fg = "red", command=decryptt)
decrypt.pack(pady=20)
# result label
result = Label(frame, font=('Calibri', 15))
result.pack(pady=20)

# program exit 
Exit = Button(frame, text = "Exit", font= ('Calibri', 15), padx =10, fg='white', bg = 'brown', command = root.destroy)
Exit.pack()

root.mainloop()
