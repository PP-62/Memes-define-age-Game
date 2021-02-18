''' IMPORTS '''
from tkinter import *
from PIL import Image, ImageTk

''' VARIABLES '''
# Окно создаёться...
root = Tk()
root.title('Мемы определяют возраст')
root.geometry('500x400+300+200')

<<<<<<< HEAD
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
=======
canv = Canvas(menu, width=100, height=100, bg='red')
canv.create_rectangle(100, 100, 100, 100, outline='green')

>>>>>>> main
# Загрузка изображений
like = Image.open('Buttons/like.jpg')
like = like.resize((60, 55), Image.ANTIALIAS)
photoLike = ImageTk.PhotoImage(like)

''' FUNCTIONS '''
def mQuit():
    menu.quit()

def mInfo():
    info = Tk()
    info.title('Информация')
    info.geometry('200x100+450+350')
    info.mainloop()

def mStart():
<<<<<<< HEAD
<<<<<<< Updated upstream
    pass

=======
    menu.place_forget()
    main.place(relx=0,  rely=0, relwidth=1,  relheight=1)
    
""" MENU """

''' BUTTONS '''

menu = Frame(root)

>>>>>>> Stashed changes
=======
    quitButton.destroy()
    infoButton.destroy()
    startButton.destroy()

''' BUTTONS '''
>>>>>>> main
#quit
quitButton = Button(menu, bg='gray', fg='white', text='Выход', command=mQuit, font='Arial 12')
quitButton.place(relx=0.4,  rely=0.80, relwidth=0.2,  relheight=0.1)

#info
infoButton = Button(menu, bg='gray', fg='white', text='Инфо', command=mInfo, font='Arial 12')
infoButton.place(relx=0.4,  rely=0.65, relwidth=0.2,  relheight=0.1)

#start
startButton = Button(menu, bg='gray', fg='white', text='Начать тест', command=mStart, font='Arial 20')
startButton.place(relx=0.3,  rely=0.35, relwidth=0.4,  relheight=0.2)

<<<<<<< Updated upstream
#like
<<<<<<< HEAD
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
=======
# likeButton = Button(menu, image=photoLike )
# likeButton.place(relx=0.4,  rely=0.50, relwidth=0.11,  relheight=0.13)




>>>>>>> main

#startButton.pack()
#infoButton.pack()
#quitButton.pack()







menu.mainloop() # Главный обработчик событий
