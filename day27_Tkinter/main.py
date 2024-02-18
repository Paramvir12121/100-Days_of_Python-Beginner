from tkinter import *  

window = Tk()
window.title("My first GUI")
window.minsize(width=500,height=300)



my_label = Label(text="This is a label", font=("Arial",18,"bold"))
my_label.pack()

def button_click():
    entered_text = input.get()
    print(entered_text)
    my_label.config(text=entered_text)

input = Entry(width=20)
input.pack()

print(input.get())


button = Button( text="Click Me", command=button_click)
button.pack()




# it has to be at the very end
window.mainloop()