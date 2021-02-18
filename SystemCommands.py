# С помощью os мы вводим в cmd команды с помощью питона
from os import system, getcwd, walk

'''Creating Virtual Environment'''
venvdir = f'{getcwd()}\\venv'
needVEnv = True
# Стратегия следующая: Если виртуальная среда уже установлена - не трогаем её, иначе нужно её установить
for address, dirs, files in walk(getcwd()):
    if venvdir == address:
        needVEnv = False
if needVEnv == True:
    system('python -m venv venv/')

system('cd venv/Scripts')
system('activate.bat')
for i in (1, 2):
    system('cd ..')
system('pip install -r requirements.txt')
