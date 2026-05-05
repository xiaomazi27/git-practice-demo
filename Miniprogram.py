import tkinter as tk
import random

def random_color():
    return f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'

def show_number(num):
    lbl.config(text=str(num), fg=random_color(), font=('Arial', random.randint(30, 80)))

root = tk.Tk()
root.title("数字点击窗口")
root.geometry("500x400")

lbl = tk.Label(root, text="", font=('Arial', 50))
lbl.pack(pady=30)

for i in range(1, 11):
    btn = tk.Button(root, text=str(i), width=4, command=lambda n=i: show_number(n))
    btn.pack(side=tk.LEFT, padx=3)

root.mainloop()