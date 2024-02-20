from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("miles to km")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)


def input():
  miles = miles_input.get()
  km = float(miles) * 1.60934
  km_result_label.config(text=f"{km}")


miles_input = Entry(width=20)
print(miles_input.get())
miles_input.grid(row=1, column=1)

km_result_label = Label(text="0")
km_result_label.grid(row=2, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=2)
km_label = Label(text="km")
km_label.grid(row=2, column=2)
equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=2, column=0)

button = Button(text="Calculate", command=input)
button.grid(row=3, column=1)

window.mainloop()
