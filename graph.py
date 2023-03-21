from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

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


# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # list of squares
    y = [i**2 for i in range(101)]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.set_xlabel("time")
    plot1.set_ylabel("Price")
    # plot1.ylabel("Price")
    # plot1.set_facecolor("yellow")
    plot1.grid()
    plot1.legend("Stock Trends")
    plot1.plot(y,color="orange")
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = tkWindow)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=0,y=400)
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   tkWindow)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
tkWindow = Tk()
  
# setting the title 
tkWindow.title('Plotting in Tkinter')
  
# dimensions of the main window
tkWindow.geometry("700x900")

canvas = Canvas(tkWindow, width=700, height=100)
canvas.create_rectangle(0, 50, 700, 0, fill='orange')
canvas.pack()

tab1= Button(tkWindow, text="Open an Account", command=account,width=20,bg='brown',fg='white').place(x=10,y=10)
tab1= Button(tkWindow, text="Money In/Out", command=io,width=20,bg='brown',fg='white').place(x=170,y=10)
tab1= Button(tkWindow, text="Invest Now", command=invest,width=20,bg='brown',fg='white').place(x=340,y=10)
tab1= Button(tkWindow, text="View", command=view,width=20,bg='brown',fg='white').place(x=510,y=10)

Total_money= Label(tkWindow,text="Stock Trends",font=("bold", 20),background="orange")
Total_money.place(x=270,y=70)

# button that displays the plot
plot_button = Button(master = tkWindow, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.place(x=300,y=150)

# run the gui
tkWindow.mainloop()