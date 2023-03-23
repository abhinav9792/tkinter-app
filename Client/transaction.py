from tkinter import *
from conn import *
import json


# money function
def update_money():
    amount = amount_entry.get()
    client.send(json.dumps({'route': 'update_cash', 'data': {'amount': amount}}).encode('utf-8'))
    res = client.recv(SIZE).decode(FORMAT)
    tkWindow.destroy()
    import invest


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


# radio button
def sel():
    selection = "You selected the option " + str(var.get())
    print(selection)


tkWindow = Tk()
tkWindow.geometry("700x500")
tkWindow.resizable(False, False)

canvas = Canvas(tkWindow, width=700, height=800)
canvas.create_rectangle(0, 50, 700, 0, fill='orange')
canvas.pack()

tab1 = Button(tkWindow, text="Open an Account", command=account, width=20, bg='brown', fg='white').place(x=10, y=10)
tab1 = Button(tkWindow, text="Money In/Out", command=io, width=20, bg='brown', fg='white').place(x=170, y=10)
tab1 = Button(tkWindow, text="Invest Now", command=invest, width=20, bg='brown', fg='white').place(x=340, y=10)
tab1 = Button(tkWindow, text="View", command=view, width=20, bg='brown', fg='white').place(x=510, y=10)

tkWindow.title("Transaction Window")

Title_label = Label(tkWindow, text="Your transaction", width=20, font=("bold", 30), background="orange")
Title_label.place(x=120, y=70)
# update the variable with database
client.send(json.dumps({'route': 'get_user_cash', "data": {}}).encode(FORMAT))
res = client.recv(SIZE)
res = res.decode(FORMAT)
res_js = json.loads(res)
cash = res_js["cash"]
a = str(cash)
Total_money = Label(tkWindow, text="Your total Money is :" + a, font=("bold", 20), background="orange")
Total_money.place(x=190, y=140)

amount_entry = IntVar()
Entry(tkWindow, textvariable=amount_entry).place(x=280, y=230)

Submit_amount = Button(tkWindow, text="Modify Amount", command=update_money, width=20, bg='brown', fg='white')
Submit_amount.place(x=250, y=300)
# tkWindow['background']='#2D2727'

# canvas.create_rectangle(0, 450, 670, 500, fill='orange')
# canvas.pack()

tkWindow.mainloop()
