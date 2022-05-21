from tkinter import *
calculator_window = Tk()
calculator_window.title("Calculator")
calculator_window.geometry("600x200")
calculator_window.maxsize(600, 200)
calculator_window.minsize(600, 200)
calculator_frame = Frame(calculator_window, bg="grey", borderwidth=5, relief=SUNKEN)
calculator_frame.grid()
calculator_frame_button = Frame(calculator_window)
calculator_frame_button.grid(sticky=W)
def add():
    add_result = Label(calculator_frame, text=f"The sum of {text1_value.get()} and {text2_value.get()}  is {text1_value.get() + text2_value.get()}", font=('cursive',20, 'bold')).grid(row=4, column=0)
def sub():
    sub_result = Label(calculator_frame, text=f"The subtraction of {text1_value.get()} and {text2_value.get()}  is {text1_value.get() - text2_value.get()}", font=('cursive',20, 'bold')).grid(row=4, column=0)
def mul():
    mul_result = Label(calculator_frame, text=f"The product of {text1_value.get()} and {text2_value.get()}  is {text1_value.get() * text2_value.get()}", font=('cursive',20, 'bold')).grid(row=4, column=0)
def div():
    div_result = Label(calculator_frame, text=f"The division of {text1_value.get()} and {text2_value.get()}  is {text1_value.get() / text2_value.get()}", font=('cursive',20, 'bold')).grid(row=4, column=0)
text1 = Label(calculator_frame, text="Enter the first value: ", font=('cursive',20, 'bold')).grid(row=0, column=0)
text2 = Label(calculator_frame, text="Enter the second value: ", font=('cursive',20, 'bold')).grid(row=1, column=0)

text1_value = IntVar()
text2_value = IntVar()
# text3_value = IntVar(text1_value, text2_value)

first_value = Entry(calculator_frame,textvariable=text1_value, font=('cursive',20, 'bold')).grid(row=0, column=1)
second_value = Entry(calculator_frame,textvariable=text2_value, font=('cursive',20, 'bold')).grid(row=1, column=1)
# third_value = Entry(textvariable=text3_value)

add = Button(calculator_frame_button, text='+', command=add, font=('cursive',20, 'bold')).grid(row=3, column=0)
sub = Button(calculator_frame_button, text='-', command=sub, font=('cursive',20, 'bold')).grid(row=3, column=1)
mul = Button(calculator_frame_button, text='X', command=mul, font=('cursive',20, 'bold')).grid(row=3, column=2)
div = Button(calculator_frame_button, text='/', command=div, font=('cursive',20, 'bold')).grid(row=3, column=3)
calculator_window.mainloop()