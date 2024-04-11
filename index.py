from tkinter import *

# Ініціалізація додатку
app = Tk()

# Налаштування додатку
app.title("Конвертер валют")
app.geometry("500x500")
app.maxsize(500, 500)
app.config(bg="#00B894", padx=10, pady=10)
app.resizable(False, False)


entry_uah = Entry(app, font=("Segoe UI", 16, "bold"), bg="white", fg="grey", justify="center")
entry_usd = Entry(app, font=("Segoe UI", 16, "bold"), bg="white", fg="grey", justify="center")


def transform_uah_to_usd():
    try:
        uah_value = float(entry_uah.get())
        usd_value = uah_value * 0.0254
        rounded_value_usd = round(usd_value, 2)
        entry_usd.delete(0, END)  # Видаляємо попереднє значення
        entry_usd.insert(0, f"${rounded_value_usd}")  # Вставляємо нове значення в поле вводу для доларів
    except ValueError:
        pass

def transform_usd_to_uah():
    try:
        usd_value = float(entry_usd.get())
        uah_value = usd_value * 38.9
        rounded_value_uah = round(uah_value, 2)
        entry_uah.delete(0, END)  # Видаляємо попереднє значення
        entry_uah.insert(0, f"{rounded_value_uah} грн")  # Вставляємо нове значення в поле вводу для гривень
    except ValueError:
        pass

# Текст
main_text = Label(app, text="Валюта", font=("Roboto", 30, "bold"), bg="#00B894")
main_text.place(x=150, y=100)
result_text = Label(app, text="", font=("Roboto", 30, "bold"), justify="center", bg="#00B894")

# Кнопки
btn_uah_to_usd = Button(app, text="UAH → USD", font=("Roboto", 16, "bold"), bg="lightgreen", command=transform_uah_to_usd, compound="center")
btn_usd_to_uah = Button(app, text="UAH ← USD", font=("Roboto", 16, "bold"), bg="lightgreen", command=transform_usd_to_uah, compound="center")

# Поля вводу


# Розміщення

btn_uah_to_usd.place(x=50, y=180, width=150, height=35)
btn_usd_to_uah.place(x=300, y=180, width=150, height=35)
entry_uah.place(x=50, y=240, width=150, height=35)
entry_usd.place(x=300, y=240, width=150, height=35)
result_text.place(x=100, y=400)
entry_uah.insert(0, "UAH")
entry_usd.insert(0, "USD")


# Слухаємо події
app.mainloop()
