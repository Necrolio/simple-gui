import tkinter

window = tkinter.Tk()
window.geometry("400x40")
window.title("My Window")

btn1_text = tkinter.StringVar()

def callback():
    btn1_text.set("Button Pressed")

btn1 = tkinter.Button(window, textvariable = btn1_text, command = callback)
btn1.config(height = 5, width = 100)
btn1_text.set("Button")

btn1.pack()
window.mainloop()
