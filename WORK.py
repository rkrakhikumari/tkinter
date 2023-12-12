from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=600)

# label
my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=50)

# button
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me!", command=button_clicked)
new_button.grid(column=2, row=0)

# entry
input = Entry(width=20)
print(input.get())
input.grid(column=3, row=3)



window.mainloop()
