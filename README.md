# Memes-define-age-Game
Игра "Мемы определяют возраст".
Данная игра определяет возраст игрока, по его реакции на мемы.

Данный проект разрабатывается студентами колледжа IThub (https://ithub.ru/).
IThub предоставляет аудитории и компьютеры для разработки проекта.

Авторами проекта являются:
Квашин Николай
Максимович Гавриил


Python VEnv(виртуальная среда):
    Зачем нужна вирт. среда? Во первых, так вы никогда не запутаетесь с версиями библиотек(ведь библиотеки в среде существуют отдельно от ОС),
    а во вторых, во всяких линуксах могут быть трабблы с системой, если устанавливать туда некоторые библитеки напрямую.

    Виртуальная среда не общая, она у каждого своя. Но файлик requirements.txt позволяет в одну команду подгружать нужные библиотеки в среду.

    Полезные команды в cmd(Windows):
        cd [путь до папки] - сменить директорию, перейти в папку. Если нужно перейти на другой диск(Допустим с C: на D:), то пишем cd /D [путь до папки]
        cd .. - переносит на одну директорию назад(Допустим из C:\Users\Пользователь в C:\Users)
        dir - если нужно просмотреть содержимое папки через консоль
        python [чтоугодно].py - запускаем наш код


    1) Создаём виртуальную среду(в консоли, заранее перейдя в папку проекта, используя команду cd) - python -m venv venv/  
    2) Чтобы активировать среду и запускать код внутри неё - перемещаемся в нужную папочку(cd venv/Scripts/) и запускаем скрипт командой activate.bat
    3) Изначально виртуальная среда пустая, но это не беда - уже находясь в своей среде пишем в консоль pip install -r requirements.txt и всё волшебным образом подкачивается с файлика.
    4) Если были установлены новые библиотеки или произошли какие-то обновления - пишем(в папке проекта, а не вирт. среды) pip freeze > requirements.txt
    и текстовый файлик из которого подкачиваются библиотеки обновляется

    P.S. Если нужно выйти из виртуальной среды, можно воспользоваться командой cd venv/Scripts/deactivate.bat, но я обычно просто закрываю консолю и всё.
    P.S.S. Вот источнек, но некоторые команды оттуда я изменял так, чтобы они  работали на шиндоус: 
    https://www.machinelearningmastery.ru/virtual-environments-104c62d48c54/

