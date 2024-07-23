import tkinter as tk

def calculate():
  """
  This function retrieves user input, performs the selected operation, and displays the result.
  """
  try:
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    operation = operation_var.get()

    if operation == "+":
      result = num1 + num2
    elif operation == "-":
      result = num1 - num2
    elif operation == "*":
      result = num1 * num2
    elif operation == "/":
      if num2 == 0:
        result = "Error: Division by zero"
      else:
        result = num1 / num2
    else:
      result = "Invalid operation"

    result_label.config(text="Result: " + str(result))
  except ValueError:
    result_label.config(text="Error: Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create labels and entry fields for numbers
number1_label = tk.Label(window, text="Number 1:")
number1_label.grid(row=0, column=0)
number1_entry = tk.Entry(window)
number1_entry.grid(row=0, column=1)

number2_label = tk.Label(window, text="Number 2:")
number2_label.grid(row=1, column=0)
number2_entry = tk.Entry(window)
number2_entry.grid(row=1, column=1)

# Create label and dropdown menu for operation selection
operation_label = tk.Label(window, text="Operation:")
operation_label.grid(row=2, column=0)

operation_var = tk.StringVar(window)
operation_var.set("+")  # Set default operation to addition
operation_menu = tk.OptionMenu(window, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

# Create a button to trigger calculation and a label to display the result
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(window, text="")
result_label.grid(row=4, columnspan=2)

window.mainloop()
