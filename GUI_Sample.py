from tkinter import *

window = Tk()
window.geometry("280x450")
window.title("Calculator")
window.configure(bg="black")

#label
label = Label(window, text="Calculator", fg="white", bg="black", font=("Times", 20, 'bold'))
label.pack()

text_in = StringVar()
operator = ""


def click_button(number):
    global operator
    operator = operator + str(number)
    text_in.set(operator)


def equal():
    try:
        global operator

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(operator))

        text_in.set(total)

        # initialze the expression variable
        # by empty string
        operator = ""

        # if error is generate then handle
        # by the except block
    except:

        text.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global operator
    expression = ""
    text_in.set("")





text = Entry(window, textvariable=text_in, width="60", bd="5", bg="white")
text.pack()

text_in.set("enter your expression")



clear_button = Button(window, text="C", padx="5", pady="10", width="5", height="2", fg="black", bg="green", command=lambda: clear(),
                      font=("Times", 10, 'bold'))
clear_button.place(x=15, y=100)

divide_button = Button(window, text="/", padx="5", pady="10", width="5", height="2", fg="black", bg="green", command=lambda: click_button("/"),
                       font=("Times", 10, 'bold'))
divide_button.place(x=80, y=100)

multiply_button = Button(window, text="*", padx="5", pady="10", width="5", height="2",fg="black", bg="green",
                         command=lambda: click_button("*"), font=("Times", 10, 'bold'))
multiply_button.place(x=145, y=100)

substract_button = Button(window, text="-", padx="5", pady="10", width="5", height="2",fg="black", bg="green",
                          command=lambda: click_button("-"), font=("Times", 10, 'bold'))
substract_button.place(x=210, y=100)

# Second row buttons

seven_button = Button(window, text="7", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(7),
                      font=("Times", 10, 'bold'))
seven_button.place(x=15, y=170)

eight_button = Button(window, text="8", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(8),
                      font=("Times", 10, 'bold'))
eight_button.place(x=80, y=170)

nine_button = Button(window, text="9", padx="5", pady="10", width="5", height="2", fg="black", bg="green",command=lambda: click_button(9),
                     font=("Times", 10, 'bold'))
nine_button.place(x=145, y=170)

plus_button = Button(window, text="+", padx="5", pady="10", width="5", height="7",fg="black", bg="green", command=lambda: click_button("+"),
                     font=("Times", 10, 'bold'))
plus_button.place(x=210, y=170)

# third row buttons

four_button = Button(window, text="4", padx="5", pady="10", width="5", height="2", fg="black", bg="green",command=lambda: click_button(4),
                     font=("Times", 10, 'bold'))
four_button.place(x=15, y=240)

five_button = Button(window, text="5", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(5),
                     font=("Times", 10, 'bold'))
five_button.place(x=80, y=240)

six_button = Button(window, text="6", padx="5", pady="10", width="5", height="2", fg="black", bg="green",command=lambda: click_button(6),
                    font=("Times", 10, 'bold'))
six_button.place(x=145, y=240)

equal_button = Button(window, text="=", padx="5", pady="10", width="5", height="6",fg="black", bg="green", command=lambda: equal(),
                      font=("Times", 10, 'bold'))
equal_button.place(x=210, y=315)

# Fourth row button

one_button = Button(window, text="1", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(1),
                    font=("Times", 10, 'bold'))
one_button.place(x=15, y=310)

two_button = Button(window, text="2", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(2),
                    font=("Times", 10, 'bold'))
two_button.place(x=80, y=310)

three_button = Button(window, text="3", padx="5", pady="10", width="5", height="2",fg="black", bg="green", command=lambda: click_button(3),
                      font=("Times", 10, 'bold'))
three_button.place(x=145, y=310)

# fifth row button

zero_button = Button(window, text="0", padx="5", pady="10", width="14", height="2",fg="black", bg="green", command=lambda: click_button(0),
                     font=("Times", 10, 'bold'))
zero_button.place(x=15, y=380)

dot_button = Button(window, text=".", padx="5", pady="10", width="5", height="2", fg="black", bg="green",command=lambda: click_button("."),
                    font=("Times", 10, 'bold'))
dot_button.place(x=145, y=380)

window.mainloop()
