from importlib.metadata import files
import re
from werkzeug.utils import secure_filename
import filetype


# Validaciones en común

def validar_region(region):
    return region != "sin-region"

def validar_comuna(comuna):
    return comuna != "sin-comuna"

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

# Validaciones hincha

def validar_deportes(value):
  if (value is None): return False
  if (value == ""): return False
  # Sports
  deportes = ["Clavados","Natación","Natación artística","Polo acuático","Natación en Aguas abiertas","Maratón","Marcha","Atletismo","Bádminton","Balonmano","Básquetbol","Básquetbol 3x3","Béisbol","Boxeo","Bowling","Breaking","Canotaje Slalom","Canotaje de velocidad","BMX Freestyle","BMX Racing","Mountain Bike","Ciclismo pista","Ciclismo ruta","Adiestramiento ecuestre","Evento completo ecuestre","Salto ecuestre","Escalada deportiva","Esgrima","Esquí acuático y Wakeboard","Fútbol","Gimnasia artística Masculina","Gimnasia artística Femenina","Gimnasia rítmica","Gimnasia trampolín","Golf","Hockey césped","Judo","Karate","Levantamiento de pesas","Lucha","Patinaje artístico","Skateboarding","Patinaje velocidad","Pelota vasca","Pentatlón moderno","Racquetball","Remo","Rugby 7","Sóftbol","Squash","Surf","Taekwondo","Tenis","Tenis de mesa","Tiro","Tiro con arco","Triatlón","Vela","Vóleibol","Vóleibol playa"]
  Valid = True
  # value contiene los indices de los deportes seleccionados
  for deporte in value:
    if deporte not in deportes:
       Valid = False
       return Valid
  return Valid

def validar_transporte(transporte):
  if (transporte is None): return False
  if (transporte == ""): return False
  if (transporte == "Seleccione"): return False
  return True

def validar_comentarios(comentarios):
  if (comentarios is None): return True
  # length validation
  maxlength = len(comentarios) <= 80
  return maxlength and True

def validar_hincha(deportes, region, comuna, transporte, nombre, email, numero, comentarios):
  msg = ""
  if not validar_deportes(deportes): msg += "deportes"
  if not validar_region(region): msg += "región"
  if not validar_comuna(comuna): msg += "comuna"
  if not validar_transporte(transporte): msg += "transporte"
  if not validar_nombre(nombre): msg += "nombre"
  if not validar_email(email): msg += "email de contacto"
  if not validar_numero(numero): msg += "número de contacto"
  if not validar_comentarios(comentarios): msg += "comentarios"

  if msg == "":
    return True, msg
  
  else: 
    return False, msg
  
# Validaciones artesano
  
def validar_tipo_artesania(lista_tipo_artesania):  
    lenght = len(lista_tipo_artesania)
    for i in range(lenght):
      if lista_tipo_artesania[i] == "seleccione":
        return False
    length_valid = 1 <= lenght <= 3
    return length_valid
  
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