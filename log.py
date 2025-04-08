import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
#import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="#607B8B")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Medical Instrument Detection")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('m1.jpg')
image2 = image2.resize((950,800), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=600, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="Medical Instrument Detection",font=("Times New Roman", 30, 'bold'),
                    background="#B0E0E6", fg="black", width=70, height=1)
label_l1.place(x=0, y=0)



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def home():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "Great to see you again! You're logged in")
            # ===========================================
            # root.destroy()

            from subprocess import call
            call(['python','testing_image.py'])
            
            root.destroy()
            
         # ================================================
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')







        
title=tk.Label(root, text="__Login Here__", font=("Times new roman", 30, "bold","italic"),bd=5,bg="#3CB371",fg="black")
title.place(x=200,y=200,width=250)
        
Login_frame=tk.Frame(root,bg="gray")
Login_frame.place(x=80,y=300)
        
logolbl=tk.Label(Login_frame,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=home,width=15,font=("Times new roman", 14, "bold"),bg="#B0E0E6",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#B0E0E6",fg="black")
btn_reg.grid(row=3,column=0,pady=10)
        
        
    
       
        # Login Function



# def about():
#     from subprocess import call
#     call(["python","aboutus.py"])
#     root.destroy()

def con():
    from subprocess import call
    call(["python","GUI_main.py"])
    root.destroy()

def window():
  root.destroy()
    
    
button1 = tk.Button(root, text="HOME", command=con, width=12, height=1,font=('times 15 bold underline'),bd=0, bg="#4169E1", fg="white")
button1.place(x=20, y=100)

button2 = tk.Button(root, text="REGISTER",command=registration,width=12, height=1,font=('times 15 bold underline'), bd=0,bg="#4169E1", fg="white")
button2.place(x=200, y=100)

button4 = tk.Button(root, text="EXIT", command=window, width=12, height=1,font=('times 15 bold underline'),bd=0,bg="#FF8000", fg="white")
button4.place(x=400, y=100)





root.mainloop()