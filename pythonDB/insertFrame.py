from tkinter import *
import accessData
from tkinter import messagebox

'''
Created by Amogh Pradeep on 17-03-2021
amoghpradeep242@gmail.com
'''

class createFrame:
    def __init__(self, table, field_list, frame):
        self.table = table
        self.field_list = field_list
        self.frame = frame
        self.result  = []
    
    def insertDB(self, entries):
        #populating result lists with fresh entries.
        for e in entries:
            self.result.append(e.get("1.0", 'end-1c'))
        #clearing textboxes
        
        if accessData.insertData(self.table, tuple(self.result)):
            messagebox.showinfo("SUCCESS!", "Entry Successful!")
            for e in entries:
                e.delete('1.0', END)
        else:
            messagebox.showerror("ERROR", "Invalid Input! Try again!")
        
    def delDB(self, box, primary_key):
        val = box.get("1.0", 'end-1c')

        if accessData.delData(self.table, primary_key, val):
            messagebox.showinfo("SUCCESS!", "Removed Value!")
            box.delete('1.0', END)
        else:
            messagebox.showerror("ERROR", "Invalid Input! Try again!")

    def createInsert(self):
        insert = LabelFrame(self.frame, text = "Insert", font = ("Bahnschrift", 16, 'italic'))

        insert.place(x = 20, y = 0, height = 320, width = 500)

        #initial height of labels.
        init_y = 30

        #storing all labels in a list.
        labels = []
        #populating labels list.
        for field in self.field_list:
            new_label = Label(insert, text = field + " : ",font = ("Bahnschrift", 12))
            labels.append(new_label)

        #placing labels.
        for label in labels:
            label.place(x = 30, y = init_y)
            init_y += 25
        
        #storing all text fields in a list.
        textBoxes = []
        #populating texts list.
        for i in range (len(self.field_list)):
            new_text = Text(insert, bg = "#ffe0bf")
            textBoxes.append(new_text)
        
        sumbit = Button(insert, text = "Submit", bg = "orange", command = lambda: self.insertDB(textBoxes), font = "Bahnschrift").place(x = 250, y = init_y + 25, width = 200)
        init_y = 30
        for box in textBoxes:
            box.place(x = 150, y = init_y, width = 300, height = 20)
            init_y += 25

    def createDelete(self, primary_key):
        delete = LabelFrame(self.frame, text = "Delete", font = ("Bahnschrift", 16, 'italic'))
        delete.place(x = 550, y = 0, height = 320, width = 500)

        pk_label = Label(delete, text = primary_key + " : ", font =("Bahnschrift", 12))
        pk_label.place(x = 30, y = 30)

        textBox = Text(delete, bg = "#ffe0bf") 
        sumbit = Button(delete, text = "Submit", bg = "orange", command = lambda: self.delDB(textBox, primary_key), font = "Bahnschrift").place(x = 250, y = 75, width = 200)

        textBox.place(x = 150, y = 30, width = 300, height = 20)

    def createDisplay(self):
        display = LabelFrame(self.frame, text = "Table Data", font = ("Bahnschrift", 16, 'italic'))
        display.place(x = 20, y = 340, height = 320, width = 1030)




