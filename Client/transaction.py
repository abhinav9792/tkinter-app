from tkinter import * 

#money function
def validateLogin():
    print("Added Money :", amount_entry.get())
    return
# tab function

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

#radio button
def sel():
   selection = "You selected the option " + str(var.get())
   print(selection)
tkWindow = Tk()
tkWindow.geometry("700x500")
tkWindow.resizable(False,False)

canvas = Canvas(tkWindow, width=700, height=800)
canvas.create_rectangle(0, 50, 700, 0, fill='orange')
canvas.pack()



tab1= Button(tkWindow, text="Open an Account", command=account,width=20,bg='brown',fg='white').place(x=10,y=10)
tab1= Button(tkWindow, text="Money In/Out", command=io,width=20,bg='brown',fg='white').place(x=170,y=10)
tab1= Button(tkWindow, text="Invest Now", command=invest,width=20,bg='brown',fg='white').place(x=340,y=10)
tab1= Button(tkWindow, text="View", command=view,width=20,bg='brown',fg='white').place(x=510,y=10)

tkWindow.title("Transaction Window")

Title_label = Label(tkWindow, text="Your transaction",width=20,font=("bold", 30),background="orange")  
Title_label.place(x=120,y=70) 
#update the variable with database
a=str(100)
Total_money= Label(tkWindow,text="Your total Money is :"+a,font=("bold", 20),background="orange")
Total_money.place(x=190,y=140)


var = IntVar()
R1 = Radiobutton(tkWindow, text="Enter the Amount", variable=var, value=1, command=sel)
R1.place(x=180,y=190)

R2 = Radiobutton(tkWindow, text="Enter the Quantity", variable=var, value=2,command=sel)
R2.place(x=380,y=190)
    
amount_entry = IntVar()
Entry(tkWindow,textvariable=amount_entry).place(x=280,y=230)
	
Submit_amount = Button(tkWindow, text="Modify Amount", command=validateLogin,width=20,bg='brown',fg='white')
Submit_amount.place(x=250,y=300)   
# tkWindow['background']='#2D2727'

# canvas.create_rectangle(0, 450, 670, 500, fill='orange')
# canvas.pack()

tkWindow.mainloop()