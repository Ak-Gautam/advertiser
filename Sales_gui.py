from tkinter import *
import pickle

#Loading the model
MODEL_PATH = "models/model3.sav"
loaded_model = pickle.load(open(MODEL_PATH, 'rb'))

#calculating sales w.r.t input
def calculate_sale(arg):
    res = loaded_model.predict([[tv.get(),radio.get()+newspaper.get()]])
    sale_label.config(text="Expected Sale : {:.2f}/-".format(100*(res[0])))

#Initializing the tkinter window
master = Tk()
master.geometry("700x400")
master.configure(background='#07575B')
master.title('Sales Estimater')

#Label to show the estimated sale
sale_label = Label(master, bg='#07575B', fg="white", font=("Times", 40, "bold"), text="Hello Tkinter!")
sale_label.pack(padx=5, pady=20)

#Scale to take TV advertising investment ammount from user
tv = Scale(master, length=650, label="TV", bg='#C4DFE6', fg="black", from_=0, to=2000, orient=HORIZONTAL , command=calculate_sale)
tv.set(10)
tv.pack(padx=5, pady=5)

#Scale to take Radio advertising investment ammount from user
radio = Scale(master, length=650, label="Radio", bg='#C4DFE6', fg="black",from_=0, to=2000, orient=HORIZONTAL, command=calculate_sale)
radio.set(10)
radio.pack(padx=5, pady=5)

#Scale to take Newspaper advertising investment ammount from user
newspaper = Scale(master, length=650, label="Newspaper", bg='#C4DFE6', fg="black", from_=0, to=2000, orient=HORIZONTAL, command=calculate_sale)
newspaper.set(10)
newspaper.pack(padx=5, pady=5)

#Showing the Application
mainloop()