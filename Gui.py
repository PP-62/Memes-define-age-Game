import tkinter as tk
# надо импортировать Pillow

main_set = {"geometry":"500x500",
        "background":"white",
        "title":"meme game"}

meme = {"name":"имя",
        "text":"подпись",
    "info":"Инфа о меме",
        "img":"image_link"}


canv_set = {"height":300,
        "width":400,
        "background":"white"}

name_meme_set = {"color":"black",
                 "font":"Arial 14",
                 "height":2,
                 "width":20}

text_meme_set = {"color":"black",
                 "font":"Arial 8",
                 "height":2,
                 "width":20}

button_set = {"height":1,
              "width":6,
              "color":"black",
              "font":"Arial 14",
              "like":"like",
              "like_color":"green",
              "dislike":"dislike",
              "dislike_color":"red"}

#root
root = tk.Tk()
root.title(main_set["title"])
root.geometry(main_set["geometry"])
root.resizable(False, False)

#elements_place
meme_image = ""
#meme_image = tk.PhotoImage(file = meme["img"])
#добавить изображение в канвас

main = tk.Frame(root)
meme_name = tk.Label(main,text = meme["name"],fg = name_meme_set["color"],font = name_meme_set["font"],height = name_meme_set["height"],width = name_meme_set["width"])
meme_text = tk.Label(main,text = meme["text"],fg = text_meme_set["color"],font = text_meme_set["font"],height = text_meme_set["height"],width = text_meme_set["width"])
canvas = tk.Canvas(main,height =canv_set["height"],width = canv_set["width"],bg = canv_set["background"])
buttons=tk.Frame(main,height = button_set["height"],width = button_set["width"]*2)
like = tk.Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["like"],bg = button_set["like_color"],font = button_set["font"])
dislike = tk.Button(buttons,height = button_set["height"],width = button_set["width"],text = button_set["dislike"],bg = button_set["dislike_color"],font = button_set["font"])

#pack
meme_name.pack(side='top')
canvas.pack(side='top')
meme_text.pack(side='top')
buttons.pack(side='top')

like.grid(row = 1,column = 1)
dislike.grid(row = 1,column = 2)

