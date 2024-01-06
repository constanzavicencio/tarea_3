from importlib.metadata import files
import re
from werkzeug.utils import secure_filename
import filetype


# Funciones de validación 
def validar_region(region):
    return region != "sin-region"

def validar_comuna(comuna):
    return comuna != "sin-comuna"

def validar_tipo_artesania(lista_tipo_artesania):  
    lenght = len(lista_tipo_artesania)
    for i in range(lenght):
      if lista_tipo_artesania[i] == "seleccione":
        return False
    length_valid = 1 <= lenght <= 3
    return length_valid

def validar_nombre(nombre):
    if not nombre:
        return False
    length_valid = 3 <= len(nombre) <= 80
    format_valid = re.match(r'^[A-Za-z ]{3,80}$', nombre) is not None
    return length_valid and format_valid

def validar_email(email):
    if not email:
        return False
    format_valid = re.match(r'^[\w.]+@[a-zA-Z]{2,}\.[a-zA-Z]{2,3}$', email) is not None
    return format_valid

def validar_numero(numero):
    if numero:
        format_valid = re.match(r'^[+]56 9 [0-9]{4} [0-9]{4}$', numero) is not None
        return format_valid
    else:
        return True

def validar_imagenes(files):
    if (files is None) or (files == ""): return False

    ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/jpg", "image/png"}

    for file in files:
       ftype_guess = filetype.guess(file)
       if ftype_guess.extension not in ALLOWED_EXTENSIONS:
          return False
       if ftype_guess.mime not in ALLOWED_MIMETYPES:
          return False
       
    return True

    #def extension_permitida(filename):
    #    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    # Verifica si imgArtesanias está presente en files
    #if 'imgArtesanias' not in files:
    #    return False

    # file_list = files.getlist('imgArtesanias')

    # Verifica si hay al menos 1 y como máximo 3 elementos en la lista
    # length_valid = 1 <= files <= 3

    # Verifica que cada elemento sea un archivo con una extensión permitida
    # type_valid = all(extension_permitida(file.filename) for file in file_list)

    #return length_valid and type_valid


def validar_artesano(region, comuna, tipo_artesania, nombre, email, numero, imagenes):
  msg = ""

  if not validar_region(region): msg += "región"
  if not validar_comuna(comuna): msg += "comuna"
  if not validar_tipo_artesania(tipo_artesania): msg += "tipo de artesanía"
  if not validar_nombre(nombre): msg += "nombre"
  if not validar_email(email): msg += "email de contacto"
  if not validar_numero(numero): msg += "número de contacto"
  if not validar_imagenes(imagenes): msg += "imágenes artesanías"

  if msg == "":
    return True, msg
  
  else: 
    return False, msg