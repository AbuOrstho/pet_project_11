# Импортирование необходимых модулей
import qrcode  # Модуль для создания QR-кодов
from tkinter import *  # Модуль для создания графического интерфейса
from PIL import Image  # Модуль для работы с изображениями

# Глобальная переменная для хранения текущего окна
current_window = None

# Функция для создания QR-кода и отображения его в окне
def create_qr():
    global text, current_window

    # Если есть открытое окно, закрываем его
    if current_window:
        current_window.destroy()

    # Получаем данные для создания QR-кода
    data = text.get()

    # Имя файла для сохранения QR-кода
    filename = "qr_code.png"
    # Создаем QR-код
    img = qrcode.make(data)
    # Сохраняем QR-код в файл
    img.save(filename)

    try:
        # Открываем изображение для получения его размеров
        img = Image.open(filename)
        width, height = img.size
        width = width
        height = height
    except:
        return None

    # Создаем новое окно для отображения QR-кода
    root = Toplevel()
    root.geometry(f'{width}x{height}')
    root.title('Qr-code')
    qr_image = PhotoImage(file='qr_code.png')
    Label(root, image=qr_image).place(x=0, y=0)
    current_window = root
    root.mainloop()

# Создание основного окна
window = Tk()
window.configure(bg='#131313')  # Установка цвета фона
window.geometry('480x550')  # Установка размеров окна
window.resizable(False, False)  # Запрет изменения размеров окна

# Создание рамки внутри основного окна
frame = Frame(window, width=430, height=510, bg='#1C1C1C')
frame.place(x=25, y=20)

# Добавление текстовой метки и поля ввода в рамку
Label(frame, width=22, text='''Введите текст или ссылку''', bg='#1C1C1C', fg='white', font=('Arial', 11, 'bold')).place(
    x=10, y=20)
text = Entry(frame, width=25, bg='#464544', fg='white', bd=0, font=('Arial', 11, 'bold'))
text.place(x=215, y=24)

# Добавление кнопки для генерации QR-кода
Button(window, text='Сгенерировать', bg='green', fg='#1C1C1C', font=('Arial', 11, 'bold'), command=create_qr).place(
    x=180, y=475)

# Запуск главного цикла обработки событий
window.mainloop()
