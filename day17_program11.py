#Entry Widgets:

from tkinter import *
master=Tk()
l1=Label(master,text="First Name")
l1.grid(row=0,column=0)
l2=Label(master,text="Last Name")
l2.grid(row=1,column=0)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def show_entry_fields():
    print("First Name:%s \n Last Name: %s" %(e1.get(),e2.get()))
##    print("First Name:",e1.get())
##    print("Last Name",e2.get())
b1=Button(master,text='Quit', command=master.quit)
b1.grid(row=3,column=0)

b2=Button(master,text='Show', command=show_entry_fields)
b2.grid(row=3,column=1)#sticky=W, pady=4
mainloop()

'''
OUTPUT:
First Name: shaik
Last Name sufiya
First Name: shaik
Last Name sufiya
'''


