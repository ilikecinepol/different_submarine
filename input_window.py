from tkinter import *

root = Tk()

table1 = Frame(root)

Label(table1, text="Наименование грузов") \
    .grid(row=0, column=0, rowspan=2, pady=10, padx=10)
Label(table1, text="Нормальная нагрузка") \
    .grid(row=0, column=1, columnspan=2)
Label(table1, text="Дифференовка за (дата), тс") \
    .grid(row=0, column=3)
Label(table1, text="Фактическая нагрузка, тс") \
    .grid(row=0, column=4)
Label(table1, text="Наименование нагрузки") \
    .grid(row=0, column=5, columnspan=2)
Label(table1, text="p, тс") \
    .grid(row=1, column=1)
Label(table1, text="х, м") \
    .grid(row=1, column=2)
Label(table1, text="delta p, тс") \
    .grid(row=1, column=5)
Label(table1, text="delta M, тс м") \
    .grid(row=1, column=6)
Label(table1, text="") \
    .grid(row=2, column=1, columnspan=7)

Label(table1, text="Запасные торпеды") \
    .grid(row=3, column=0)
Entry(table1, width=10) \
    .grid(row=3, column=1)
Entry(table1, width=10) \
    .grid(row=3, column=2)
Entry(table1, width=10) \
    .grid(row=3, column=3)
Entry(table1, width=10) \
    .grid(row=3, column=4)
Entry(table1, width=10) \
    .grid(row=3, column=5)
Entry(table1, width=10) \
    .grid(row=3, column=6)

Label(table1, text="Торпедозаместительные цистерны №1 и 2") \
    .grid(row=4, column=0)
Entry(table1, width=10) \
    .grid(row=4, column=1)
Entry(table1, width=10) \
    .grid(row=4, column=2)
Entry(table1, width=10) \
    .grid(row=4, column=3)
Entry(table1, width=10) \
    .grid(row=4, column=4)
Entry(table1, width=10) \
    .grid(row=4, column=5)
Entry(table1, width=10) \
    .grid(row=4, column=6)

Label(table1, text="Масло в цистерне судового запаса масла №2") \
    .grid(row=5, column=0)
Entry(table1, width=10) \
    .grid(row=5, column=1)
Entry(table1, width=10) \
    .grid(row=5, column=2)
Entry(table1, width=10) \
    .grid(row=5, column=3)
Entry(table1, width=10) \
    .grid(row=5, column=4)
Entry(table1, width=10) \
    .grid(row=5, column=5)
Entry(table1, width=10) \
    .grid(row=5, column=6)

Label(table1, text="Масло в цистерне цирукляционного масла №2") \
    .grid(row=6, column=0)
Entry(table1, width=10) \
    .grid(row=6, column=1)
Entry(table1, width=10) \
    .grid(row=6, column=2)
Entry(table1, width=10) \
    .grid(row=6, column=3)
Entry(table1, width=10) \
    .grid(row=6, column=4)
Entry(table1, width=10) \
    .grid(row=6, column=5)
Entry(table1, width=10) \
    .grid(row=6, column=6)

Label(table1, text="Масло в цистернах грязного масла №1 и 2") \
    .grid(row=7, column=0)
Entry(table1, width=10) \
    .grid(row=7, column=1)
Entry(table1, width=10) \
    .grid(row=7, column=2)
Entry(table1, width=10) \
    .grid(row=7, column=3)
Entry(table1, width=10) \
    .grid(row=7, column=4)
Entry(table1, width=10) \
    .grid(row=7, column=5)
Entry(table1, width=10) \
    .grid(row=7, column=6)

Label(table1, text="Питательная вода в цистерне №1") \
    .grid(row=8, column=0)
Entry(table1, width=10) \
    .grid(row=8, column=1)
Entry(table1, width=10) \
    .grid(row=8, column=2)
Entry(table1, width=10) \
    .grid(row=8, column=3)
Entry(table1, width=10) \
    .grid(row=8, column=4)
Entry(table1, width=10) \
    .grid(row=8, column=5)
Entry(table1, width=10) \
    .grid(row=8, column=6)

Label(table1, text="Провизия в цистерне №1") \
    .grid(row=9, column=0)
Entry(table1, width=10) \
    .grid(row=9, column=1)
Entry(table1, width=10) \
    .grid(row=9, column=2)
Entry(table1, width=10) \
    .grid(row=9, column=3)
Entry(table1, width=10) \
    .grid(row=9, column=4)
Entry(table1, width=10) \
    .grid(row=9, column=5)
Entry(table1, width=10) \
    .grid(row=9, column=6)

Label(table1, text="Провизия в цистерне №5") \
    .grid(row=10, column=0)
Entry(table1, width=10) \
    .grid(row=10, column=1)
Entry(table1, width=10) \
    .grid(row=10, column=2)
Entry(table1, width=10) \
    .grid(row=10, column=3)
Entry(table1, width=10) \
    .grid(row=10, column=4)
Entry(table1, width=10) \
    .grid(row=10, column=5)
Entry(table1, width=10) \
    .grid(row=10, column=6)

Label(table1, text="Провизия в цистерне №4") \
    .grid(row=11, column=0)
Entry(table1, width=10) \
    .grid(row=11, column=1)
Entry(table1, width=10) \
    .grid(row=11, column=2)
Entry(table1, width=10) \
    .grid(row=11, column=3)
Entry(table1, width=10) \
    .grid(row=11, column=4)
Entry(table1, width=10) \
    .grid(row=11, column=5)
Entry(table1, width=10) \
    .grid(row=11, column=6)

Label(table1, text="Итого переменных грузов") \
    .grid(row=12, column=0)

table1.pack()
if __name__ == "__main__":
    print(table1)

root.mainloop()
