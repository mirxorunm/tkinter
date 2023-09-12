import tkinter as tk


# Функция для обработки нажатия кнопок
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем поле для ввода
entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Определяем кнопки
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+",
    "="
]

# Создаем и размещаем кнопки на окне
row = 1
col = 0

for text in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20))
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Запускаем главный цикл
root.mainloop()
