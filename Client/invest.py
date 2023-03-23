import json
from tkinter import *
from tkinter import ttk
from conn import client, SIZE, FORMAT, user

data_resp = {"route": "stock_price", "data": {}}

client.send(json.dumps(data_resp).encode(FORMAT))
res = client.recv(SIZE * 10).decode(FORMAT)

res_js = json.loads(res)

data_resp = {"route": "get_investments", "data": {}}

client.send(json.dumps(data_resp).encode(FORMAT))
res = client.recv(SIZE).decode(FORMAT)
sell_data = json.loads(res)

# Create an instance of tkinter frame
tkWindow = Tk()

# Set the size of the tkinter window
tkWindow.geometry("700x800")
s = ttk.Style()
s.theme_use('clam')
tkWindow.resizable(False, False)
# tkWindow.["background"]="black"

canvas = Canvas(tkWindow, width=700, height=800)
canvas.create_rectangle(0, 50, 700, 0, fill='orange')
canvas.pack()


def account():
    tkWindow.destroy()
    import login


def io():
    tkWindow.destroy()
    import transaction


def invest():
    import invest
    tkWindow.destroy()


def view():
    tkWindow.destroy()
    import tables


tab1 = Button(tkWindow, text="Open an Account", command=account, width=20, bg='brown', fg='white').place(x=10, y=10)
tab1 = Button(tkWindow, text="Money In/Out", command=io, width=20, bg='brown', fg='white').place(x=170, y=10)
tab1 = Button(tkWindow, text="Invest Now", command=invest, width=20, bg='brown', fg='white').place(x=340, y=10)
tab1 = Button(tkWindow, text="View", command=view, width=20, bg='brown', fg='white').place(x=510, y=10)

labl_0 = Label(tkWindow, text="Invest Now", width=20, font=("bold", 20), bg="orange")
labl_0.place(x=180, y=60)

# Add a Treeview widget

labl_01 = Label(tkWindow, text="Availble to Buy ", width=20, font=("bold", 15), bg="orange")
labl_01.place(x=230, y=100)
tree = ttk.Treeview(tkWindow, column=("c1", "c2", "c3"), show='headings', height=5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="FName")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="LName")

# Insert the data in Treeview widget
count = 1
for name, val in res_js.items():
    tree.insert('', 'end', text="1", values=(str(count), name, val))
    count += 1

tree.place(x=10, y=150)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)


def get_item_select():
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        return record


tree.bind('<<TreeviewSelect>>', item_selected)


def confirm():
    conf = Toplevel(tkWindow)
    conf.geometry("600x500")
    conf.title("Purchased the stock")

    record = get_item_select()
    option = var.get()
    amount = amount_entry.get()
    d = {
        "option": option, 'amount': amount, 'name': record[1], 'price': record[2]
    }
    client.send(json.dumps({'route': 'confirm_buy', 'data': d}).encode(FORMAT))
    res = client.recv(SIZE).decode(FORMAT)
    res_js = json.loads(res)

    Label(conf, text="Purchased", font=('Arial 18 bold')).place(x=10, y=10)
    Label(conf, text="Congratulations You Bought the Stock ",
          font=('Arial 15'), bg="orange").place(x=100, y=50)
    Label(conf, text="and it will visible in your account within few minuates ",
          font=('Arial 15'), bg="orange").place(x=100, y=90)
    Label(conf, text="here are the details ",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=130)

    Label(conf, text=f"Name of the currency {res_js['currency']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=170)
    Label(conf, text=f"Quantity {res_js['quantity']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=200)
    Label(conf, text=f"Amount {res_js['amount']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=230)
    Label(conf, text=f"Date {res_js['date']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=260)

    # tree_sell.insert('', 'end', text="1", values=(str(id), name, str(price)))


def cancel():
    top.destroy()


def edit():
    pass


def Buy_Stock():
    global top, var
    top = Toplevel(tkWindow)
    top.geometry("700x400")
    top.title("Buy Stock Window")
    client.send(json.dumps({'route': 'get_user_cash', "data": {}}).encode(FORMAT))
    res = client.recv(SIZE)
    res = res.decode(FORMAT)
    res_js = json.loads(res)
    cash = res_js["cash"]
    record_selected = get_item_select()
    if cash <= float(record_selected[-1]):
        msg = "You have Money!"
        color = 'green'
    else:
        msg = "You don't have Sufficent Money"
        color = 'red'

    Label(top, text=msg, font=('Arial 15'),bg=color).place(x=200,y=50)
    Label(top, text="Are you sure you want to buy", font=('Arial 10')).place(x=200, y=80)

    var = IntVar()
    R1 = Radiobutton(top, text="Enter the Amount", variable=var, value=1, command=sel)
    R1.place(x=200, y=150)

    R2 = Radiobutton(top, text="Enter the Quantity", variable=var, value=2, command=sel)
    R2.place(x=400, y=150)

    global amount_entry
    amount_entry = IntVar()
    Entry(top, textvariable=amount_entry).place(x=300, y=200)

    # usernameEntry = Entry(tkWindow, textvariable=username)
    # usernameEntry.place(x=300,y=130)

    Button(top, text="Confirm", command=confirm, width=10, bg='Green', fg='white').place(x=100, y=250)
    Button(top, text="Cancel", command=cancel, width=10, bg='Red', fg='white').place(x=200, y=250)
    Button(top, text="Edit", command=edit, width=10, bg='Yellow', fg='white').place(x=300, y=250)

    return var

    # button


Button(tkWindow, text="Buy Stock",
       command=Buy_Stock, width=40, bg='brown', fg='white').place(x=200, y=300)

# sell
labl_01 = Label(tkWindow, text="Sell Stock ", width=20, font=("bold", 15), bg="orange")
labl_01.place(x=230, y=350)

tree_sell = ttk.Treeview(tkWindow, column=("c1", "c2", "c3"), show='headings', height=5)
tree_sell.column("# 1", anchor=CENTER)
tree_sell.heading("# 1", text="ID")
tree_sell.column("# 2", anchor=CENTER)
tree_sell.heading("# 2", text="FName")
tree_sell.column("# 3", anchor=CENTER)
tree_sell.heading("# 3", text="LName")

# Insert the data in Treeview widget
for id, name, price in sell_data['data']:
    tree_sell.insert('', 'end', text="1", values=(str(id), name, str(price)))

tree_sell.place(x=10, y=400)


def item_selected(event):
    for selected_item in tree_sell.selection():
        item = tree_sell.item(selected_item)
        print("--->>>", item)
        record = item['values']
        # record = json.dumps(record)
        return record


def get_item_select_sell():
    for selected_item in tree_sell.selection():
        item = tree.item(selected_item)
        record = item['values']
        return record


tree_sell.bind('<<TreeviewSelect>>', item_selected)


def confirm2():
    global res_js
    conf = Toplevel(tkWindow)
    conf.geometry("600x500")
    conf.title("Sold the stock")

    record = get_item_select_sell()
    d = {
        'id': record[0], 'amount': res_js[record[1]], 'name': record[1]
    }
    client.send(json.dumps({'route': 'sell_stock', 'data': d}).encode(FORMAT))
    res = client.recv(SIZE).decode(FORMAT)
    res_json = json.loads(res)

    Label(conf, text="Sold", font=('Arial 18 bold')).place(x=10, y=10)
    Label(conf, text="Congratulations You Sold the Stock ",
          font=('Arial 15'), bg="orange").place(x=100, y=50)
    Label(conf, text="and it will visible in your account within few minuates ",
          font=('Arial 15'), bg="orange").place(x=100, y=90)
    Label(conf, text="here are the details ",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=130)

    Label(conf, text=f"Name of the currency {res_json['currency']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=170)
    Label(conf, text=f"Amount {res_json['price']}",
          font=('Arial 10'), bg="green", fg="white").place(x=100, y=200)


def sel():
    selection = "You selected the option " + str(var.get())
    print(selection)


def Sell_Stock():
    top = Toplevel(tkWindow)
    top.geometry("700x400")
    top.title("Sell Stock Window")
    Label(top, text="Proceed to Sell", font=('Arial 18 bold')).place(x=10, y=10)
    # Label(top, text= "You don'thave Sufficent Money", font=('Arial 15'),bg="red").place(x=200,y=50)
    Label(top, text="You have Money in your accpunt", font=('Arial 15'), bg="green").place(x=200, y=50)
    Label(top, text="Are you sure you want to Sell", font=('Arial 10')).place(x=200, y=80)

    Button(top, text="Confirm2", command=confirm2, width=10, bg='Green', fg='white').place(x=200, y=250)
    Button(top, text="Cancel", command=cancel, width=10, bg='Red', fg='white').place(x=300, y=250)
    # button

Sell_Stock = Button(tkWindow, text="Sell Stock",
                    command=Sell_Stock, width=40, bg='brown', fg='white').place(x=200, y=550)

tkWindow.mainloop()
