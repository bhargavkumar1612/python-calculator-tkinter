#calculator
def formatinput(s):
    d = [' ', ',']
    op = ['+','-','*','/','(',')', '^', 'i']
    f = ['']
    if '++' in s or '--' in s or '+*' in s or '*+' in s or '-*' in s or '*-' in s or '/*' in s or '*/' in s or '+/' in s or '/+' in s or '-/' in s or '/-' in s:
        return 'quit'
    while "+-" in s or '-+' in s or '**' in s or '//' in s:
        if "+-"in s:
            s = s.replace('+-','-')
        elif '-+' in s:
            s = s.replace('-+','-')
        elif '**' in s:
            s = s.replace('**', '^')
        elif '//' in s:
            s = s.replace('//', 'i')
    for _ in s:
        if _ in d:
            pass
        elif _.isdigit() or _ == '.' or (_ == "" and inp.index(_)==0):
            f[-1]+= _
        elif _ in op:
            try:
                f[-1] = float(f[-1])
            except:
                pass
            f.append(_)
            f.append("")
        elif not _.isdigit() and not _ in (d+op):
            print('>>symbols other than numbers, operaters and braces are entered')
            break
    try:
        f[-1] = float(f[-1])
    except:
        pass
    while "" in f:
        f.remove("")  
    return f
def power(f):
    while '^' in f:
        for i in range(len(f)):
            if f[i] == '^':
                f[i] = f[i-1]**f[i+1]
                del f[i-1]
                del f[i]
                break
    return f
def multdiv(finp):
    while '*' in finp or '/' in finp or 'i' in finp:
        for i in range(len(finp)):
            if finp[i] == '/':
                #print(finp[i-1], finp[i], finp[i+1])
                finp[i] = finp[i-1]/finp[i+1]
                del finp[i-1]
                del finp[i]
                break
            elif finp[i] == 'i':
                #print(finp[i-1], finp[i], finp[i+1])
                finp[i] = finp[i-1]//finp[i+1]
                del finp[i-1]
                del finp[i]
                break
            elif finp[i] == '*':
                #print(finp[i-1], finp[i], finp[i+1])
                finp[i] = finp[i-1]*finp[i+1]
                del finp[i-1]
                del finp[i]
                break
            elif finp[i] == '':
                del finp[i]
                break
    return finp

def addsub(finp):
    if type(finp[0]) == float:
        while len(finp) > 1:
            if finp[1] == '+':
                finp[0] = finp[0]+finp[2]
                del finp[1]
                del finp[1]
            elif finp[1] == "-":
                finp[0] = finp[0]-finp[2]
                del finp[1]
                del finp[1]
    else:
        if finp[0] == '+':
            del finp[0]
            while len(finp) > 1:
                if finp[1] == '+':
                    finp[0] = finp[0]+finp[2]
                    del finp[1]
                    del finp[1]
                elif finp[1] == "-":
                    finp[0] = finp[0]-finp[2]
                    del finp[1]
                    del finp[1]
        elif finp[0] == '-':
            del finp[0]
            finp[0]= -finp[0]
            while len(finp) > 1:
                if finp[1] == '+':
                    finp[0] = finp[0]+finp[2]
                    del finp[1]
                    del finp[1]
                elif finp[1] == "-":
                    finp[0] = finp[0]-finp[2]
                    del finp[1]
                    del finp[1]
    return finp[0]
def calc(s):
    s = formatinput(s)
    if s=='quit':
        return
    while '(' in s and ')' in s:
        fo = 0
        fc = 0
        for i in range(len(s)):
            if s[i] == '(':
                fo = i
            elif s[i] == ')':
                fc = i
                s[fo] = addsub(multdiv(power(s[fo+1:fc])))
                del s[fo+1:fc+1]
                break
    out = addsub(multdiv(power(s)))
    out = int(out) if int(out) == out else out
    return out


from tkinter import *
expression = ''
ans = ""
def press(n):
    global expression
    expression += str(n)
    equation.set(expression)

def equalpress():
    try:
        global expression, ans
        total = str(calc(expression))
        equation.set(expression +' = ' + total)
        ans = total
        expression = ''
    except:
        equation.set('error')
        expression = ""
def bs():
    try:
        global expression
        expression = expression[:-1]
        equation.set(expression)
    except:
        clear()
def clear(): 
    global expression 
    expression = "" 
    equation.set("")

gui = Tk()
gui.configure(background = 'Blue')
gui.title('CALCULATOR')
gui.geometry('400x200')
equation = StringVar()
expression_field = Entry(gui, textvariable = equation)
expression_field.grid(columnspan=10, ipadx=150)
equation.set('enter your expression')
#row2 clear, 0, and backspace buttons 
bclear = Button(gui, text = 'CLEAR ALL', fg = 'black', bg = 'pink',
           command = lambda: clear(), height = 1, width = 7)
bclear.grid(row = 2, column = 0)
bbs = Button(gui, text = 'Backspace', fg = 'black', bg = 'pink',
           command = lambda: bs(), height = 1, width = 7)
bbs.grid(row = 2, column = 4)
bans = Button(gui, text = 'Ans', fg = 'black', bg = 'green',
           command = lambda: press(ans), height = 1, width = 7)
bans.grid(row = 2, column = 3)

#row3 has 1,2,3,+,- buttons 
b1 = Button(gui, text = '1', fg = 'black', bg = 'white',
           command = lambda: press(1), height = 1, width = 7)
b1.grid(row = 3, column = 0)
b2 = Button(gui, text = '2', fg = 'black', bg = 'white',
           command = lambda: press(2), height = 1, width = 7)
b2.grid(row = 3, column = 1)
b3 = Button(gui, text = '3', fg = 'black', bg = 'white',
           command = lambda: press(3), height = 1, width = 7)
b3.grid(row = 3, column = 2)
bplus = Button(gui, text = '+', fg = 'black', bg = 'yellow',
           command = lambda: press('+'), height = 1, width = 7)
bplus.grid(row = 3, column = 3)
bminus = Button(gui, text = '-', fg = 'black', bg = 'yellow',
           command = lambda: press('-'), height = 1, width = 7)
bminus.grid(row = 3, column = 4)
#row4 has 4,5,6,x,÷ buttons
b4 = Button(gui, text = '4', fg = 'black', bg = 'white',
           command = lambda: press(4), height = 1, width = 7)
b4.grid(row = 4, column = 0)
b5 = Button(gui, text = '5', fg = 'black', bg = 'white',
           command = lambda: press(5), height = 1, width = 7)
b5.grid(row = 4, column = 1)
b6 = Button(gui, text = '6', fg = 'black', bg = 'white',
           command = lambda: press(6), height = 1, width = 7)
b6.grid(row = 4, column = 2)
bmult = Button(gui, text = 'x', fg = 'black', bg = 'yellow',
           command = lambda: press('*'), height = 1, width = 7)
bmult.grid(row = 4, column = 3)
bdiv = Button(gui, text = '÷', fg = 'black', bg = 'yellow',
           command = lambda: press('/'), height = 1, width = 7)
bdiv.grid(row = 4, column = 4)
#row5 has 7,8,9,^,intdiv
b7 = Button(gui, text = '7', fg = 'black', bg = 'white',
           command = lambda: press(7), height = 1, width = 7)
b7.grid(row = 5, column = 0)
b8 = Button(gui, text = '8', fg = 'black', bg = 'white',
           command = lambda: press(8), height = 1, width = 7)
b8.grid(row = 5, column = 1)
b9 = Button(gui, text = '9', fg = 'black', bg = 'white',
           command = lambda: press(9), height = 1, width = 7)
b9.grid(row = 5, column = 2)
bpow = Button(gui, text = '^', fg = 'black', bg = 'yellow',
           command = lambda: press('**'), height = 1, width = 7)
bpow.grid(row = 5, column = 3)
bintdiv = Button(gui, text = 'intdiv', fg = 'black', bg = 'yellow',
           command = lambda: press('//'), height = 1, width = 7)
bintdiv.grid(row = 5, column = 4)
#row6 has 0,.,(,),=
b0 = Button(gui, text = '0', fg = 'black', bg = 'white',
           command = lambda: press(0), height = 1, width = 7)
b0.grid(row = 6, column = 0)
bdot = Button(gui, text = '.', fg = 'black', bg = 'white',
           command = lambda: press('.'), height = 1, width = 7)
bdot.grid(row = 6, column = 1)
bopenbracket = Button(gui, text = '(', fg = 'black', bg = 'white',
           command = lambda: press('('), height = 1, width = 7)
bopenbracket.grid(row = 6, column = 2)
bclosedbracket = Button(gui, text = ')', fg = 'black', bg = 'white',
           command = lambda: press(')'), height = 1, width = 7)
bclosedbracket.grid(row = 6, column = 3)
bequal = Button(gui, text = '=', fg = 'black', bg = 'green',
           command = lambda: equalpress(), height = 1, width = 7)
bequal.grid(row = 6, column = 4)


gui.mainloop()
