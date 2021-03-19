from tkinter import *
import accessData
from tkinter import messagebox

'''
Created By Amogh Pradeep on 18-03-2021
amoghpradeep242@gmail.com
'''
close = False
authorized = False
def validate(e_idT, passT, window):
    e_id = e_idT.get()
    password = passT.get()
    data = accessData.getData("password", "emp_id = " + str(e_id))
    if len(data) == 0:
        messagebox.showerror("ERROR", "Invalid ID! Try again!")
    else:
        if list(data[0])[0] == password:
            destroy(window, True)
        else:
            messagebox.showerror("ERROR", "Invalid Password! Try again!")
            

def destroy(window, flag = False):
    global authorized
    window.destroy()
    authorized = flag

def closeWin(window):
    global close
    window.destroy()
    close = True

def login():
    global close
    auth = Tk()
    auth.title("Log In")        
    auth.protocol("WM_DELETE_WINDOW",lambda: closeWin(auth))
    auth.geometry("450x200")
    auth.resizable(0, 0)
    auth.iconbitmap("D:\D-Drive Downloads\icon1final.ico")
    
    title = Label(text = "Enter Credentials", font = ("Montserrat", 18, 'italic'))
    title.place(x = 120, y = 0)

    e_idL = Label(text = "Employee ID", font = ("Montserrat", 14))
    passL = Label(text =  "Password ", font = ("Montserrat", 14))
    e_idL.place(x = 10, y = 60)
    passL.place(x = 10, y = 85)

    e_idT = Entry(auth, bg = "#ffe0bf")
    passT = Entry(auth, show = "*", bg = "#ffe0bf")

    submit = Button(auth, text = "Submit", bg = "orange", command = lambda: validate(e_idT, passT, auth), font = "Montserrat").place(x = 120, y = 140, width = 200)
    e_idT.place(x = 150, y = 60, width = 230, height = 25)
    passT.place(x = 150, y = 87, width = 230, height = 25)
    auth.mainloop()
    if close:
        return 2
    return authorized