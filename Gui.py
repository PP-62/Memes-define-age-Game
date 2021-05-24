from tkinter import *
from PIL import Image, ImageTk
from Constants import *
from random import randint
import pickle

######хранение результатов

# def mk_res():

#     return {}

def add_res(n,v,results):
    results[n] = v
    
######
    
# Создаём окошко в tkinter

root = Tk()
root.title(main_set["title"])
root.geometry(main_set["geometry"])
root.resizable(False, False)

######функции

def get_memes(memes_list,size):
    m = memes_list.copy()
    memes = []
    for _ in range(size):
        memes.append(m.pop(randint(0,len(m)-1)))
    print(memes)
    return memes

def upd_img(meme):
    global meme_image
    pilImage = Image.open(meme["img"])
    pilImage = pilImage.resize((200, 200), Image.ANTIALIAS)
    meme_image = ImageTk.PhotoImage(pilImage)

def upd(name,id,value:bool):
    
    global meme,counter
    add_res(id,value,data)
    #change meme
    counter+=1
    print(data)
    if counter == len(meme_list):
        game_screen.place_forget()
        result_screen.place(relx=0,  rely=0, relwidth=1,  relheight=1)
        end()
    else:
        meme = meme_list[counter]
        meme_name.config(text = meme["name"])
        meme_text.config(text = meme["text"])
        upd_img(meme)
        IMG.config(image = meme_image)


def end():
    clean_data = [[0]*22]
    
    for i in data.keys():
        for j in range(len(clean_data)):
            clean_data[0][j] += int(memes[int(i)]["data"][j]) if data[i] else 0
    print(clean_data)
    loaded_model = pickle.load(open("liner_model.sav", 'rb'))
    result = int(loaded_model.predict(clean_data))/10
    result_text.configure(text = result)

def menu_quit():
    menu.quit()

def menu_info():
    info = Tk()
    info.title('Информация')
    info.geometry('200x100+450+350')
    info.mainloop()

def menu_start():
    menu.place_forget()
    game_screen.place(relx=0,  rely=0, relwidth=1,  relheight=1)
 
######        


meme_list = get_memes(memes,3)
counter = 0
data = {}
result = 0



# Подкачиваем нужное изображение

meme_image = None

meme = meme_list[counter]
upd_img(meme)

###### виджеты

'''FRAMES'''

menu = Frame(root)

game_screen = Frame(root)
buttons=Frame(game_screen,height = button_set["height"],width = button_set["width"]*2, borderwidth=10)

result_screen = Frame(root)



'''LABELS'''
meme_name = Label(game_screen,text = meme["name"],fg = name_meme_set["color"],font = name_meme_set["font"],height = name_meme_set["height"],width = name_meme_set["width"])
meme_text = Label(game_screen,text = meme["text"],fg = text_meme_set["color"],font = text_meme_set["font"],height = text_meme_set["height"],width = text_meme_set["width"])
result_top_text = Label(result_screen,text = result_text_set["text"],fg = result_text_set["color"],font = result_text_set["font"],height = result_text_set["height"],width = result_text_set["width"])
result_text = Label(result_screen,fg = result_text_set["color"],font = result_text_set["font_val"],height = result_text_set["height"],width = result_text_set["width"])


'''IMAGE'''

IMG = Label(game_screen, image=meme_image)



#canvas = Canvas(game_screen,height =canv_set["height"],width = canv_set["width"])
#meme_imagesprite = canvas.create_image(canv_set["height"],canv_set["width"],image=meme_image)


'''BUTTONS'''

#menu
quitButton = Button(menu, bg=quitButton["bg"], fg=quitButton["fg"], text=quitButton["text"], command=menu_quit, font=quitButton["font"])
infoButton = Button(menu, bg=infoButton["bg"], fg=infoButton["fg"], text=infoButton["text"], command=menu_info, font=infoButton["font"])
startButton = Button(menu, bg=startButton["bg"], fg=startButton["fg"], text=startButton["text"], command=menu_start, font=startButton["font"])

#main
like = Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["like"],bg = button_set["like_color"],font = button_set["font"],command = lambda:upd(meme["name"],meme["id"],True))
dislike = Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["dislike"],bg = button_set["dislike_color"],font = button_set["font"],command = lambda:upd(meme["name"],meme["id"],False))


#

# Пакуемся 

#фрейм
menu.place(relx=0,  rely=0, relwidth=1,  relheight=1)

#виджеты

#menu
quitButton.place(relx=0.4,  rely=0.80, relwidth=0.2,  relheight=0.1)
infoButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)
startButton.place(relx=0.3,  rely=0.35, relwidth=0.4,  relheight=0.2)

#main
meme_name.pack(side='top')
#canvas.pack(side='top')
IMG.pack(side='top')
meme_text.pack(side='top')
buttons.pack(side='top')

#results
result_top_text.place(relx=0.3,  rely=0.2, relwidth=0.4,  relheight=0.1)
result_text.place(relx=0.4,  rely=0.4, relwidth=0.2,  relheight=0.1)

# Гриды
like.grid(row = 1,column = 1)
dislike.grid(row = 1,column = 2)


game_screen.mainloop() # Главный обработчик событий
