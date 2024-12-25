import tkinter as tk
from math import sin, cos, tan, radians

# Function to evaluate expressions
def evaluate_expression(expression):
    try:
        # Handle trigonometric functions
        if "sin" in expression:
            number = float(expression.split("sin")[1])
            return sin(radians(number))
        elif "cos" in expression:
            number = float(expression.split("cos")[1])
            return cos(radians(number))
        elif "tan" in expression:
            number = float(expression.split("tan")[1])
            return tan(radians(number))
        # Handle basic arithmetic
        else:
            return eval(expression)
    except Exception as e:
        return "Error"

# Function to handle button clicks
def on_button_click(button_text):
    if button_text == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    elif button_text == "=":
        expression = entry.get()  # Get the user input
        result = evaluate_expression(expression)  # Calculate result
        entry.delete(0, tk.END)
        entry.insert(0, str(result))  # Display result
    else:
        entry.insert(tk.END, button_text)  # Add button text to the entry field

# GUI Setup
root = tk.Tk()
root.title("Calculator")

# Entry widget for user input
entry = tk.Entry(root, width=30, font=("Arial", 14), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "sin", "cos", "tan", "C",
    
]

# Create and place buttons
row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(
        root,
        text=button_text,
        width=7,
        height=2,
        font=("Arial", 12),
        command=lambda text=button_text: on_button_click(text)
    )
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
