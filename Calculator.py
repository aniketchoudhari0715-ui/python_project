import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x700")
root.resizable(False, False)

# Global variable to store expression
expression = ""

# Function to update expression in display
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear display
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar for display
equation = tk.StringVar()

# Display Entry box
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25)

# Button styling
btn_font = ('Arial', 14)

# Number Buttons
tk.Button(root, text='7', font=btn_font, command=lambda: press(7), height=2, width=5).grid(row=1, column=0)
tk.Button(root, text='8', font=btn_font, command=lambda: press(8), height=2, width=5).grid(row=1, column=1)
tk.Button(root, text='9', font=btn_font, command=lambda: press(9), height=2, width=5).grid(row=1, column=2)
tk.Button(root, text='/', font=btn_font, command=lambda: press('/'), height=2, width=5).grid(row=1, column=3)

tk.Button(root, text='4', font=btn_font, command=lambda: press(4), height=2, width=5).grid(row=2, column=0)
tk.Button(root, text='5', font=btn_font, command=lambda: press(5), height=2, width=5).grid(row=2, column=1)
tk.Button(root, text='6', font=btn_font, command=lambda: press(6), height=2, width=5).grid(row=2, column=2)
tk.Button(root, text='*', font=btn_font, command=lambda: press('*'), height=2, width=5).grid(row=2, column=3)

tk.Button(root, text='1', font=btn_font, command=lambda: press(1), height=2, width=5).grid(row=3, column=0)
tk.Button(root, text='2', font=btn_font, command=lambda: press(2), height=2, width=5).grid(row=3, column=1)
tk.Button(root, text='3', font=btn_font, command=lambda: press(3), height=2, width=5).grid(row=3, column=2)
tk.Button(root, text='-', font=btn_font, command=lambda: press('-'), height=2, width=5).grid(row=3, column=3)

tk.Button(root, text='0', font=btn_font, command=lambda: press(0), height=2, width=5).grid(row=4, column=0)
tk.Button(root, text='C', font=btn_font, command=clear, height=2, width=5, bg='red', fg='white').grid(row=4, column=1)
tk.Button(root, text='=', font=btn_font, command=equal, height=2, width=5, bg='green', fg='white').grid(row=4, column=2)
tk.Button(root, text='+', font=btn_font, command=lambda: press('+'), height=2, width=5).grid(row=4, column=3)

# Run application
root.mainloop()
