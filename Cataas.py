from tkinter import*
from PIL import Image, ImageTk
import requests
from io import BytesIO
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOC)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    img = load_image(url)
    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x400")

        label.config(new_window,image = img)
        label.image = img
        label.pack()

def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x480")

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu-bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото",command=open_new_window())
file_menu.add_separator()
file_menu.add_command(label="Выход",command=exit)

#update_button = Button(text="Обновить", command=set_image)
#update_button.pack

url = 'https://cataas.com/cat'
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img
set_image()
window.mainloop()