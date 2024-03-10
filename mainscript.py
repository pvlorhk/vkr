import os
import webbrowser
import eel

eel.init('web')

@eel.expose
def view_profile():
    #os.getdwd - позволяет получить путь к текущей папке
    #+'/knownfaces - добаляет к текущей пути папку knownfaces
    path = (os.getcwd()+'/knownfaces')
    #webbrowser.open(path) - открывает папку knownfaces с профилями
    webbrowser.open(path)
eel.start('main.html')