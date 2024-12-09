import tkinter as tk

# Function to update the entry box with button press
def button_click(value):
    current = entry.get()
    print(f"Button clicked: {value}")
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        print(f"Evaluating: {expression}")
        result = eval(expression)
        print(f"Result: {result}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        print(f"Error: {e}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry box
def clear():
    print("Clear button pressed")
    entry.delete(0, tk.END)

# Function to calculate the square of the current value
def square():
    try:
        current = float(entry.get())
        print(f"Calculating square of: {current}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, current ** 2)  # Square the value
    except ValueError:
        print("Invalid input for square")
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle backspace
def backspace():
    current = entry.get()
    print(f"Backspace: {current}")
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])  # Remove the last character

# Function to calculate percentage
def percentage():
    try:
        current = float(entry.get())
        print(f"Percentage calculation: {current}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, current / 100)  # Convert to percentage
    except ValueError:
        print("Invalid input for percentage") 
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("670x670")
root.config(bg="#2c3e50")  # Set background color

# Entry widget to display input and result
entry = tk.Entry(root, width=25, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button styling
button_style = {
    "width": 10,
    "height": 3,
    "font": ("Arial", 18),
    "relief": "raised",
    "bd": 5,
    "bg": "#ecf0f1",
    "activebackground": "#bdc3c7"
}

# Create buttons for digits and operations
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, **button_style, command=evaluate)
    else:
        button = tk.Button(root, text=text, **button_style, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create clear button
clear_button = tk.Button(root, text="C", **button_style, command=clear)
clear_button.grid(row=1, column=0, padx=5, pady=5)

# Create square (x^2) button
square_button = tk.Button(root, text="x²", **button_style, command=square)
square_button.grid(row=1, column=1, padx=5, pady=5)

# Create percentage button
percentage_button = tk.Button(root, text="%", **button_style, command=percentage)
percentage_button.grid(row=1, column=2, padx=5, pady=5)

# Create backspace button
backspace_button = tk.Button(root, text="←", **button_style, command=backspace)
backspace_button.grid(row=1, column=3, padx=5, pady=5)

# Run the main loop
root.mainloop()