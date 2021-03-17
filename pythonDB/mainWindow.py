from tkinter import *
from insertFrame import createFrame
import accessData
import authorize
from time import strftime
from datetime import date

while authorize.login():
    time.sleep(2)


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


def employee(display):
	field_list = ["emp_id", "full_name", "email", "designation", "salary", "branch_id", "joining_date"]
	frame = createFrame("employee", field_list, display)
	frame.createInsert()
	frame.createDelete("emp_id")

def customer(display):
	field_list = ["cust_id", "name", "adderss", "postal_code", "tel_no", "branch"]
	frame = createFrame("customer", field_list, display)
	frame.createInsert()
	frame.createDelete("cust_id")

def cust_orders(display):
    field_list = ["ord_id", "ord_date", "qty", "p_id", "cust_id"]
    frame = createFrame("cust_orders", field_list, display)
    frame.createInsert()
    frame.createDelete("ord_id")

def store_orders(display):
    field_list = ["ord_id", "ord_date", "qty", "p_id"]
    frame = createFrame("store_orders", field_list, display)
    frame.createInsert()
    frame.createDelete("ord_id")
    frame.createDisplay()

def product(display):
    field_list = ["p_id", "p_name", "p_vendor", "stock", "buyPrice", "mrp"]
    frame = createFrame("product", field_list, display)
    frame.createInsert()
    frame.createDelete("p_id")
	
def home(display):
    data = accessData.getTableInfo()

    info = LabelFrame(display, text = "Information", font = ("Bahnschrift", 16))
    info.place(x = 20, y = 0, height = 320, width = 500)

    title = Label(info, text = "Tables :", font = ("Bahnschrift", 18, 'underline', 'italic')).place(x = 20, y = 10)
    init_y = 60
    for entry in data:
        entry = list(entry)
        line = Label(info, text = entry[0], font = ("Bahnschrift", 16))
        line.place(x = 20, y = init_y)
        init_y += 30

    size = Label(info, text = "Size :", font = ("Bahnschrift", 18, 'underline', 'italic'))
    size.place(x = 300, y = 10)
    init_y = 60
    for entry in data:
        entry = list(entry)
        line = Label(info, text = entry[1], font = ("Bahnschrift", 16))
        line.place(x = 300, y = init_y)
        init_y += 30

    def timeupdate():
        tstring = strftime('%H:%M:%S %p')
        timecounter.config(text = tstring)
        timecounter.after(1000, timeupdate)

    time = LabelFrame(display, text = "Time", font = ("Bahnschrift", 16))
    time.place(x = 550, y = 0, height = 320, width = 500)
    
    d = date.today().strftime("%B %d, %Y")
    dateL = Label(time, text = d, font = ("Bahnschrift", 20, "bold"))
    dateL.place(x = 50, y = 65)
    timecounter = Label(time, font = ("Bahnschrift", 32, "bold"))
    timecounter.place(x = 50, y = 115)
    timeupdate()
   



main_title = Label(win,text = "STORE MANAGER",font = ("Bahnschrift", 20, "bold", "italic"), bg = "orange")
main_title.place(x = 0, y = 0, relwidth = 1)

# SIDE BUTTONS TO SELECT DATABASE
home_b = Button(win, text="Home", command = lambda: home(display))
cust_b = Button(win, text="Customer", command = lambda: customer(display))
emp_b = Button(win, text="Employee", command = lambda: employee(display))
cust_ord_b = Button(win, text="Customer Orders", command = lambda: cust_orders(display))
store_ord_b = Button(win, text="Store Orders", command = lambda: store_orders(display))
prod_b = Button(win, text="Product Stock", command = lambda: product(display))

#FRAME

display = LabelFrame(win)
display.place(x = 10, y = 45, height = 717, width = 1074.8)

# PLACEMENT
home_b.place(x= 1092.8, y = 39, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_b.place(x= 1092.8, y = 96.6, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

emp_b.place(x= 1092.8, y = 154.2, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

cust_ord_b.place(x= 1092.8, y = 211.8, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

store_ord_b.place(x= 1092.8, y = 269.4, relwidth = 0.2375, relheight = 0.075, bordermode = OUTSIDE)

prod_b.place(x= 1092.8, y = 327, relwidth =0.2375, relheight = 0.075, bordermode = OUTSIDE)

win.mainloop()