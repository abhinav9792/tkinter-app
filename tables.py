
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
table_data.heading("Date of purchasing",text="Name of the cryptocurrencies",anchor=CENTER)
table_data.heading("Buy/sell option",text="Date of purchasing",anchor=CENTER)
table_data.heading("Quantity",text="Buy/sell option",anchor=CENTER)
table_data.heading("Cost",text="Cos",anchor=CENTER)

#insert code here
table_data.insert(parent='',index='end',iid=0,text='',
values=( '1','Ethyrem','23/03/23','Buy', '1500'))
table_data.insert(parent='',index='end',iid=1,text='',
values=('2','Bitcoin','23/03/23','Sell', '120'))
table_data.insert(parent='',index='end',iid=2,text='',
values=('3','Dogecoin','23/03/23', 'Buy', '1234'))
table_data.insert(parent='',index='end',iid=3,text='',
values=('4','Ethyrem','24/03/23','Sell', '1800'))
table_data.insert(parent='',index='end',iid=4,text='',
values=('5','Rock','24/03/23','Buy', '1700'))
table_data.insert(parent='',index='end',iid=5,text='',
values=('6','Gold','24/03/23','Buy', '15000'))

table_data.pack()

canvas.create_rectangle(0, 450, 670, 500, fill='orange')
canvas.pack()

tkWindow.mainloop()