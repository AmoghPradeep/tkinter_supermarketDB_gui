from tkinter import *
from insertFrame import createFrame

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

def product(display):
    field_list = ["p_id", "p_name", "p_vendor", "stock", "buyPrice", "mrp"]
    frame = createFrame("product", field_list, display)
    frame.createInsert()
    frame.createDelete("p_id")
	

main_title = Label(win,text = "STORE MANAGER",font = ("Bahnschrift", 20), bg = "orange")
main_title.place(x = 0, y = 0, relwidth = 1)

# SIDE BUTTONS TO SELECT DATABASE
home_b = Button(win, text="Home", command = lambda: customer(display))
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