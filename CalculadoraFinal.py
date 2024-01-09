from tkinter import *
from tkinter import ttk
import math

color1 = '#a141d1' #purple
color2 = '#169ec4' #blue
color3 = '#e88ec8' #pink
color4 = '#e8bf8e' #orange
color5 = '#f5f0eb' #white

root = Tk()
root.title("Calculadora Simples")
root.geometry("570x700")
root.resizable(False,False)
root.configure(bg=color5)

#Creating frames

frame_tela = Frame(root, width=300, height=56, bg=color5)
frame_body = Frame(root, width=300, height=340)

#Config frame_tela

label_result = Label(root, width=25, height=2, text="", font=("arial", 30,), justify="right")
label_result.pack()

#functions

equation = ""
texto = StringVar()

def enter_values(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    global texto
    operations = ['math.factorial', 'math.pi']
    for i in operations:
        if i == 'math.factorial':
            equation = equation.replace("!", i)
        if i == 'math.pi':
            equation = equation.replace("π", i)
    texto = str(equation)
    if 'x' in texto:
        texto = texto.replace("x", "*")
    elif '÷' in texto:
        texto = texto.replace("÷", "/")
    elif '%' in texto:
        texto = texto.replace("%", "/100")
    elif '√' in texto:
        texto = texto.replace("√", "**(1/2)")
    elif '^' in texto:
        texto = texto.replace("^", "**")
    elif ',' in texto:
        texto = texto.replace(",", ".")

    resultado = float(eval(texto))
    label_result.config(text=resultado)
    equation = ''

def del_last_value():
    global equation
    if len(equation) == 1:
        equation = ""
    else:
        equation = equation[:-1]
    label_result.config(text=equation)

#Buttons

Button(root, text="√", width=5, height=0,font=("arial", 30,"bold"), bd=0,fg=color5,bg=color1,command=lambda: enter_values("√")).place(x=10, y=100)
Button(root, text="π", width=5, height=0,font=("arial", 30,"bold"), bd=0,fg=color5,bg=color1,command=lambda: enter_values("π")).place(x=150, y=100)
Button(root, text="x^", width=5, height=0,font=("arial", 30,"bold"), bd=0,fg=color5,bg=color1,command=lambda: enter_values("^")).place(x=290, y=100)
Button(root, text="!", width=5, height=0,font=("arial", 30,"bold"), bd=0,fg=color5,bg=color1,command=lambda: enter_values("!")).place(x=430, y=100)

Button(root, text="AC", width=10, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color4, command=lambda: clear()).place(x=10, y=200)
Button(root, text="%", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: enter_values("%")).place(x=290, y=200)
Button(root, text="÷", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: enter_values("÷")).place(x=430, y=200)

Button(root, text="7", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("7")).place(x=10, y=300)
Button(root, text="8", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("8")).place(x=150, y=300)
Button(root, text="9", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("9")).place(x=290, y=300)
Button(root, text="x", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: enter_values("x")).place(x=430, y=300)

Button(root, text="4", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("4")).place(x=10, y=400)
Button(root, text="5", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("5")).place(x=150, y=400)
Button(root, text="6", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("6")).place(x=290, y=400)
Button(root, text="-", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: enter_values("-")).place(x=430, y=400)

Button(root, text="1", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("1")).place(x=10, y=500)
Button(root, text="2", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("2")).place(x=150, y=500)
Button(root, text="3", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values("3")).place(x=290, y=500)
Button(root, text="+", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: enter_values("+")).place(x=430, y=500)

Button(root, text=",", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: enter_values(",")).place(x=10, y=600)
Button(root, text="0", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda:enter_values("0")).place(x=150, y=600)
Button(root, text="←", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color3,command=lambda: del_last_value()).place(x=290, y=600)
Button(root, text="=", width=5, height=1,font=("arial", 30,"bold"), bd=1,fg=color5,bg=color2,command=lambda: calculate()).place(x=430, y=600)


root.mainloop()