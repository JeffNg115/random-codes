import tkinter as tk

def addTwoNumbers():
    try:
        number1 = float(numberBox1.get())
        number2 = float(numberBox2.get())
        sum = number1 + number2
        label.config(text=f"The Sum is: {sum}")
    except ValueError:
        label.config(text="syntax error")

def changeTitle():
    window.title(str(titleBox.get()))

window = tk.Tk()
window.title("Gui application 101")


numberBox1 = tk.Entry(window)
numberBox1.pack()
numberBox2 = tk.Entry(window)
numberBox2.pack()

titleBox = tk.Entry(window)
titleBox.pack()

label = tk.Label(window, text="The Sum is:")
label.pack()

button = tk.Button(window, text="Im a button", command=addTwoNumbers)
button.pack()

canvas = tk.Canvas(window, bd=50, confine=True, bg="white")
canvas.pack()

button2 = tk.Button(canvas, text="Click to change the programme title!", command = changeTitle)
button2.pack()



window.mainloop()
