from tkinter import *
from insertFrame import createFrame
import accessData
import authorize
from time import strftime
from datetime import date,datetime
'''
Created By Amogh Pradeep on 18-03-2021
amoghpradeep242@gmail.com
'''
class bill:
    billFrame = None
    custId = -1
    def __init__(self, frame):
        self.frame = frame
        self.total = 0
        self.order = "ID  |\t\tNAME        \t|QTY| PRICE \n"
        self.ord_id = accessData.getData("cust_orders", column = "count(*)")[0][0] + 2200

    def storeBill(self):
        today = date.today().strftime("%d_%m_%Y") + "_" + ((datetime.now().strftime("%X")).replace(":", "_"))
        f = open(today + ".txt", "x")
        f.write(self.order[: 6] + "   " + self.order[6:] + "\n TOTAL = " + str(self.total))
        self.total = 0
        self.order = "ID  |\t\tNAME        \t|QTY| PRICE \n"
        self.billFrame.destroy()
        self.createBillFrame()
        messagebox.showinfo("Success", "Successfully stored Bill")


    def getEntry(self, pidt , qtyt):
        pid = pidt.get()
        qty = qtyt.get()
        pidt.delete(0, END)
        qtyt.delete(0, END)
        self.ord_id += 1
        try:
            data = accessData.getData("product", "p_id = " + pid)[0]
        except:
            messagebox.showerror("Error", "Product " + pid + " Doesnt Exist!")
            heading.destroy()
            self.createBillFrame()
            return False
        
        
        val = (self.ord_id, date.today().strftime("%Y-%m-%d"), int(qty), int(pid), int(self.custId))
        print(val)
        try:
            print(accessData.insertData("cust_orders",val))
        except:
            messagebox.showerror("Error", "Product" + pid + " Out of Stock!")
            heading.destroy()
            self.createBillFrame()
            return False

        self.total += data[5]*int(qty)
        self.order += pid + ((4 - len(str(data[0])))* ' ') + '|' + data[1][:24] + (max(0, 24 - len(data[1])) * ' ') + "|" + qty + ((3 - len(qty))*' ') + '|' + str(data[5]) + "\n"
        itemDisplay = Text(self.billFrame, height = 17.2, width = 41)
        itemDisplay.place(x = 10, y = 10)
        itemDisplay.bind("<Key>", lambda a: "break")
        itemDisplay.insert('1.0', self.order)

        totalL = Label(self.billFrame, text = " Total :",  font = ("Montserrat", 13, 'italic'))
        priceL = Label(self.billFrame, text = "₹" + str(int(self.total)) + "  ",  font = ("Montserrat", 28, 'italic', 'bold'), fg = "orange")
        totalL.place(x = 700, y = 280)
        priceL.place(x = 760, y =260)

    def createBill(self, getCust_id, b, l):
        self.custId = getCust_id.get()
        getCust_id.destroy()
        cust_name = accessData.getData("customer", "cust_id =" + self.custId)

        print(cust_name)
        b.destroy()
        l.destroy()
        
        heading = Label(self.billFrame, text = "Create Bill For  ", font = ("Montserrat", 15, 'italic'))
        heading.place(x = 390, y = 8)
        try:
            name = Label(self.billFrame, text = cust_name[0][1], font = ("Montserrat", 20,  'italic', 'bold'), fg = 'orange').place(x = 550, y = 2)
        except:
            messagebox.showerror("Error", "Customer Doesnt Exist!")
            heading.destroy()
            self.createBillFrame()
            return False

        pid_text = Label(self.billFrame, text = "Product ID", font = ("Montserrat", 20,  'bold')).place(x = 390, y = 90)
        qty_text = Label(self.billFrame, text = "Quantity", font = ("Montserrat", 20,'bold')).place(x = 390, y = 140)

        pid_entry = Entry(self.billFrame, bg = "#ffe0bf", font = ("Montserrat", 20, 'italic'))
        qty_entry = Entry(self.billFrame, bg = "#ffe0bf", font = ("Montserrat", 20, 'italic'))
        

        next = Button(self.billFrame, text = "next", bg = "orange", command =lambda: self.getEntry(pid_entry, qty_entry), font = ("Montserrat", 10))
        create = Button(self.billFrame, text = "create bill", bg = "orange", command = lambda: self.storeBill(), font = ("Montserrat", 10))
        next.place(x = 800, y = 190, width = 100)
        create.place(x = 800, y = 230, width = 100)

        pid_entry.place(x = 650, y = 90, width = 250)
        qty_entry.place(x = 650, y = 140, width = 250)
        generateBill = Button()
        
    def createBillFrame(self):
        # Billing System Frame
        billDesk = LabelFrame(self.frame, text = "Billing", font = ("Montserrat", 16, 'bold'))
        billDesk.place(x = 20, y = 340, height = 350, width = 1030)
        self.billFrame = billDesk

        getCust_id = Entry(billDesk, bg = "#ffe0bf", font = ("Montserrat", 20, 'bold'))
        heading = Label(billDesk, text = "Enter Customer ID ", font = ("Montserrat", 20, 'bold'))
        heading.place(x = 150, y = 100)

        submit = Button(billDesk, text = "Start", bg = "orange", command =lambda: self.createBill(getCust_id, submit, heading), font = ("Montserrat", 14, 'italic'))
        submit.place(x = 575, y = 150, width = 150)
        getCust_id.place(x = 475, y = 100, height = 40, width = 250)
