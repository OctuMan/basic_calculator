# import modules 
from tkinter import *
from tkinter.ttk import *
import re

# declare the main window 
root=Tk()
# title
root.title('Calculator')

# root.geometry(width x height + left + top )
root.geometry('420x500+600+150')

#controle resize width and/or height by true or false values
root.resizable(True , False)
#  background
# root.config(background='#ccc')
# favicon
root.iconbitmap(r'C:\Users\Said Lehoufi\Desktop\Python\basic_calculator\Calculator2.ico')

# minimal size 
root.minsize(450,400)

# frames

fr1=Frame(width='500', height='40' )
fr1.place(x=50, y=0)

fr2=Frame(width='300', height='50')
fr2.place(x=20, y=80)

fr3=Frame(width='300', height='200' )
fr3.place(x=20, y=135)

fr4=Frame(width='60', height='260')
fr4.place(x=320, y=80)


# Specify a larger font to increase the height
larger_font = ('Arial', 20)

style=Style()
style.configure('styled_btn.TButton', font =
               ('calibri', 10, 'bold', ),
               padding=(5, 10, 5, 10)
                )
style.configure('styled_clear_btn.TButton', font =
               ('calibri', 10, 'bold', ),
               padding=(5, 10, 5, 10),
               background='#FF6A74'
                )
# functions 

def onclick(text):
    ''' This function runs when click on a button'''
    if text == 'clear':
        clear()
    elif text == 'CE':
        ce()
    elif text == '=':
        result()
    else:
        display.insert(END, text)
        
def ce():
    ''' Clear one element '''
    current_text = input_value.get()
    # Remove the last character from the display
    display.delete(len(current_text) - 1, 'end')

def clear(): 
    ''' Empthy the entry field'''
    input_value.set(' ')

def result():
    ''' Proccessing the operations and show the result'''
    expression = input_value.get()
    try:
        result=eval(expression)
        clear()
        display.insert('end',result)
    except:
        clear()
        display.insert(0,'Error')
   
# content 
from tkinter import ttk
# the display widget
input_value=StringVar()
display = Entry(fr1, font=larger_font, textvariable=input_value, justify='right')
display.grid(row=0, column=0, columnspan=5, pady=20, sticky='ew')

extra_buttons=[
     ('clear', 1, 1), ('CE', 1, 2), ('%', 1, 3),
]
for (btn_text, btn_row, btn_col) in extra_buttons:
    btn = Button(fr2, text=btn_text, command=lambda text=btn_text: onclick(text), style='styled_btn.TButton')
    btn.grid(row=btn_row, column=btn_col)

num_buttons_layout = [
    ('1', 2, 1), ('2', 2, 2), ('3',2, 3),
    ('4', 3, 1), ('5', 3, 2),('6',3,3),('7',4,1),
    ('8', 4, 2), ('9', 4, 3), ('0', 5,2),
    ('#', 5, 1), ('.', 5, 3),
]
for (btn_text, btn_row, btn_col) in num_buttons_layout:
    btn = Button(fr3, text=btn_text, command=lambda text=btn_text: onclick(text), style='styled_btn.TButton')
    btn.grid(row=btn_row, column=btn_col)

char_buttons_layout = [
    ('+', 1, 4), ('-', 2, 4), ('/', 3, 4),
    ('x', 4, 4), ('=', 5, 4),
]
for (btn_text, btn_row, btn_col) in char_buttons_layout:
    btn = Button(fr4, text=btn_text, command=lambda text=btn_text: onclick(text), style='styled_btn.TButton')
    btn.grid(row=btn_row, column=btn_col, pady=0.50)


# Start the main loop
root.mainloop()
