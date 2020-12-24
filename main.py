from tkinter import *
from PIL import Image, ImageTk

# Окно создаёться...
menu = Tk()
menu.title('Мемы определяют возраст')
menu.geometry('500x400+300+200')

# Загрузка изображений
like = Image.open('like.jpg')
like = like.resize((50, 50), Image.ANTIALIAS)
photoLike = ImageTk.PhotoImage(like)


def mQuit():
    menu.quit()

def mInfo():
    info = Tk() 
    info.title('Информация')
    info.geometry('200x100+450+350')
    info.mainloop()

def mStart():
    pass

#quit
quitButton = Button(menu, bg='gray', fg='white', text='Выход', command=mQuit)
quitButton.place(relx=0.4,  rely=0.8, relwidth=0.2,  relheight=0.1)

#info
infoButton = Button(menu, bg='gray', fg='white', text='Инфо', command=mInfo)
infoButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)

#start
startButton = Button(menu, bg='gray', fg='white', text='Начать тест', command=mStart)
startButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)

#like
startButton = Button(menu, image=photoLike )
startButton.place(relx=0.4,  rely=0.50, relwidth=0.1,  relheight=0.1)


menu.mainloop() # Главный обработчик событий

