from tkinter import *

class Application(Frame):

 def __init__(self, master):
     super(Application, self).__init__(master)
     self.grid()
     self.create_widgets()

     self.electrical = []
     self.mechanical = []
     self.fabrication = []
     self.assembly = []
     self.software = []
     self.exit = Button(self,text="   Exit   ",font = ("Arial",20),command=master.destroy)
     self.exit.grid(column=0,row=10)

     
 def create_widgets(self):
     self.title = Label(self, text = "\nFRC Robotics Item Inventory", font = ("Arial",30))
     self.title.grid(row=0,column=0)
     self.viewitems = Button(self,text = "View Items", font = ("Arial",20),command = self.viewItems)
     self.viewitems.grid(column=0, row=1)

 def viewItems(self):
     Label(self,
             text = "Add item below:"
             ).grid(row = 1, column = 0, sticky = W)
     self.item = Entry(self)
     self.item.grid(column=0,row=2,sticky=W)
     
     self.var = StringVar(self)
     self.teams = OptionMenu(self,self.var,"Software","Electrical","Mechanical","Fabrication","Assembly","Media")
     self.teams.grid(column=1,row=2)

     self.var2 = StringVar(self)
     self.num = OptionMenu(self,self.var2,"1","2","3","4","5","6","7","8","9","10")
     self.num.grid(column=2,row=2)

     Label(self,
           text = "              "
           ).grid(row = 6,column = 0)
     self.add = Button(self,text=" ADD ",command=self.addItems)
     self.add.grid(column=1,row=7)

     self.remove = Button(self,text=" REMOVE ",command=self.removeItems)
     self.remove.grid(column=2,row=7)

  
     self.textBox = Text(self,height=10,width=65)
     self.textBox.grid(column=0,row=7,sticky=W)

 def addItems(self):
     self.textBox.insert(END,self.var2.get() + " " + self.item.get() + "(s) have been added to the " + self.var.get() + " inventory.\n")
     if (self.var.get() == "Mechanical"):
         self.mechanical.append([self.item.get(),self.var2.get()])
         for i in self.mechanical:
             self.textBox.insert(END,"Mechanical Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     elif (self.var.get() == "Software"):
         self.software.append([self.item.get(),self.var2.get()])
         for i in self.software:
             self.textBox.insert(END,"Software Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     elif (self.var.get() == "Assembly"):
         self.assembly.append([self.item.get(),self.var2.get()])
         for i in self.assembly:
             self.textBox.insert(END,"Assembly Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     elif (self.var.get() == "Fabrication"):
         self.fabrication.append([self.item.get(),self.var2.get()])
         for i in self.fabrication:
             self.textBox.insert(END,"Fabrication Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     elif (self.var.get() == "Electrical"):
         self.electrical.append([self.item.get(),self.var2.get()])
         for i in self.electrical:
             self.textBox.insert(END,"Electrical Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     else:
         self.media.append([self.item.get(),self.var2.get()])
         for i in self.media:
             self.textBox.insert(END,"Media Inventory:\n")
             self.textBox.insert(END,"Item:\t\tQuantity:\n")
             self.textBox.insert(END,i[0]+"\t\t"+str(i[1]))
     

 def removeItems(self):
     self.textBox.insert(END,self.var2.get() + " " + self.item.get() + "(s) have been removed to the " + self.var.get() + " inventory.\n")
     if (self.var.get() == "Mechanical"):
         self.mechanical.append([self.item.get(),self.var2.get()])
     elif (self.var.get() == "Software"):
         self.software.append([self.item.get(),self.var2.get()])
     elif (self.var.get() == "Assembly"):
         self.assembly.append([self.item.get(),self.var2.get()])
     elif (self.var.get() == "Fabrication"):
         self.fabrication.append([self.item.get(),self.var2.get()])
     elif (self.var.get() == "Electrical"):
         self.electrical.append([self.item.get(),self.var2.get()])
     else:
         self.media.append([self.item.get(),self.var2.get()])
     
     
def main():
 root = Tk()
 root.title("Robotics Inventory")
 root.geometry("700x600")

 app = Application(root)
 app.grid()

 root.mainloop()

main()
