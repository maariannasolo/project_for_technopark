#импорт библиотек
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
from numpy import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import warnings
from tkinter.ttk import Radiobutton 


#создание окна
root = Tk() 
root.title("Calculator")
root.geometry('500x200') 

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
# создаем фреймы
frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Калькулятор")
notebook.add(frame2, text="Выражение для построения графиков")
notebook.add(frame3, text="Физика")

#список кнопок
bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]

#создание кнопок
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(frame1, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

#содание окна ввода
calc_entry = Entry(frame1, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

#логика калькулятора
def calc(key):
    global memory
    if key == "=":

#исключение написания слов
        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Первый символ-не цифра!")

#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror('Ошибка', 'Пример некорректен')

#очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)

#изменение знака на противоположный
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

#число Пи
    elif key == "π":
        calc_entry.insert(END, math.pi)

#закрытие окна
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit

#возведение в степень
    elif key == "xⁿ":
        calc_entry.insert(END, "**")

# синус
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))

# косинус
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

# скобки
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

# факториал
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

# квадратный корень
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

# окончание ввода
    else:
            if "=" in calc_entry.get():
                calc_entry.delete(0, END)
            calc_entry.insert(END, key)  


def evaluate(event):
    try:
        mystr = entry.get()
        exec('f = lambda x:' + mystr, globals())
        a = float(strA.get())
        b = float(strB.get())
        X = linspace(a, b, 300)
        Y = [f(x) for x in X]
        ax.clear()  # очистить графическую область
        ax.plot(X, Y, linewidth=2)
        ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        canvasAgg.draw()  # перерисовать "составной" холст
        return
    except:  # реакция на любую ошибку
        showerror('Ошибка', "Неверное выражение или интервал [a,b].")


#графики


def evaluate2(event):  # чтобы кнопка отжималась при ошибке
    root.after(100, evaluate, event)


root = Tk()
root.wm_title("График функции")
warnings.filterwarnings("error")
frameUp = Frame(frame2, relief=SUNKEN, height=64)
frameUp.pack(side=TOP, fill=X)
Label(frameUp, text="Выражение: ").place(x=20, y=4, width=100, height=25)
Label(frameUp, text="Начало интервала a:").place(x=250, y=4, width=140, height=25)
Label(frameUp, text="Конец интервала b:").place(x=370, y=4, width=140, height=25)
entry = Entry(frameUp, relief=RIDGE, borderwidth=4)
entry.bind("<Return>", evaluate)
entry.place(x=6, y=30, width=250, height=25)
strA = StringVar()
strA.set(0)
entryA = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strA)
entryA.place(x=280, y=30, width=80, height=25)
entryA.bind("<Return>", evaluate)
strB = StringVar()
strB.set(1)
entryB = Entry(frameUp, relief=RIDGE, borderwidth=4, textvariable=strB)
entryB.place(x=400, y=30, width=80, height=25)
entryB.bind("<Return>", evaluate)
fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(111)
canvasAgg = FigureCanvasTkAgg(fig, master=root)
canvasAgg.draw()
canvas = canvasAgg.get_tk_widget()
canvas.pack(fill=BOTH, expand=1)
btn = Button(root, text='График')
btn.bind("<Button-1>", evaluate2)
btn.pack(ipady=2, pady=4, padx=10)
root.bind('<Control-z>', lambda event: root.destroy())

lbl40=Label()
#физика
def clicked(): 
    messagebox.showinfo("название", "Справка о приложении:\какой-то текст") 
    messagebox.showerror("название", "текст") 
    messagebox.showwarning("название", "текст") 
    lbl40.configure(text=selected.get()) 

def cspec():
    lbl1 = Label(frame3, text='Q*m/Δt')
    lbl1.grid(row=1, column=2)

def Qspec():
    lbl2 = Label(frame3, text='c*m*Δt')
    lbl2.grid(row=1, column=2)

def mspec():
    lbl3 = Label(frame3, text='Q/(Δt*c)')
    lbl3.grid(row=1, column=2)

def tspec():
    lbl4 = Label(frame3, text='Q/(m*c)')
    lbl4.grid(row=1, column=2)


def specific_heat():
    lbl = Label(frame3, text='Выберите нужную величину:')
    lbl.grid(row=0, column=1)
    btn19=Button(frame3, text='c', command=cspec).grid(row=0, column=2)
    btn20=Button(frame3, text='Q', command=Qspec).grid(row=0, column=3)
    btn21=Button(frame3, text='m', command=mspec).grid(row=0, column=4)
    btn22=Button(frame3, text='Δt', command=tspec).grid(row=0, column=5)



def ccapac():
    lbl5 = Label(frame3, text='C/m')
    lbl5.grid(row=3, column=6)

def mcapac():
    lbl6 = Label(frame3, text='C/c')
    lbl6.grid(row=3, column=6)

def bigccapac():
    lbl7 = Label(frame3, text='m*c')
    lbl7.grid(row=3, column=6)



def heat_capacity():
    lbl8 = Label(frame3, text='Выберите нужную величину:')
    lbl8.grid(row=2, column=1)
    btn23=Button(frame3, text='c', command=ccapac).grid(row=2, column=4)
    btn24=Button(frame3, text='С', command=bigccapac).grid(row=2, column=5)
    btn25=Button(frame3, text='m', command=mcapac).grid(row=2, column=6)

def Qmou():
    lbl12 = Label(frame3, text='mq')
    lbl12.grid(row=5, column=6)

def qmou():
    lbl11= Label(frame3, text='Q/m')
    lbl11.grid(row=5, column=6)

def mau():
    lbl10= Label(frame3, text='Q/q')
    lbl10.grid(row=5, column=6)



def amount_of_heat ():
    lbl9 = Label(frame3, text='Выберите нужную величину:')
    lbl9.grid(row=2, column=1)
    btn23=Button(frame3, text='Q', command=Qmou).grid(row=4, column=4)
    btn24=Button(frame3, text='q', command=qmou).grid(row=4, column=5)
    btn25=Button(frame3, text='m', command=mau).grid(row=4, column=6)


btn15 = Button(frame3, text='Удельная теплоемкость вещества',  command=specific_heat)
btn16 = Button(frame3, text='Теплоемкость тела',  command=heat_capacity)
btn17 = Button(frame3, text='Количество теплоты при сгорании топлива',  command=amount_of_heat)
btn15.grid(row=0, column = 0)
btn16.grid(row=1, column = 0)
btn17.grid(row=2, column = 0)


root.mainloop()