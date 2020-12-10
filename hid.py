import tkinter as tk
import requests
import subprocess
import os
import hashlib 

def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid
# print(GetUUID())


  

md5 = hashlib.md5()
md5.update((GetUUID()).encode('utf-8'))



root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def gen ():  
    label1 = tk.Label(root, text= md5.hexdigest(), fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Get HWID',command=gen, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()