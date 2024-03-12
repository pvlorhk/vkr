import eel
import os

eel.init('web')

@eel.expose
def view_profile():
    #os.getdwd - позволяет получить путь к текущей папке
    #+'/knownfaces - добаляет к текущей пути папку knownfaces
    path = (os.getcwd()+'/knownfaces')
    #webbrowser.open(path) - открывает папку knownfaces с профилями
    os.system("start "+path)

@eel.expose
def view_atten():
    #os.getdwd - позволяет получить путь к текущей папке
    file_path = (os.getcwd()+'/Attendance.csv')
    #webbrowser.open(path) - открывает файл Attendens с посещаемостью
    os.system("start "+file_path)

eel.start('main.html')