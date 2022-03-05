from tkinter import*
from tkinter import messagebox as mbox 
from tkinter import ttk

root=Tk()
root.title("Classes")
root.geometry("600x400")

elements=["Label","Button","Input","Dropdown"]
selectedval=StringVar()
dropdown=ttk.Combobox(root,values=elements,state="readonly",textvariable=selectedval).pack()
label1=""
btn_1=""
input_box=""
example=""
class CreateElement():
    def __init__(self):
        print("Element Created")
        
    def chooseElements(self):
        output=selectedval.get()
        print(output)
        
        if output=="Label":
            self.createlabel()
        elif output=="Button":
            self.createbutton()
        elif output=="Input":
            self.createInput()
        elif output=="Dropdown":
            self.createDropdown()
        
    def createlabel(self):
        global label1
        label1=Label(root,text="The button was creted using classes",fg="red")
        label1.pack()
        
    def createbutton(self):
        global btn_1
        btn_1=Button(root,text="Show Alert Pannel",bg="blue",fg="aqua",command=self.messagepannel)
        btn_1.pack(padx=20,pady=10)
    
    def createInput(self):
        global input_box
        input_box=Entry(root,width=30)
        input_box.pack(padx=20,pady=10)
    
    def createDropdown(self):
        global example
        element=["Label","Button","Input","Dropdown"]
        example=ttk.Combobox(root,values=element,state="readonly").pack()
        example.pack(padx=20,pady=10)
    
    def messagepannel(self):
        value=input_box.get()
        mbox.showinfo("Showinfo",value)
        
    def destroyElements(self):
        global label1
        global btn_1
        global input_box
        global example
        
        label1.destroy()
        btn_1.destroy()
        input_box.destroy()
        example.destroy()
        
        
obj_create_element=CreateElement()
btn_2=Button(root,text="Start Class",bg="red",fg="Gold",command=obj_create_element.chooseElements)
btn_2.pack(padx=20,pady=10)
btn_3=Button(root,text="Close Element",bg="lightblue",fg="blue",command=obj_create_element.destroyElements)
btn_3.pack(padx=20,pady=10)
root.mainloop()