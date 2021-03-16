from tkinter import *
#MAIN WINDOW 
win = Tk()
win.title("Amogh Roshan Database")
win.geometry("1440x768")
win.resizable(0, 0)
win.iconbitmap("D:\D-Drive Downloads\icon1final.ico")



main_title = Label(win,text = "STORE MANAGER",font = ("Bahnschrift", 20), bg = "orange")
main_title.place(x = 0, y = 0, relwidth = 1)

# SIDE BUTTONS TO SELECT DATABASE
home_b = Button(win, text="Home")
cust_b = Button(win, text="Customer")
emp_b = Button(win, text="Employee")
cust_ord_b = Button(win, text="Customer Orders")
store_ord_b = Button(win, text="Store Orders")
prod_b = Button(win, text="Product Stock")
# PLACEMENT
home_b.place(x= 1092.8, y = 39, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_b.place(x= 1092.8, y = 96.6, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

emp_b.place(x= 1092.8, y = 154.2, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_ord_b.place(x= 1092.8, y = 211.8, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

store_ord_b.place(x= 1092.8, y = 269.4, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

prod_b.place(x= 1092.8, y = 327, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

#FRAME

display = LabelFrame(win, text = "Display")
display.place(x = 10, y = 45, height = 717, width = 1074.8)




win.mainloop()
