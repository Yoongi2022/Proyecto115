import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source='main.txt'
dest='newfile.txt'

os.rename(source,dest)
print("La ruta de origen fue renombrada ruta de destino exitosamente")

