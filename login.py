from tkinter import *
from functools import partial

def validateLogin(username, password,cash_Entry):
	print("username entered :", username.get())
	print("password entered :", password.get())
	print("total cash is:",cash_Entry.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('670x500')  
tkWindow.title('Trade-app-login-form')
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

labl_0 = Label(tkWindow, text="Open an Account",width=20,font=("bold", 20),bg="orange")  
labl_0.place(x=180,y=60) 

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",font=("bold", 10))
usernameLabel.place(x=180,y=130)  
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(x=300,y=130)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",font=("bold", 10))
passwordLabel.place(x=180,y=180) 
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.place(x=300,y=180) 

cash = Label(tkWindow, text="Cash To Invest:",font=("bold", 10))  
cash.place(x=180,y=230)
cash_amount = IntVar()
cash_Entry = Entry(tkWindow, textvariable=cash_amount)
cash_Entry.place(x=300,y=230) 

validateLogin = partial(validateLogin, username, password,cash_Entry)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin,width=20,bg='brown',fg='white').place(x=230,y=280)   
# tkWindow['background']='#2D2727'


canvas.create_rectangle(0, 450, 670, 500, fill='orange')
canvas.pack()

tkWindow.mainloop()