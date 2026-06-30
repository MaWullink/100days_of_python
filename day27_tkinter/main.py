from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=80)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(3, weight=1)

# Input-box
user_input = Entry(width=5)
user_input.grid(row=0, column=1)

# Button
def clicked():
    miles = float(user_input.get())
    kilometers = round(miles*1.609934, 1)
    converted.config(text=kilometers)

button = Button(text="Convert", command=clicked)
button.grid(row=1, column=1, padx=5, pady=5)
# Label
miles_input = Label(text = "Miles")
miles_input.grid(row=0, column=2)
kilometers_input = Label(text="Kilometers")
kilometers_input.grid(row=2, column=2)
converted = Label(text="")
converted.grid(row=2, column=1)



window.mainloop()