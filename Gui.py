import tkinter as tk
from PIL import Image, ImageTk
from Constants import *


# Создаём окошко в tkinter
game_screen = tk.Tk()
game_screen.title(main_set["title"])
game_screen.geometry(main_set["geometry"])
game_screen.resizable(False, False)

# Подкачиваем нужное изображение
pilImage = Image.open(meme["img"])
meme_image = ImageTk.PhotoImage(pilImage)


'''LABELS'''
meme_name = tk.Label(game_screen,text = meme["name"],fg = name_meme_set["color"],font = name_meme_set["font"],height = name_meme_set["height"],width = name_meme_set["width"])
meme_text = tk.Label(game_screen,text = meme["text"],fg = text_meme_set["color"],font = text_meme_set["font"],height = text_meme_set["height"],width = text_meme_set["width"])

'''CANVAS'''
canvas = tk.Canvas(game_screen,height =canv_set["height"],width = canv_set["width"])
meme_imagesprite = canvas.create_image(canv_set["height"],canv_set["width"],image=meme_image)

'''FRAMES'''
buttons=tk.Frame(game_screen,height = button_set["height"],width = button_set["width"]*2, borderwidth=10)

'''BUTTONS'''
like = tk.Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["like"],bg = button_set["like_color"],font = button_set["font"])
dislike = tk.Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["dislike"],bg = button_set["dislike_color"],font = button_set["font"])

# Пакуемся 
meme_name.pack(side='top')
canvas.pack(side='top')
meme_text.pack(side='top')
buttons.pack(side='top')

# Гриды
like.grid(row = 1,column = 1)
dislike.grid(row = 1,column = 2)


game_screen.mainloop() # Главный обработчик событий