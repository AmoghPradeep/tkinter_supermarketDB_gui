import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import accessData
'''
Created by Roshan Somayajula on 18-03-2021
'''
# MAIN present_dataDOW
def view_helper(present_data,table, table_attrib, cond, col):
    condition = cond.get()
    column = col.get()
    top = Toplevel(present_data) #new present_datadow connected to main present_datadow
    top.title("Data in the table")
    top.geometry("1450x600")
    top.resizable(0, 0)
    data = accessData.getData(table, condition,column)
    rows = len(data)
    cols = len(data[0])
    l1 = []
    for i in range(cols):
        l1.append(str(i+1))
    my_tree = ttk.Treeview(top, height=600)
    my_tree["columns"] = l1
    my_tree["show"] = "headings"
    for i in l1:
        my_tree.column(i, anchor=CENTER)
    print(cols)
    

    for i in range(1, cols+1):
        if cols == 1:
            colName = column
        else:
            colName = table_attrib[i-1]
        my_tree.heading(str(i), text=colName)
    index = iid = 0
    for x in data:
        my_tree.insert("", index, iid, values=x)
        index += 1
        iid = index+1
    verscrlbar = Scrollbar(top, orient="vertical", command=my_tree.yview)
    my_tree.pack()
    verscrlbar.place(x=1430, y=0, height=600)
    my_tree.configure(xscrollcommand=verscrlbar.set)


def viewTable(present_data, table, table_attrib, column):
    condition = tkinter.Entry(present_data, bg = "#ffe0bf", font = ("Montserrat", 16))
    show_data = tkinter.Button(present_data, command=lambda:view_helper(present_data, table,
            table_attrib, condition, column), text="View Data in the table", bg="orange", font=("Montserrat", 14))
    show_data.place(x=500, y=200, height=60, width=400)
    condition.place(x = 700, y = 84, width = 200)

    present_data.mainloop()