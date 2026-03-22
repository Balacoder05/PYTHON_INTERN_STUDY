import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label.config(text="Result: " + str(result))
    except:
        label.config(text="Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()