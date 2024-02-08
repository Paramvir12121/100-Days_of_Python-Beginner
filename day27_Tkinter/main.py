import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500,height=300)

my_label = tkinter.Label(text="This is a label", font=("Arial",18,"bold"))
my_label.pack()



# it has to be at the very end
window.mainloop()