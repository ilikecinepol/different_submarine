from tkinter import * 
import random 
import time
import cmath, math



tk = Tk()        
tk.title("Моделирование подводной лодки")        
tk.resizable(0, 0)        
tk.wm_attributes("-topmost", 1)        
canvas = Canvas(tk, width=1200, height=750, highlightthickness=0)        
canvas.pack()        
tk.update()        
canvas_height = 500        
canvas_width = 50
bg = PhotoImage(file="pictures/background.gif")
w = bg.width() 
h = bg.height()

for x in range(0, 5):    
    for y in range(0, 5):        
        canvas.create_image(x * w, y * h, image=bg, anchor='nw')
        sprites = [] 
        running = True
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
        
        self.div = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11, self.d12,
                    self.d13, self.d14, self.d15, self.d16, self.d17, self.d18, self.d19, self.d20, self.d21, self.d22, self.d23, self.d24, self.d25]

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
        
        self.canvas.itemconfig(self.id, image = self.sub)
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
                self.canvas.itemconfig(self.id, image = self.div[m])
                self.canvas.move(self.id, 0, -1)
    
                        
                system()
          

            
        
    def diving(self):
        self.canvas.itemconfig(self.id, image = self.sub)
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
                                       
                self.canvas.itemconfig(self.id, image = self.div[m])
                self.canvas.move(self.id, 0, 1)              
                system()
                
                    
            self.draw()
        elif self.pos[1] > 500.0:
            self.canvas.move(self.id, 0, 0)
            self.draw()
            system()
       



    
s = Submarine()
btn1 = Button(tk, text="Всплытие!", command = s.emersion).place(x=75, y=20)
btn2 = Button(tk, text="Погружение!", command = s.diving).place(x=75, y=100)
#btn1.pack()
#btn2.pack()




mainloop()








##canvas.bind_all('<KeyPress-Return>', movetriangle)
