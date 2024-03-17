import collections
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from numpy import *

program = Tk()
program.title("XO")


def arr_empty(array_empty):
    i = 0
    length_arr = len(array_empty)
    while i < length_arr:
        array_empty.remove(array_empty[length_arr-i-1])
        i += 1


def know():
    return var.get()


var = IntVar()
checkbox_Know = ttk.Checkbutton(program, variable=var, onvalue=True, offvalue=False)
checkbox_Know.grid(row=5, column=2, sticky='snew')
checkbox_Know.config(state=ACTIVE, command=know)
var.set(1)
var.get()


def replay():

    i = 0
    num = len(array_buttons)
    while i < num:
        array_buttons[i].config(text="", state=ACTIVE)
        i += 1
    var.set(1)


def function_XO(index_list_button):
    if know() == 1:
        array_buttons[index_list_button].config(text="X", font=20, fg="red")
        var.set(0)
        program.title("player 2")
        list_player1.append(index_list_button)
        winner_player1()
    elif know() == 0:
        array_buttons[index_list_button].config(text="O", font=20, fg="blue")
        var.set(1)
        program.title("player 1")
        list_player2.append(index_list_button)
        winner_player2()
    array_buttons[index_list_button].config(state=DISABLED)


list_player1 = []
list_player2 = []


def winner_player1():
    list_player1.sort()
    list_moins1 = []
    i = 0
    while i < (len(list_player1)-1):
        j = i+1
        result = list_player1[i] - list_player1[j]
        list_moins1.append(result)
        i += 1
    count_numbers_used = collections.Counter(list_moins1).most_common()
    print("1", count_numbers_used)
    if len(count_numbers_used) > 0:
        if count_numbers_used[0][1] == 3:
            print("player 1 is the winner")
            tkinter.messagebox.showinfo("player 1 is the winner")
            arr_empty(list_player1)
            arr_empty(list_player2)


def winner_player2():
    list_player2.sort()
    list_moins2 = []
    i = 0
    while i < (len(list_player1)-1):
        j = i+1
        result = list_player1[i] - list_player1[j]
        list_moins2.append(result)
        i += 1
    count_numbers_used = collections.Counter(list_moins2).most_common()
    print("2", count_numbers_used)
    if len(count_numbers_used) > 0:
        if count_numbers_used[0][1] == 3:
            print("player 2 is the winner")
            tkinter.messagebox.showinfo("player 2 is the winner")
            arr_empty(list_player1)
            arr_empty(list_player2)


btn1 = Button(program, text='')
btn1.grid(row=0, column=0, ipadx=40, ipady=40, sticky='snew')
btn1.config(command=lambda v=0: function_XO(v))

btn2 = Button(program, text='')
btn2.grid(row=0, column=1, ipadx=40, ipady=40, sticky='snew')
btn2.config(command=lambda v=1: function_XO(v))

btn3 = Button(program, text='')
btn3.grid(row=0, column=2, ipadx=40, ipady=40, sticky='snew')
btn3.config(command=lambda v=2: function_XO(v))

btn4 = Button(program, text='')
btn4.grid(row=0, column=3, ipadx=40, ipady=40, sticky='snew')
btn4.config(command=lambda v=3: function_XO(v))

btn5 = Button(program, text='')
btn5.grid(row=0, column=4, ipadx=40, ipady=40, sticky='snew')
btn5.config(command=lambda v=4: function_XO(v))

btn6 = Button(program, text='')
btn6.grid(row=1, column=0, ipadx=40, ipady=40, sticky='snew')
btn6.config(command=lambda v=5: function_XO(v))

btn7 = Button(program, text='')
btn7.grid(row=1, column=1, ipadx=40, ipady=40, sticky='snew')
btn7.config(command=lambda v=6: function_XO(v))

btn8 = Button(program, text='')
btn8.grid(row=1, column=2, ipadx=40, ipady=40, sticky='snew')
btn8.config(command=lambda v=7: function_XO(v))

btn9 = Button(program, text='')
btn9.grid(row=1, column=3, ipadx=40, ipady=40, sticky='snew')
btn9.config(command=lambda v=8: function_XO(v))

btn10 = Button(program, text='')
btn10.grid(row=1, column=4, ipadx=40, ipady=40, sticky='snew')
btn10.config(command=lambda v=9: function_XO(v))

btn11 = Button(program, text='')
btn11.grid(row=2, column=0, ipadx=40, ipady=40, sticky='snew')
btn11.config(command=lambda v=10: function_XO(v))

btn12 = Button(program, text='')
btn12.grid(row=2, column=1, ipadx=40, ipady=40, sticky='snew')
btn12.config(command=lambda v=11: function_XO(v))

btn13 = Button(program, text='')
btn13.grid(row=2, column=2, ipadx=40, ipady=40, sticky='snew')
btn13.config(command=lambda v=12: function_XO(v))

btn14 = Button(program, text='')
btn14.grid(row=2, column=3, ipadx=40, ipady=40, sticky='snew')
btn14.config(command=lambda v=13: function_XO(v))

btn15 = Button(program, text='')
btn15.grid(row=2, column=4, ipadx=40, ipady=40, sticky='snew')
btn15.config(command=lambda v=14: function_XO(v))

btn16 = Button(program, text='')
btn16.grid(row=3, column=0, ipadx=40, ipady=40, sticky='snew')
btn16.config(command=lambda v=15: function_XO(v))

btn17 = Button(program, text='')
btn17.grid(row=3, column=1, ipadx=40, ipady=40, sticky='snew')
btn17.config(command=lambda v=16: function_XO(v))

btn18 = Button(program, text='')
btn18.grid(row=3, column=2, ipadx=40, ipady=40, sticky='snew')
btn18.config(command=lambda v=17: function_XO(v))

btn19 = Button(program, text='')
btn19.grid(row=3, column=3, ipadx=40, ipady=40, sticky='snew')
btn19.config(command=lambda v=18: function_XO(v))

btn20 = Button(program, text='')
btn20.grid(row=3, column=4, ipadx=40, ipady=40, sticky='snew')
btn20.config(command=lambda v=19: function_XO(v))

btn21 = Button(program, text='')
btn21.grid(row=4, column=0, ipadx=40, ipady=40, sticky='snew')
btn21.config(command=lambda v=20: function_XO(v))

btn22 = Button(program, text='')
btn22.grid(row=4, column=1, ipadx=40, ipady=40, sticky='snew')
btn22.config(command=lambda v=21: function_XO(v))

btn23 = Button(program, text='')
btn23.grid(row=4, column=2, ipadx=40, ipady=40, sticky='snew')
btn23.config(command=lambda v=22: function_XO(v))

btn24 = Button(program, text='')
btn24.grid(row=4, column=3, ipadx=40, ipady=40, sticky='snew')
btn24.config(command=lambda v=23: function_XO(v))

btn25 = Button(program, text='')
btn25.grid(row=4, column=4, ipadx=40, ipady=40, sticky='snew')
btn25.config(command=lambda v=24: function_XO(v))

array_buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
                 btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25]

lab_player1 = Label(program, text="player 1 : X")
lab_player1.grid(row=6, column=0)
lab_player1.config()

lab_player2 = Label(program, text="player 2 : O")
lab_player2.grid(row=6, column=4)
lab_player2.config()

replay_button = Button(program, text="replay")
replay_button.grid(row=7, column=2, sticky="snew", pady=40, padx=20)
replay_button.config(command=replay)

program.mainloop()
