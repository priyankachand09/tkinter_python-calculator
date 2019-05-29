import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("Calculator")

First_Number = tk.Label(mainWindow,text="enter first number", pady=10, padx=20)
First_Number.pack()

First_Number_Value = tk.Entry(mainWindow)
First_Number_Value.pack()

Second_Number = tk.Label(mainWindow, text="enter second number", pady=10, padx=20)
Second_Number.pack()

Second_Number_Value = tk.Entry(mainWindow)
Second_Number_Value.pack()

operation_label = tk.Label(mainWindow, text="OPERATIONS", pady=10, padx=20)
operation_label.pack()


Addition = tk.Button(mainWindow, text="+", command=lambda: add(), pady=10, padx=20)
Addition.pack()
Subtract = tk.Button(mainWindow, text="-", command=lambda: sub(), pady=10, padx=20)
Subtract.pack()
Multiply = tk.Button(mainWindow,text="*",command=lambda:mul(),pady=(10), padx=(20))
Multiply.pack()
Division = tk.Button(mainWindow,text="/",command=lambda:divide(),pady=(10), padx=(20))
Division.pack()

Result_Label = tk.Label(mainWindow,text="result is",pady=(10), padx=(20))
Result_Label.pack()


def add():
    first, second = takeValueInput()
    result = first+second
    #print("result is" , result)
    Result_Label.config(text="OPERATION RESULT IS" + str(result))


def sub():
    first, second = takeValueInput()
    result = first-second
    Result_Label.config(text="OPERATION RESULT IS" + str(result))


def mul():
    first, second = takeValueInput()
    result = first*second
    Result_Label.config(text="OPERATION RESULT IS" + str(result))


def divide():
    first, second = takeValueInput()
    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
    Result_Label.config(text="OPERATION RESULT IS" + str(result))


def takeValueInput():
    first = First_Number_Value.get()
    second = Second_Number_Value.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(First_Number_Value.get()) == 0) or (len(Second_Number_Value.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


mainWindow.mainloop()
