from tkinter import *
from tkinter.ttk import *
import getdata

# MAIN WINDOW
win = Tk()
win.title("Amogh Roshan Database")
win.geometry("1440x768")
win.resizable(0, 0)
win.iconbitmap(r"C:\Users\rk009\Downloads\icon1.ico")

main_title = Label(win, text="STORE MANAGER", font=("Bahnschrift", 20))
main_title.place(x=0, y=0, relwidth=1)

display = LabelFrame(win, text="Display")
display.place(x=10, y=45, height=500, width=1074.8)


def newWindow():
    top = Toplevel(win) #new window connected to main window
    top.title("Data in the table")
    top.geometry("1050x600")
    top.resizable(0, 0)
    data = getdata.getData(table="Cust_orders")
    rows = len(data)
    cols= len(data[0])
    l1 = []
    for i in range(cols):
        l1.append(str(i+1))
    print(l1)
    my_tree = Treeview(top, height=600)
    my_tree["columns"] = l1
    my_tree["show"] = "headings"
    for i in l1:
        my_tree.column(i, anchor=CENTER)
    my_tree.heading("1", text="Order ID")
    my_tree.heading("2", text="Order Date")
    my_tree.heading("3", text="Quantity")
    my_tree.heading("4", text="Product ID")
    my_tree.heading("5", text="Customer ID")
    index = iid = 0
    for x in data:
        my_tree.insert("", index, iid, values=x)
        index += 1
        iid = index+1
    verscrlbar = Scrollbar(top, orient="vertical", command=my_tree.yview)
    my_tree.pack()
    verscrlbar.place(x=1030, y=0, height=600)
    my_tree.configure(xscrollcommand=verscrlbar.set)


show_data = Button(win, command=newWindow, text="View Data in the table")
show_data.place(x=650, y=650, height=60, width=200)

win.mainloop()
