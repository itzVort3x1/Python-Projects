from tkinter import *

window = Tk()
window.title("Miles To Kilometers Converter")

#miles input widget
miles_input = Entry()
miles_input.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

kilometer_result_label = Label(text="0")
def conversion():
    result = 0
    user_input = float(miles_input.get())
    result = user_input * 1.609
    kilometer_result_label.config(text= f"{result}")
kilometer_result_label.grid(column=2, row=2)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(column=2, row=3)










window.mainloop()