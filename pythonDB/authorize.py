from tkinter import *
import accessData
from tkinter import messagebox



def validate(e_idT, passT, window):
    e_id = e_idT.get("1.0", 'end-1c')
    password = passT.get()
    data = accessData.getData("password", "emp_id = " + str(e_id))
    if data == False:
        messagebox.showerror("ERROR", "Invalid ID! Try again!")
    else:
        if list(data[0])[0] == password:
            window.destroy()
        else:
            print(password)
            print(list(data[0])[0])
            messagebox.showerror("ERROR", "Invalid Password! Try again!")


def login():
    auth = Tk()
    auth.title("Log In")
    auth.geometry("450x200")
    auth.resizable(0, 0)
    auth.iconbitmap("D:\D-Drive Downloads\icon1final.ico")
    
    title = Label(text = "Enter Credentials", font = ("Bahnschrift", 18, 'italic'))
    title.place(x = 120, y = 0)

    e_idL = Label(text = "Employee ID", font = ("Bahnschrift", 14))
    passL = Label(text =  "Password ", font = ("Bahnschrift", 14))
    e_idL.place(x = 30, y = 60)
    passL.place(x = 30, y = 85)

    e_idT = Text(auth, bg = "#ffe0bf")
    passT = Entry(auth, show = "*", bg = "#ffe0bf")

    submit = Button(auth, text = "Submit", bg = "orange", command = lambda: validate(e_idT, passT, auth), font = "Bahnschrift").place(x = 120, y = 140, width = 200)

    e_idT.place(x = 150, y = 60, width = 230, height = 25)
    passT.place(x = 150, y = 87, width = 230, height = 25)
    auth.mainloop()

    return False

  