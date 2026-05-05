import tkinter as tk
import random

def random_color():
    return f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'

def show_number(num):
    lbl.config(text=str(num), fg=random_color(), font=('Arial', random.randint(30, 80)))

def draw_coordinate():
    canvas.create_line(50, 250, 450, 250, arrow=tk.LAST)
    canvas.create_line(250, 50, 250, 450, arrow=tk.LAST)
    canvas.create_text(460, 250, text="X")
    canvas.create_text(250, 40, text="Y")

root = tk.Tk()
root.title("数字+坐标系")
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()
draw_coordinate()

lbl = tk.Label(root, text="", font=('Arial', 50))
lbl.pack(pady=10)

for i in range(1, 11):
    btn = tk.Button(root, text=str(i), width=4, command=lambda n=i: show_number(n))
    btn.pack(side=tk.LEFT, padx=3)

root.mainloop()