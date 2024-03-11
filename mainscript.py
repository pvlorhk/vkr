import os
import eel

eel.init('web')

@eel.expose
def view_profile():
    #os.getdwd - позволяет получить путь к текущей папке
    #+'/knownfaces - добаляет к текущей пути папку knownfaces
    path = (os.getcwd()+'/knownfaces')
    #webbrowser.open(path) - открывает папку knownfaces с профилями
    os.system("start "+path)
eel.start('main.html')