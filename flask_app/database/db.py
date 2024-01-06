import pymysql
import json
import os
#from util import *;

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open(os.path.join(os.path.dirname(__file__), 'querys.json'), 'r') as querys:
	QUERY_DICT = json.load(querys)

def get_conn():
  conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
  return conn


# Inserciones

def insertar_artesano(comuna_id, descripcion_artesania, nombre, email, celular):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["insertar_artesano"], (comuna_id, descripcion_artesania, nombre, email, celular))
  conn.commit() ## commit es para registrar y fetchone para obtener datos

def insertar_artesano_tipo(artesano_id, tipo_artesania_id):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["insertar_artesano_tipo"], (artesano_id, tipo_artesania_id))
  conn.commit()

def insertar_foto(ruta_archivo, nombre_archivo, artesano_id):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["insertar_foto"], (ruta_archivo, nombre_archivo, artesano_id))
  conn.commit()

# Listados

# Obtener listado de artesanos ordenados de más reciente a más antiguo
def obtener_artesanos():
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["listado_artesanos"])
  artesanos = cursor.fetchall()
  return artesanos

def obtener_primeros_5_artesanos():
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["primeros_5_artesanos"])
  artesanos = cursor.fetchall()
  return artesanos

def obtener_primeros_5_artesanos():
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["siguientes_5_artesanos"])
  artesanos = cursor.fetchall()
  return artesanos

def get_all_artesano(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_all_artesano"], (nombre,))
	artesano = cursor.fetchall()
	return artesano

def get_list_artesanos(page):
	offset = page * 5
	limit = 5
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_list_artesanos"], (limit, offset,))
	list_artesanos = cursor.fetchall()
	return list_artesanos


## otros
def get_ultimo_id():
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["obtener_ultimo_id"])
  ultimo_id = cursor.fetchone()
  return ultimo_id

def get_comuna_id_by_region_and_comuna(region, comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_id_by_region_and_comuna"], (region, comuna))
	comuna_id = cursor.fetchone()
	return comuna_id

def get_comuna_byindex(comuna_id):
	conn = get_conn()	
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_id"], (comuna_id,))
	comuna = cursor.fetchall()
	return comuna

def get_artesano_id_by_name(nombre):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["get_artesano_id_by_name"], (nombre))
  artesano_id = cursor.fetchone()
  return artesano_id

# -- db-related functions --

def get_region_by_id(comuna_id):
	conn = get_conn()	
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region_by_id"], (comuna_id,))
	region_id  = cursor.fetchall()
	return region_id

def get_region_byregid(region_id):
	conn = get_conn()	
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region_byregid"], (region_id,))
	region = cursor.fetchall()
	return region

def get_region_id_by_name(region):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["get_region_id_by_name"], (region))
  region_id = cursor.fetchone()
  return region_id[0]

def get_comuna_id_by_region_id(comuna, region_id):
  conn = get_conn()
  cursor = conn.cursor()
  cursor.execute(QUERY_DICT["get_comuna_id_by_region_id"], (comuna, region_id))
  comuna_id = cursor.fetchone()
  return comuna_id[0]

## Otras funciones

def get_artesanias_de_artesano(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesanias_de_artesano"], (artesano_id,))
	artesanias = cursor.fetchall()
	return artesanias

def get_artesania_byindex(artesania_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_artesania_byindex"], (artesania_id,))
	artesania = cursor.fetchall()
	return artesania

def get_fotos_artesano(artesano_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_fotos_artesano"], (artesano_id,))
	fotos = cursor.fetchall()
	return fotos


