from tkinter import *
from insertFrame import createFrame
import accessData
import authorize
import billing
from time import strftime
from datetime import date
 
#Authorize
flag = False
while not flag:
    flag = authorize.login() 
    if flag == 2:
        exit()

'''
    Amogh Pradeep 
    19-03-2021
    amoghpradeep242@gmail.com
'''
#MAIN WINDOW 
win = Tk()
win.title("Amogh Roshan Database")
win.geometry("1440x768")
win.resizable(0, 0)
win.iconbitmap("D:\D-Drive Downloads\icon1final.ico")

result = []
def getVal(entries):
    for i in entries:
        result.append(i.get("1.0", "end-1c"))
    for i in entries:
        i.delete('1.0', END)
    
    for r in result:
        print(r)

def cust_orders(display):
    field_list = ["ord_id", "ord_date", "qty", "p_id", "cust_id"]
    frame = createFrame("cust_orders", field_list, display)
    frame.createInsert()
    frame.createDelete("ord_id")
    frame.createDisplay()

def store_orders(display):
    field_list = ["ord_id",  "p_id", "qty", "ord_date"]
    frame = createFrame("store_orders", field_list, display)
    frame.createInsert()
    frame.createDelete("ord_id")
    frame.createDisplay()

def product(display):
    field_list = ["p_id", "p_name", "p_vendor", "stock", "buyPrice", "mrp"]
    frame = createFrame("product", field_list, display)
    frame.createInsert()
    frame.createDelete("p_id")
    frame.createDisplay()

def employee(display):
    field_list = ["emp_id", "full_name", "email", "designation", "salary","branch_id", "joining_date"]
    frame = createFrame("employee", field_list, display)
    frame.createInsert()
    frame.createDelete("emp_id")
    frame.createDisplay()

def customer(display):
    field_list = ["cust_id", "name", "address", "postal_code", "tel_no","branch"]
    frame = createFrame("customer", field_list, display)
    frame.createInsert()
    frame.createDelete("cust_id")
    frame.createDisplay()

total = 0
order = ""
# Home Screen Design
# Created by Amogh Pradeep 
def home(display):
    # Table Information Frame Design
    data = accessData.getTableInfo()

    info = LabelFrame(display, text = "Information", font = ("Montserrat", 16))
    info.place(x = 20, y = 0, height = 320, width = 500)

    title = Label(info, text = "Tables :", font = ("Montserrat", 18, 'underline', 'italic', 'bold')).place(x = 20, y = 10)
    init_y = 60
    for entry in data:
        entry = list(entry)
        if entry[0] == "password": continue
        line = Label(info, text = entry[0], font = ("Montserrat", 16))
        line.place(x = 20, y = init_y)
        init_y += 30

    size = Label(info, text = "Size :", font = ("Montserrat", 18, 'underline', 'italic', 'bold'))
    size.place(x = 300, y = 10)
    init_y = 60
    for entry in data:
        entry = list(entry)
        if entry[0] == "password": continue
        line = Label(info, text = entry[1], font = ("Montserrat", 16))
        line.place(x = 300, y = init_y)
        init_y += 30

    # Time Frame Design
    def timeupdate():
        tstring = strftime('%H:%M:%S %p')
        timecounter.config(text = tstring)
        timecounter.after(1000, timeupdate)

    time = LabelFrame(display, text = "Time", font = ("Montserrat", 16))
    time.place(x = 550, y = 0, height = 320, width = 500)
    
    d = date.today().strftime("%B %d, %Y")
    dateL = Label(time, text = d, font = ("Montserrat", 20, "bold"))
    dateL.place(x = 50, y = 65)
    timecounter = Label(time, font = ("Montserrat", 32, "bold"))
    timecounter.place(x = 50, y = 115)
    timeupdate()

    billFrame = billing.bill(display)
    billFrame.createBillFrame()

main_title = Label(win,text = "STORE MANAGER",font = ("Montserrat", 20, "bold", "italic"), bg = "orange")
main_title.place(x = 0, y = 0, relwidth = 1)

# SIDE BUTTONS TO SELECT DATABASE
home_b = Button(win, text="Home", font = ('Montserrat', 11),relief=RIDGE , command = lambda: home(display))
cust_b = Button(win, text="Customer",font = ('Montserrat', 11),relief=RIDGE , command = lambda: customer(display))
emp_b = Button(win, text="Employee",font = ('Montserrat', 11), relief=RIDGE ,command = lambda: employee(display))
cust_ord_b = Button(win, text="Customer Orders",font = ('Montserrat', 11), relief=RIDGE ,command = lambda: cust_orders(display))
store_ord_b = Button(win, text="Store Orders", font = ('Montserrat', 11),relief=RIDGE ,command = lambda: store_orders(display))
prod_b = Button(win, text="Product Stock",font = ('Montserrat', 11), relief=RIDGE ,command = lambda: product(display))


#FRAME

display = LabelFrame(win)
display.place(x = 10, y = 45, height = 717, width = 1074.8)

# PLACEMENT
home_b.place(x= 1092.8, y = 44, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_b.place(x= 1092.8, y = 100.6, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

emp_b.place(x= 1092.8, y = 158.2, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_ord_b.place(x= 1092.8, y = 215, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

store_ord_b.place(x= 1092.8, y = 272, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

prod_b.place(x= 1092.8, y = 329, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

home(display)
win.mainloop()
