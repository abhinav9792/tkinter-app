
from tkinter import *
from  tkinter import ttk


tkWindow  = Tk()
tkWindow.geometry('670x500')  
tkWindow.title('Trade-app-View-Details')
tkWindow.resizable(False,False)

canvas = Canvas(tkWindow, width=670, height=500)
canvas.create_rectangle(0, 50, 700, 0, fill='orange')
canvas.pack()


def account():
	tkWindow.destroy()
	import login
def io():
	tkWindow.destroy()
	import transaction
def invest():
	tkWindow.destroy()
	import invest
def view():
	tkWindow.destroy()
	import tables

tab1= Button(tkWindow, text="Open an Account", command=account,width=20,bg='brown',fg='white').place(x=10,y=10)
tab1= Button(tkWindow, text="Money In/Out", command=io,width=20,bg='brown',fg='white').place(x=170,y=10)
tab1= Button(tkWindow, text="Invest Now", command=invest,width=20,bg='brown',fg='white').place(x=340,y=10)
tab1= Button(tkWindow, text="View", command=view,width=20,bg='brown',fg='white').place(x=510,y=10)

labl_0 = Label(tkWindow, text="Account Statements",width=20,font=("bold", 20),bg="orange")  
labl_0.place(x=180,y=60) 


table_frame = Frame(tkWindow)
table_frame.place(x=140,y=150)

table_data = ttk.Treeview(table_frame)

table_data['columns'] = ("Name of the cryptocurrencies" ,
                         "Date of purchasing" ,"Buy/sell option","Quantity" ,"Cost" )

table_data.column("#0", width=0,  stretch=NO)
table_data.column("Name of the cryptocurrencies",anchor=CENTER, width=80)
table_data.column("Date of purchasing",anchor=CENTER,width=80)
table_data.column("Buy/sell option",anchor=CENTER,width=80)
table_data.column("Quantity",anchor=CENTER,width=80)
table_data.column("Cost",anchor=CENTER,width=80)

table_data.heading("#0",text="",anchor=CENTER)
table_data.heading ("Name of the cryptocurrencies",text="Id",anchor=CENTER  )
table_data.heading("Date of purchasing",text="Name",anchor=CENTER)
table_data.heading("Buy/sell option",text="Rank",anchor=CENTER)
table_data.heading("Quantity",text="States",anchor=CENTER)
table_data.heading("Cost",text="States",anchor=CENTER)

#insert code here
table_data.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'))
table_data.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
table_data.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
table_data.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
table_data.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
table_data.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

table_data.pack()

canvas.create_rectangle(0, 450, 670, 500, fill='orange')
canvas.pack()

tkWindow.mainloop()