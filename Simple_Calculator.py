import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("350x550")
window.resizable(False, False)
window.configure(bg="#1e1e1e")


expression = ""


display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="#D4A37F",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=10, pady=15, ipady=10)



def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ) or event.char in ".+-*/()":
        return None

    return "break"



def sync_expression(event):
    global expression
    expression = display.get()


display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)



def button_click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(tk.END, expression)



def clear():
    global expression

    expression = ""
    display.delete(0, tk.END)



def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, tk.END)
    display.insert(tk.END, expression)



def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        expression = str(result)

    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")

        expression = ""



buttons = [
    ["3", "6", "9", "+"],
    ["2", "5", "8", "-"],
    ["1", "4", "7", "*"],
    ["=", ".", "0", "/"]
]



button_frame = tk.Frame(
    window,
    bg="#1e1e1e"
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)



clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="#d84f4f",
    fg="white",
    bd=0,
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)


backspace_button = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 18, "bold"),
    bg="#555555",
    fg="white",
    bd=0,
    command=backspace
)

backspace_button.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)


for row_index, row in enumerate(buttons, start=2):

    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = "#108ec0"

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#bd57b1"

        else:
            command = lambda v=value: button_click(v)
            color = "#8e9fc1"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )



for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)



window.mainloop()
