import pathlib
from pathlib import Path

rutas = []

rutas.append('Z:\\')
rutas.append('Y:\\')
rutas.append('X:\\smb1\\Descargas')

files = []

for r in rutas:
    p = Path(r).glob('**/*')
    # files = [x for x in p if x.is_file() and x.suffix in ('.mp4','.avi') ]
    for x in p:
        if x.is_file() and x.suffix in ('.mp4','.avi'):
            files.append(x)
    


print (files)