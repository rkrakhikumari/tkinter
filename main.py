from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("My first GUI")

# LABEL
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    print("I got clicked!")
    new_text = entry.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()

# ENTRY
entry = Entry(width=20)


entry.pack()
print(entry.get())

# TEXT
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multiline text entry")
print(text.get("1.0", END))
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# scale
def scale_used(value):
    print(value)
scale = Scale(from_=0 , to=100, command=scale_used)
scale.pack()

# checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



