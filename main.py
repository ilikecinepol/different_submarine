from tkinter import *
from tkinter import ttk, messagebox
import calculation_of_dif as calc
import time


tk = Tk()
tk.title("Моделирование подводной лодки")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 0)
canvas = Canvas(tk, width=1200, height=750, highlightthickness=0)
canvas.pack()
# tk.update()
canvas_height = 500
canvas_width = 50
bg = PhotoImage(file="pictures/background.gif")
w = bg.width()
h = bg.height()

Spare_torpedoes = [0, 0, 0]
cistern12 = [0, 0, 0]
oil2_1 = [0, 0, 0]
oil2_2 = [0, 0, 0]
oil1_2 = [0, 0, 0]
water1 = [0, 0, 0]
food = [0, 0, 0]
water4 = [0, 0, 0]
summ = [0, 0]


for x in range(0, 5):
    for y in range(0, 5):
        canvas.create_image(x * w, y * h, image=bg, anchor='nw')
        sprites = []
        running = True


def input_window():
    input_window = Tk()
    input_window.geometry("1300x550")
    input_window.title("Данные для рассчёта")
    input_window.wm_attributes("-topmost", 1)
    input_window.wm_attributes('-alpha', 0.5)
    input_canvas = Canvas(input_window, width=800, height=750, highlightthickness=0)


    frame_a = Frame(input_window)   #Для строки заголовков таблицы
    frame_b = Frame(input_window)   #Заголовок окна
    frame_c = Frame(frame_a, width = 20)        #Подпункты нормальной нагрузки
    frame_d = Frame(frame_a)
    frame_n = Frame(input_window)   #Для итогов
    title1 = Label(master = frame_b, text='Переменные грузы: ',  anchor='n')
    lab1 = Label(master = frame_a, width = 50, text="Наименование грузов",  anchor='center')
    lab2 = Label(master = frame_c, text="Нормальная нагрузка",  anchor='center')
    lab21 = Label(master = frame_c, width = 10, text="p, тс",  anchor='center')
    lab22 = Label(master = frame_c, width = 10, text="х, м",  anchor='center')
    #lab3 = Label(master = frame_a, text="Дифференовка за (дата), тс",  anchor='center')
    lab4 = Label(master = frame_a, text="Фактическая нагрузка, тс",  anchor='center')
    lab5 = Label(master = frame_d, text="Изменение нагрузки", anchor='center')
    lab51 = Label(master = frame_d, text="delta p, тс", anchor='center')
    lab52 = Label(master = frame_d, text="delta M, тс м", anchor='center')

    main_label = Label(master = input_window, text='Всего грузов: ', anchor='w')
 #Первая строка
    def calc():
        lab6_1 = Label(str_1, text=val3 - val1)
        lab6.pack(side=LEFT, **opts)
        input_window.update()

    str_1 = Frame(input_window)
    lab6 = Label(master = str_1, width=50, text="Запасные торпеды", anchor='center')
    val1 = IntVar()
    val2 = IntVar()
    val3  = IntVar()

    ent11 = Entry(str_1, width=10, textvariable = val1)
    ent12 = Entry(str_1, width=10,textvariable=val2)
    ent13 = Entry(str_1, width=25, textvariable=val3)

    val1 = int(val1.get())
    val2 = int(val2.get())
    val3 = int(val3.get())

    lab6_1 = Label(str_1, text=val3 - val1)
    #lab6_1 = Label(str_1, text=int(val1) - int(val2))
    btn_test = Button(str_1, text = 'Произвести расчёты', command =calc)


    opts = {'ipadx':10, 'ipady': 10, "fill": BOTH}

    title1.pack(side=TOP, **opts)
    lab1.pack(side=LEFT, **opts)

    lab2.pack(side=TOP, **opts)
    lab21.pack(side=LEFT, **opts)
    lab22.pack(side=LEFT, **opts)

    frame_c.pack(side=LEFT, **opts)

    #lab3.pack(side=LEFT, **opts)
    lab4.pack(side=LEFT, **opts)
    lab5.pack(side=TOP, **opts)
    lab51.pack(side=LEFT, **opts)
    lab52.pack(side=LEFT, **opts)
    frame_d.pack(side=LEFT, **opts)
#Первая строка
    lab6.pack(side=LEFT, **opts)
    ent11.pack(side=LEFT, **opts)
    ent12.pack(side=LEFT, **opts)
    ent13.pack(side=LEFT, **opts)
    lab6_1.pack(side=LEFT, **opts)
    btn_test.pack(side=LEFT, **opts)

    frame_b.pack(side=TOP, **opts)
    frame_a.pack(side=TOP, **opts)
    str_1.pack(side=TOP, **opts)
    frame_n.pack(side=TOP, **opts)





    #lab21.pack(side=LEFT, **opts)
    #lab22.pack(side=LEFT, **opts)

    #main_label.pack(side=TOP, **opts)
    input_canvas.pack()
    input_window.update_idletasks()
    input_window.update()




btn3 = Button(tk, text="Ввод данных для рассчёта", command=input_window).place(x=500, y=700)

# entry.pack()

def system():
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)






class Submarine:
    def __init__(self):
        self.canvas = canvas
        self.sub = PhotoImage(file="pictures/lodka.gif")
        self.d1 = PhotoImage(file="pictures/d1.gif")
        self.d2 = PhotoImage(file="pictures/d2.gif")
        self.d3 = PhotoImage(file="pictures/d3.gif")
        self.d4 = PhotoImage(file="pictures/d4.gif")
        self.d5 = PhotoImage(file="pictures/d5.gif")
        self.d6 = PhotoImage(file="pictures/d6.gif")
        self.d7 = PhotoImage(file="pictures/d7.gif")
        self.d8 = PhotoImage(file="pictures/d8.gif")
        self.d9 = PhotoImage(file="pictures/d9.gif")
        self.d10 = PhotoImage(file="pictures/d10.gif")
        self.d11 = PhotoImage(file="pictures/d11.gif")
        self.d12 = PhotoImage(file="pictures/d12.gif")
        self.d13 = PhotoImage(file="pictures/d13.gif")
        self.d14 = PhotoImage(file="pictures/d14.gif")
        self.d15 = PhotoImage(file="pictures/d15.gif")
        self.d16 = PhotoImage(file="pictures/d16.gif")
        self.d17 = PhotoImage(file="pictures/d17.gif")
        self.d18 = PhotoImage(file="pictures/d18.gif")
        self.d19 = PhotoImage(file="pictures/d19.gif")
        self.d20 = PhotoImage(file="pictures/d20.gif")
        self.d21 = PhotoImage(file="pictures/d21.gif")
        self.d22 = PhotoImage(file="pictures/d22.gif")
        self.d23 = PhotoImage(file="pictures/d23.gif")
        self.d24 = PhotoImage(file="pictures/d24.gif")
        self.d25 = PhotoImage(file="pictures/d25.gif")

        self.div = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11,
                    self.d12,
                    self.d13, self.d14, self.d15, self.d16, self.d17, self.d18, self.d19, self.d20, self.d21, self.d22,
                    self.d23, self.d24, self.d25]

        self.start = [600, 200]
        self.id = canvas.create_image(self.start[0], self.start[1], image=self.div[1])
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.pos = self.canvas.coords(self.id)
        self.xy = [(300, 115), (900, 115), (900, 386), (300, 386)]

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[1] >= 500 or pos[1] <= 250:
            self.canvas.move(self.id, 0, 0)

    def emersion(self):

        self.canvas.itemconfig(self.id, image=self.sub)
        pos = self.canvas.coords(self.id)
        if pos[1] > 250.0:
            deep = 250
            print(deep)
            m = 25
            while pos[1] >= self.start[1]:
                pos = self.canvas.coords(self.id)
                currentDeep = int(pos[1]) - 250
                j = int(currentDeep % 10)

                if j == 0:
                    m = m - 1
                self.canvas.itemconfig(self.id, image=self.div[m])
                self.canvas.move(self.id, 0, -1)

                system()

    def diving(self):
        self.canvas.itemconfig(self.id, image=self.sub)
        pos = self.canvas.coords(self.id)
        if self.pos[1] < 500.0:
            deep = 250
            m = 0
            while pos[1] <= 500:
                pos = self.canvas.coords(self.id)
                currentDeep = int(pos[1]) - self.start[1]
                j = int(currentDeep % 10)

                if j == 0:
                    m += 1

                self.canvas.itemconfig(self.id, image=self.div[m])
                self.canvas.move(self.id, 0, 1)
                system()

            self.draw()
        elif self.pos[1] > 500.0:
            self.canvas.move(self.id, 0, 0)
            self.draw()
            system()


s = Submarine()
btn1 = Button(tk, text="Всплытие!", command=s.emersion, width=15).place(x=1050, y=650)
btn2 = Button(tk, text="Погружение!", command=s.diving, width=15).place(x=1050, y=700)

# btn2 = Button(tk, text="Ввести параметры для расчёта!", command=new_window()).place(x=75, y=100)
# btn2 = Button(tk, text="Погружение!", command=s.diving).place(x=75, y=100)
# btn1.pack()
# btn2.pack()

mainloop()
