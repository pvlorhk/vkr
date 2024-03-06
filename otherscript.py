import os
import webbrowser
#os.getdwd - позволяет получить путь к текущей папке
#+'/knownfaces - добаляет к текущей пути папку knownfaces
path = (os.getcwd()+'/knownfaces')
webbrowser.open(path)