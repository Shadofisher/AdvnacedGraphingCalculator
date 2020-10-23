from tkinter import *
from tkinter import filedialog
# from sympy import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

pos = 0
i = 0

master = Tk()

c1 = Canvas(master, width=600, height=170, bg='lightgreen')

x, y, z = sp.symbols('x,y,z')

current_entry = ''
shiftvala = '0'


# shiftval = ''


class Stack:
    mystack_ptr = 0
    mystack = []

    def __init__(self):
        self.mystack_ptr = 0
        self.mystack = []

    def push(self, data):
        self.mystack.append(data)
        self.mystack_ptr = self.mystack_ptr + 1
        print(self.mystack_ptr)

    def pop(self):
        self.mystack_ptr = self.mystack_ptr - 1
        print(self.mystack_ptr)
        return self.mystack.pop()

    def get(self, index):
        return self.mystack[index]

    def get_index(self):
        return self.mystack_ptr


stk = Stack()


def is_mynumber(a):
    try:
        int(a)
        return True
    except:
        return False


def show_stack(window, current_entry, shiftval):
    print("Showing stack....")

    window.delete("all")
    window.create_text(20, 30, fill="darkblue", font="Times 20 italic bold", text="4 :")
    window.create_text(20, 60, fill="darkblue", font="Times 20 italic bold", text="3 :")
    window.create_text(20, 90, fill="darkblue", font="Times 20 italic bold", text="2 :")
    window.create_text(20, 120, fill="darkblue", font="Times 20 italic bold", text="1 :")
    window.create_text(20, 150, fill="darkblue", font="Times 20 italic bold", text="")

    n = stk.get_index()
    if n > 3:
        n = 3

    print("Number of stack entries: " + str(n) + " " + str(stk.get_index()))

    if n > 0:
        stk.get((stk.get_index() - 1))

    for i in range(n):
        window.create_text(580 - (5 * len(stk.get((stk.get_index()) - i - 1))), 120 - (30 * i), fill="darkblue",
                           font="Times 17 italic bold", text=stk.get((stk.get_index()) - i - 1))

    window.create_text(580 - (6 * len(current_entry)), 150, fill="darkblue", font="Times 17 italic bold",
                       text=current_entry)
    print(current_entry)
    if shiftval == 'A':
        print("ShiftvalA found")
        window.create_text(400, 10, font="Times 10 italic bold", text="Shift A")
    if shiftval == 'B':
        window.create_text(400, 10, font="Times 10 italic bold", text="Alpha")



def get_base(val):
    if '0b' in val:
        return 2
    elif '0x' in val:
        return 16
    elif '0o' in val:
        return 8
    else:
        return 10


def b_callback(window, val):
    global current_entry
    global shiftvala
    if "<error:" in current_entry:
        current_entry = ''
    # show_stack(window,current_entry,shiftval)
    print(val)
    if "ENTER" not in val:
        if val.isnumeric() or val == '.':
            current_entry = current_entry + str(val)
        if val == 'Var X':
            if shiftvala == 'B':
                current_entry = current_entry + 'x'
            else:
                current_entry = current_entry + "x"
        print(len(current_entry))
    if "ENTER" in val:
        stk.push(current_entry)
        current_entry = ''

    if "X" == val:
        if not current_entry and stk.get_index() >= 2:
            current_entry = stk.pop()
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "*" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry and stk.get_index() >= 1:
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "*" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            # ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = "<error: not enough arguments>"
            # window.create_text(580-(6*len("<error: not enough args>")),150,fill="darkblue",font="Times 17 italic bold",text="<error: not enough args>")

    if "/" == val:
        if not current_entry and stk.get_index() >= 2:
            current_entry = stk.pop()
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "/" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry and stk.get_index() >= 1:
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "/" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = "<error: not enough arguments>"
            # window.create_text(580-(6*len("<error: not enough args>")),150,fill="darkblue",font="Times 17 italic bold",text="<error: not enough args>")

    if "+" == val:
        if not current_entry and stk.get_index() >= 2:
            current_entry = stk.pop()
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "+" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry and stk.get_index() >= 1:
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "+" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = "<error: not enough arguments>"
            # window.create_text(580-(6*len("<error: not enough args>")),150,fill="darkblue",font="Times 17 italic bold",text="<error: not enough args>")

    if "-" == val:
        if not current_entry and stk.get_index() >= 2:
            current_entry = stk.pop()
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "-" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry and stk.get_index() >= 1:
            val1 = stk.pop()
            function = ("(" + str(val1) + ")" + "-" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            ans = expr.evalf()
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = "<error: not enough arguments>"
            # window.create_text(580-(6*len("<error: not enough args>")),150,fill="darkblue",font="Times 17 italic bold",text="<error: not enough args>")
    if "SWAP" == val:
        show_stack(window, current_entry, shiftvala)
        if stk.get_index() >= 2:
            value1 = stk.pop()
            value2 = stk.pop()
            stk.push(value1)
            stk.push(value2)
            current_entry = ''
    if "DROP" in val:
        if stk.get_index() >= 1:
            stk.pop()
    if "SIN" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            if shiftvala == 'A':
                function = (sp.asin("(" + str(current_entry) + ")"))
                shiftvala = ''
            else:
                function = (sp.sin("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry:
            if shiftvala == 'A':
                function = (sp.asin("(" + str(current_entry) + ")"))
                shiftvala = ''
            else:
                function = (sp.sin("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'

    if "COS" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            function = (sp.cos("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry:
            function = (sp.cos("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'

    if "TAN" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            function = (sp.tan("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry:
            function = (sp.tan("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'

    if "HEX" == val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            try:
                current_entry = hex(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        elif current_entry:
            try:
                current_entry = hex(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        else:
            current_entry = '<error: not enough arguments>'
    if "DEC" == val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            try:
                current_entry = str(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        elif current_entry:
            try:
                current_entry = str(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        else:
            current_entry = '<error: not enough arguments>'
    if "BIN" == val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            try:
                current_entry = bin(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        elif current_entry:
            try:
                current_entry = bin(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        else:
            current_entry = '<error: not enough arguments>'
    if "OCT" == val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            try:
                current_entry = oct(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        elif current_entry:
            try:
                current_entry = oct(int(current_entry, get_base(current_entry)))
                stk.push(current_entry)
                current_entry = ''
            except:
                current_entry = "<error: > Converting to Hex"
        else:
            current_entry = '<error: not enough arguments>'

    if "LOG" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            function = (sp.log("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        elif current_entry:
            function = (sp.log("(" + str(current_entry) + ")"))
            expr = sp.sympify(function)
            # ans = expr.evalf()
            ans = expr
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'
    if "INT(x)" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'A'
        else:
            if not current_entry and stk.get_index() >= 1:
                current_entry = stk.pop()
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.integrate(expr, x)
                stk.push(str(ans))
                current_entry = ''
            elif current_entry:
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.integrate(expr, x)
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'

    if "DIFF(x)" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'B'
        else:
            if not current_entry and stk.get_index() >= 1:
                current_entry = stk.pop()
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.diff(expr, x)
                stk.push(str(ans))
                current_entry = ''
            elif current_entry:
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.diff(expr, x)
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'

    if "SQRT" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            function = str(current_entry)
            expr = sp.sympify(function)
            ans = sp.sqrt(expr)
            stk.push(str(ans))
            current_entry = ''
        elif current_entry:
            function = str(current_entry)
            expr = sp.sympify(function)
            ans = sp.sqrt(expr)
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'

    # Expand
    if "Expand" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'C'
        else:
            if not current_entry and stk.get_index() >= 1:
                current_entry = stk.pop()
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.expand(expr)
                stk.push(str(ans))
                current_entry = ''
            elif current_entry:
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.expand(expr)
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'
    # SLVE
    if "SLVE" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'D'
        else:
            if not current_entry and stk.get_index() >= 1:
                current_entry = stk.pop()
                stk.push(current_entry)
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.solve(expr, x)
                stk.push(str(ans))
                current_entry = ''
            elif current_entry:
                stk.push(current_entry)
                function = str(current_entry)
                expr = sp.sympify(function)
                ans = sp.solve(expr, x)
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'
    # Power
    if "POW" in val:
        if not current_entry and stk.get_index() >= 2:
            current_entry = stk.pop()
            val1 = stk.pop()
            if current_entry.isnumeric():
                arg1 = float(current_entry)
            else:
                arg1 = sp.sympify(current_entry)
            if val1.isnumeric():
                arg2 = float(val1)
            else:
                arg2 = sp.sympify(val1)
            ans = sp.Pow(arg2, arg1)
            stk.push(str(ans))
            current_entry = ''
        elif current_entry and stk.get_index() >= 1:
            val1 = stk.pop()
            if current_entry.isnumeric():
                arg1 = float(current_entry)
            else:
                arg1 = sp.sympify(current_entry)
            if val1.isnumeric():
                arg2 = float(val1)
            else:
                arg2 = sp.sympify(val1)
            ans = sp.Pow(arg2, arg1)
            stk.push(str(ans))
            current_entry = ''
        else:
            current_entry = "<error: not enough arguments>"
    # DUPLICATE
    if "DUP" in val:
        if not current_entry and stk.get_index() >= 1:
            current_entry = stk.pop()
            stk.push(current_entry)
            stk.push(current_entry)
            current_entry = ''
        elif current_entry:
            stk.push(current_entry)
            stk.push(current_entry)
            current_entry = ''
        else:
            current_entry = '<error: not enough arguments>'
    # EVALUATE
    if "EVAL" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'E'
        else:
            if not current_entry and stk.get_index() >= 1:
                current_entry = stk.pop()
                expr = sp.sympify(current_entry)
                ans = expr.evalf()
                stk.push(str(ans))
                current_entry = ''
            elif current_entry:
                expr = sp.sympify(current_entry)
                ans = expr.evalf()
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'
    # SUBSTITUE
    if "SUBS" in val:
        if shiftvala == 'B':
            current_entry = current_entry + 'F'
        else:
            if not current_entry and stk.get_index() >= 1:
                val1 = stk.pop()
                current_entry = stk.pop()
                expr = sp.sympify(current_entry)
                ans = expr.subs(x, sp.sympify(val1))
                stk.push(str(current_entry))
                stk.push(str(ans))
                current_entry = ''
            elif current_entry and stk.get_index() >= 1:
                function = stk.pop()
                expr = sp.sympify(function)
                ans = expr.subs(x, sp.sympify(current_entry))
                stk.push(str(function))
                stk.push(str(ans))
                current_entry = ''
            else:
                current_entry = '<error: not enough arguments>'

    if "Plot" in val:
        if shiftvala == 'A':  # GPS
            if not current_entry and stk.get_index() >= 1:

                val1 = stk.pop()
                a = val1.split('.')
                print(a)
                tmp = a[0][len(a[0]) - 2:len(a[0])]
                if tmp:
                    Val_1 = tmp + '.' + a[1]
                else:
                    Val_1 = '0' + '.' + a[1]
                Val_2 = a[0][:len(a[0]) - 2]
                print("Val1 = " + Val_1)
                print("Val2 = " + Val_2)
                if Val_2:
                    gps = str(int(Val_2) + float(Val_1) / 60)
                else:
                    gps = str(float(Val_1) / 60)
                print(gps)
                stk.push(gps)
                current_entry = ''
                shiftvala = ''
            elif current_entry:
                val1 = current_entry
                a = val1.split('.')
                print(a)
                tmp = a[0][len(a[0]) - 2:len(a[0])]
                if tmp:
                    Val_1 = tmp + '.' + a[1]
                else:
                    Val_1 = '0' + '.' + a[1]
                Val_2 = a[0][:len(a[0]) - 2]
                print("Val1 = " + Val_1)
                print("Val2 = " + Val_2)
                if Val_2:
                    gps = str(int(Val_2) + float(Val_1) / 60)
                else:
                    gps = str(float(Val_1) / 60)
                print(gps)
                stk.push(gps)
                current_entry = ''
                shiftvala = ''
            else:
                current_entry = '<error: not enough arguments>'
        else:
            if not current_entry and stk.get_index() >= 3:
                val1 = stk.pop()
                val2 = stk.pop()
                function = stk.pop()
                if is_mynumber(val1) and is_mynumber(val2):
                    print("Val1" + val1)
                    print("Val2" + val2)
                    # x_range = [i for i in range(int(val1),int(val2)+1)]
                    x_range = np.linspace(int(val1), int(val2), 1000)
                    expr = sp.sympify(function)
                    y_range = [expr.subs(x, i) for i in x_range]
                    stk.push(function)
                    plt.style.use('fivethirtyeight')
                    plt.plot(x_range, y_range)
                    plt.show()
                else:
                    current_entry = '<error: ranges must be int>'
                    stk.push(function)
                # expr = sp.sympify(current_entry)
                # ans = expr.subs(x,sp.sympify(val1))
                # stk.push(str(current_entry))
                # stk.push(str(ans))
                # current_entry=''
            else:
                current_entry = '<error: not enough arguments>'

    # PI
    if "PI" in val:
        current_entry = current_entry + str(sp.pi)

    if "Clr" in val:
        current_entry = ''

    # +/-
    if "+/-" == val:
        if current_entry:
            function = ("(" + "-1" + ")" + "*" + "(" + str(current_entry) + ")")
            expr = sp.sympify(function)
            ans = expr
            current_entry = str(ans)
        else:
            current_entry = '<error: not enough arguments>'

    if "SHFTa" == val:
        if shiftvala == 'A':
            shiftvala = ''
        else:
            shiftvala = 'A'
        print("shiftval = " + shiftvala)

    if "ALPHA" == val:
        if (shiftvala == 'B'):
            shiftvala = ''
        else:
            shiftvala = 'B'
        print("shiftval = " + shiftvala)
    if "BACK" == val:
        if len(current_entry) > 1:
            current_entry = current_entry[:-1]

    if "C2C" == val:
        master.clipboard_clear()
        if stk.get_index() >= 1:
            c2c = stk.pop()
            stk.push(c2c)
            master.clipboard_append(c2c)
    if "CFC" == val:
        try:
            cfc = master.clipboard_get();
            stk.push(cfc)
        except:
            current_entry= "<error: clipboard empty>"



    show_stack(window, current_entry, shiftvala)


def create_buttons(row, col, master, c1, buttons, origin_x, origin_y, but_width, but_height):
    global frame_list
    startx = origin_x
    starty = origin_y
    frame_list = []
    buttons_list = []
    for j in range(row):
        for i in range(col):
            frame_list.append(Frame(master, width=but_width, height=but_height, bd=3, bg='grey'))
            frame_list[len(frame_list) - 1].place(x=startx, y=starty)
            buttons_list.append(Button(frame_list[len(frame_list) - 1], text=buttons[len(frame_list) - 1][0],
                                       bg=buttons[len(frame_list) - 1][2], fg=buttons[len(frame_list) - 1][1],
                                       command=lambda i=buttons[len(frame_list) - 1][0]: b_callback(c1, i)))
            buttons_list[len(buttons_list) - 1].place(relwidth=1, relheight=1, anchor='nw')
            buttons_list[len(buttons_list) - 1].command = lambda: b_callback()
            startx = startx + 55
        startx = origin_x
        starty = starty + 50
    # print(b1['text'])


def create_labels(row, col, master, buttons, origin_x, origin_y):
    global frame_list
    startx = origin_x
    starty = origin_y
    frame_list = []
    buttons_list = []
    for j in range(row):
        for i in range(col):
            label1 = Label(master, text=buttons[j][0], font="Times 8 italic bold", fg='green')
            label1.place(x=startx, y=starty)
            # label1=Label(master,text =buttons[j][1],font="Times 7 italic bold",fg='red')
            # label1.place(x=startx+24,y=starty)
            startx = startx + 55
        startx = origin_x
        starty = starty + 50


def one_pressed(event):
    # b_callback(win,"1")
    print("Pressed " + str(event.char) + "     " + str(event.keysym))
    if is_mynumber(str(event.char)) or str(event.char) == '.':
        b_callback(c1, str(event.char))
    if str(event.char) == '*':
        b_callback(c1, 'X')
    if str(event.char) == '/':
        b_callback(c1, '/')
    if str(event.char) == '-':
        b_callback(c1, '-')
    if str(event.char) == '+':
        b_callback(c1, '+')
    if str(event.keysym) == 'Return' or str(event.keysym) == 'KP_Enter':
        b_callback(c1, 'ENTER')
    if str(event.char) == 'A' or str(event.char) == 'b' \
            or str(event.char) == 'c' or str(event.char) == 'd' or str(event.char) == 'e' or str(event.char) == 'f':
        shiftvala = 'B'
        b_callback(c1, str(event.char))


def enter_pressed(win):
    b_callback(win, "ENTER")
    print("Pressed eneter")


def main():
    pos = 0
    master.geometry("680x480")
    master.title("Advanced Scientific Calculator. Powered by Sympy and Numpy")

    c1.place(x=10, y=10)
    # canvas. create_text(100,10,fill="darkblue",font="Times 20 italic bold", text="Click the bubbles that are multiples of two.")
    c1.create_text(20, 30, fill="darkblue", font="Times 20 italic bold", text="4 :")
    c1.create_text(20, 60, fill="darkblue", font="Times 20 italic bold", text="3 :")
    c1.create_text(20, 90, fill="darkblue", font="Times 20 italic bold", text="2 :")
    c1.create_text(20, 120, fill="darkblue", font="Times 20 italic bold", text="1 :")
    c1.create_text(20, 150, fill="darkblue", font="Times 20 italic bold", text="")

    buttons = [('7', 'black', 'lightgrey'), ('8', 'black', 'lightgrey'), ('9', 'black', 'lightgrey'),
               ('/', 'black', 'lightgrey'), ('Clr', 'black', 'lightgrey'), ('4', 'black', 'lightgrey'),
               ('5', 'black', 'lightgrey'), ('6', 'black', 'lightgrey'), ('X', 'black', 'lightgrey'),
               ('RES2', 'red', 'lightgrey'), ('1', 'black', 'lightgrey'), ('2', 'black', 'lightgrey'),
               ('3', 'black', 'lightgrey'), ('-', 'black', 'lightgrey'), ('PI', 'black', 'lightgrey'),
               ('0', 'black', 'lightgrey'), ('.', 'black', 'lightgrey'), ('SQRT', 'black', 'lightgrey'),
               ('+', 'black', 'lightgrey'), ('POW', 'black', 'lightgrey')]
    create_buttons(4, 5, master, c1, buttons, 100, 300, 50, 30)

    buttons = [('SIN', 'black', 'lightgrey'), ('COS', 'black', 'lightgrey'), ('TAN', 'black', 'lightgrey'),
               ('LOG', 'black', 'lightgrey')]
    create_buttons(4, 1, master, c1, buttons, 25, 300, 50, 30)
    buttons = [('ASIN', '-1'), ('ACOS', '-1'), ('ATAN', '-1'), ('res', 'x')]
    create_labels(4, 1, master, buttons, 25, 300 - 20)

    buttons = [('ENTER', 'white', 'darkgrey')]
    create_buttons(1, 1, master, c1, buttons, 25, 250, 125, 30)

    buttons = [('+/-', 'black', 'lightgrey'), ('EEX', 'black', 'lightgrey'), ('DEL', 'black', 'lightgrey'),
               ('BACK', 'black', 'lightgrey'), ('SWAP', 'black', 'lightgrey'), ('DROP', 'black', 'lightgrey'),
               ('DUP', 'black', 'lightgrey'), ('SHFTa', 'black', 'lightgreen')]
    create_buttons(1, 8, master, c1, buttons, 160, 250, 50, 30)

    buttons = [('INT(x)', 'black', 'lightgrey'), ('DIFF(x)', 'black', 'lightgrey'), ('Expand', 'black', 'lightgrey'),
               ('SLVE', 'black', 'lightgrey')]
    create_buttons(4, 1, master, c1, buttons, 380, 300, 60, 30)

    buttons = [('EVAL', 'black', 'lightgrey'), ('SUBS(x)', 'black', 'lightgrey'), ('Var X', 'black', 'lightgrey'),
               ('Plot', 'black', 'lightgrey')]
    create_buttons(4, 1, master, c1, buttons, 450, 300, 60, 30)

    buttons = [('HEX', 'black', 'lightgrey'), ('BIN', 'black', 'lightgrey'), ('OCT', 'black', 'lightgrey'),
               ('DEC', 'black', 'lightgrey')]
    create_buttons(4, 1, master, c1, buttons, 520, 300, 60, 30)

    buttons = [('A', '0'), ('B', '0'), ('C', '0'), ('D', '0')]
    create_labels(4, 1, master, buttons, 400, 300 - 20)
    buttons = [('E', '0'), ('F', '0'), ('X', '0'), ('GPS', '0')]
    create_labels(4, 1, master, buttons, 470, 300 - 20)

    buttons = [('ALPHA', 'black', 'lightgrey')]
    create_buttons(1, 1, master, c1, buttons, 600, 250, 50, 30)
    buttons = [('C2C', 'black', 'lightgrey')]
    create_buttons(1, 1, master, c1, buttons, 600, 300, 50, 30)
    buttons = [('CFC', 'black', 'lightgrey')]
    create_buttons(1, 1, master, c1, buttons, 600, 350, 50, 30)


    # master.bind("1",lambda c1 :one_pressed(c1))
    # master.bind("<ENTER>",lambda : one_pressed(c1))
    master.bind("<Key>", one_pressed)
    master.mainloop()
    return


main()
