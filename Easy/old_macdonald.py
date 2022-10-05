#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
     
    old_macdonald('macdonald') --> MacDonald
    
Note: `'macdonald'.capitalize()` returns `'Macdonald'`

def old_macdonald(name):
    newname = list(name)
    newname[0] = newname[0].upper()
    newname[3] = newname[3].upper()
    return ''.join(newname)
