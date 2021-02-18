from tkinter import *
from PIL import Image, ImageTk

# Окно создаёться...
root = Tk()
root.title('Мемы определяют возраст')
root.geometry('500x400+300+200')

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    pass

=======
    menu.place_forget()
    main.place(relx=0,  rely=0, relwidth=1,  relheight=1)
    
""" MENU """

''' BUTTONS '''

menu = Frame(root)

>>>>>>> Stashed changes
#quit
quitButton = Button(menu, bg='gray', fg='white', text='Выход', command=mQuit)
quitButton.place(relx=0.4,  rely=0.8, relwidth=0.2,  relheight=0.1)

#info
infoButton = Button(menu, bg='gray', fg='white', text='Инфо', command=mInfo)
infoButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)

#start
startButton = Button(menu, bg='gray', fg='white', text='Начать тест', command=mStart)
startButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)

<<<<<<< Updated upstream
#like
startButton = Button(menu, image=photoLike )
startButton.place(relx=0.4,  rely=0.50, relwidth=0.1,  relheight=0.1)
=======
""" MAIN """

main = Frame(root)

#like
likeButton = Button(main, image=photoLike )
likeButton.place(relx=0.4,  rely=0.50, relwidth=0.11,  relheight=0.13)

#canv = Canvas(main, width=100, height=100, bg='red')
#canv.create_rectangle(100, 100, 100, 100, outline='green')







#PACKER

menu.place(relx=0,  rely=0, relwidth=1,  relheight=1)
>>>>>>> Stashed changes

#startButton.pack()
#infoButton.pack()
#quitButton.pack()

menu.mainloop() # Главный обработчик событий

