from tkinter import *
from PIL import Image, ImageTk
from Constants import *
from random import randint

def mk_res():
    return {}
def add_res(n,v,results):
    results[n] = v
    
######
    
# Создаём окошко в tkinter
root = Tk()
root.title(main_set["title"])
root.geometry(main_set["geometry"])
root.resizable(False, False)

######

def get_memes(memes_list,size):
    m = memes_list.copy()
    memes = []
    for _ in range(size):
        memes.append(m.pop(randint(0,len(m)-1)))
    print(memes)
    return memes

meme_list = get_memes(memes,3)
counter = 0
results = mk_res()


# Подкачиваем нужное изображение
meme_image = None
def upd_img(meme):
    global meme_image
    pilImage = Image.open(meme["img"])
    pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)
    meme_image = ImageTk.PhotoImage(pilImage)

meme = meme_list[counter]
upd_img(meme)

game_screen = Frame(root)

'''LABELS'''
meme_name = Label(game_screen,text = meme["name"],fg = name_meme_set["color"],font = name_meme_set["font"],height = name_meme_set["height"],width = name_meme_set["width"])
meme_text = Label(game_screen,text = meme["text"],fg = text_meme_set["color"],font = text_meme_set["font"],height = text_meme_set["height"],width = text_meme_set["width"])

'''IMAGE'''

IMG = Label(game_screen, image=meme_image)

#canvas = Canvas(game_screen,height =canv_set["height"],width = canv_set["width"])
#meme_imagesprite = canvas.create_image(canv_set["height"],canv_set["width"],image=meme_image)

'''FRAMES'''
buttons=Frame(game_screen,height = button_set["height"],width = button_set["width"]*2, borderwidth=10)

'''BUTTONS'''
like = Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["like"],bg = button_set["like_color"],font = button_set["font"],command = lambda:result(meme["name"],True))
dislike = Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["dislike"],bg = button_set["dislike_color"],font = button_set["font"],command = lambda:result(meme["name"],False))

def result(name,value:bool):
    
    global meme,counter
    add_res(name,value,results)
    #change meme
    counter+=1
    print(results)
    if counter == len(meme_list):
        game_screen.place_forget()

    else:
        meme = meme_list[counter]
        meme_name.config(text = meme["name"])
        meme_text.config(text = meme["text"])
        upd_img(meme)
        IMG.config(image = meme_image)
    #
# Пакуемся 

game_screen.place(relx=0,  rely=0, relwidth=1,  relheight=1)

meme_name.pack(side='top')
#canvas.pack(side='top')
IMG.pack(side='top')
meme_text.pack(side='top')
buttons.pack(side='top')

# Гриды
like.grid(row = 1,column = 1)
dislike.grid(row = 1,column = 2)


game_screen.mainloop() # Главный обработчик событий
