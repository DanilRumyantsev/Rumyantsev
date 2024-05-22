# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk
import tkinter.messagebox as messagebox

def Myfunction():
    try:
        a = int(entry_a.get())
        if a < 0:
            raise ValueError("Введите положительное число")
        b = entry_b.get()

        if not b:
            raise ValueError("Поле пустое")

        c = b * a

        result_text.delete("1.0", "end")
        result_text.insert("1.0", c)

    except ValueError as e:
        messagebox.showerror("Ошибка", e)

root = tk.Tk()
root.title("Повторение символов")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_a_label = tk.Label(frame, text="Введите число символов для строки:")
entry_a_label.grid(row=0, column=0, padx=(0, 20), pady=(20, 0))

entry_a = tk.Entry(frame)
entry_a.grid(row=0, column=1)

entry_b_label = tk.Label(frame, text="Введите символы, которые вы хотите повторить:")
entry_b_label.grid(row=1, column=0, padx=(0, 20), pady=(10, 0))

entry_b = tk.Entry(frame)
entry_b.grid(row=1, column=1)

button = tk.Button(frame, text="Выполнить", command=Myfunction)
button.grid(row=2, columnspan=2, pady=(20, 20))

result_label = tk.Label(frame, text="Результат:")
result_label.grid(row=3, column=0)

result_text = tk.Text(frame, width=40, height=5, borderwidth=2, relief="solid")
result_text.grid(row=3, column=1)

root.mainloop()
