import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Medical Instrument Detection")



# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('med.webp')
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
frame = tk.LabelFrame(root, width=550, height=300, bd=5, font=('times', 14, ' bold '),fg="orange",bg="#590054")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=850, y=250) 

label=tk.Label(root,text="Medical Instrument Detection",font=("Algerian",45),
               bg="black",fg="orange",
               width=44,
               height=1)
label.place(x=0,y=0)    
  
def log():
    from subprocess import call
    call(["python","log.py"])
    root.destroy()

def reg():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()
    
    
def window():
    root.destroy()
    
    
    # For Buttons on frame
    
    
button1 = tk.Button(root, text="👤  Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="#3CB371", fg="white")
button1.place(x=900, y=350)
def on_enter(e):
  button1['background'] = '#FF7D40'

def on_leave(e):
  button1['background'] = '#3CB371'

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

button2 = tk.Button(root, text="📝  Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="#3CB371", fg="white")
button2.place(x=1160,y=350)
def on_enter(e):
  button2['background'] = '#FF7D40'

def on_leave(e):
  button2['background'] = '#3CB371'

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)

button3 = tk.Button(root, text="⬅  Exit",command=window,width=14, height=1,font=('times',15, ' bold '), bg="#8470FF", fg="white")
button3.place(x=1050, y=450)
def on_enter(e):
  button3['background'] = '#EEC900'

def on_leave(e):
  button3['background'] = '#8470FF'

button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)

   



root.mainloop()