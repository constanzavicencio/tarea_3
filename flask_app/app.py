from flask import Flask, render_template, request, redirect, url_for
from util.validations import validar_artesano
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__, template_folder='templates')

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta para procesar el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index/index.html')
    
@app.route('/registrar-hincha', methods=['GET', 'POST'])
def registrar_hincha():
    if request.method == 'GET':
        return render_template('registrar/agregar-hincha.html')
    if request.method == 'POST':
        return render_template('registrar/agregar-hincha.html')
    
@app.route('/listado-hinchas', methods=['GET', 'POST'])
def listado_hinchas():
    if request.method == 'GET':
        return render_template('listado/ver-hinchas.html')

@app.route('/registrar-artesano', methods=['GET', 'POST'])
def registrar_artesano():
    if request.method == 'POST':
        region = request.form.get('regiones')
        comuna = request.form.get('comunas')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        numero = request.form.get('numero')
        descripcion_artesania = request.form.get('descArtesania')
        artesanias = request.form.getlist('tipoArtesania')
        imagenes_artesania = request.files.getlist('imgArtesanias')

        error = ""
        status, msg = validar_artesano(region, comuna, artesanias, nombre, email, numero, imagenes_artesania)
        if status:
            # Obtener id region
            art_region = db.get_region_id_by_name(region)
            # Obtener id comuna de acuerdo al id region
            art_comuna = db.get_comuna_id_by_region_id(comuna, art_region)
            
            # Insertar artesano
            db.insertar_artesano(art_comuna, descripcion_artesania, nombre, email, numero)
            artesano_id = db.get_artesano_id_by_name(nombre)

            # Insertar imágenes
            for imagen in imagenes_artesania:
                
                _filename = hashlib.sha256(secure_filename(imagen.filename).encode("utf-8")).hexdigest()
                _extension = filetype.guess(imagen).extension
                img_filename = f"{_filename}.{_extension}"
                
                basedir = os.path.abspath(os.path.dirname(__file__))
                imagen.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))
                
                # guardar imagen en la base de datos
                nombre_archivo = img_filename
                ruta_archivo = "/static/uploads/"+str(img_filename)
                db.insertar_foto(ruta_archivo, nombre_archivo, artesano_id)
                

            # Insertar por tipo de artesanía
            artesanias_list = ["marmol", "madera", "ceramica", "mimbre", "metal", "cuero", "telas", "joyas", "otro tipo"]
            artesanias_Selected = []

            for artesania in artesanias:
                id_artesania = artesanias_list.index(artesania) + 1
                artesanias_Selected.append(id_artesania)

            largo_artesanias = len(artesanias_Selected)

            if largo_artesanias >= 1:
                db.insertar_artesano_tipo(artesano_id, artesanias_Selected[0])
                if largo_artesanias >= 2:
                    db.insertar_artesano_tipo(artesano_id, artesanias_Selected[1])
                    if largo_artesanias == 3:
                        db.insertar_artesano_tipo(artesano_id, artesanias_Selected[2])

            return render_template("registrar/agregar-artesano.html", error=error)
        else: 
            error += msg
            return render_template("registrar/agregar-artesano.html", error=error)
    elif request.method == 'GET':
        msg = ""
        return render_template("registrar/agregar-artesano.html")
    
@app.route("/verinfohincha/<int:id>", methods=["GET"])
def verinfohincha(id):
    data = []
    if id == 1:
        nombre = "Nicole"
        region = "Región Metropolitana"
        comuna = "Maipú"
        email = "nicole123@gmail.com"
        deportes_list = ["Tenis", "Natación"]
        modo_transporte = "Particular"
        celular = "+56 9 8765 4321"
        comentarios = "Sí"
    if id == 2:
        nombre = "Nicolás"
        region = "RM"
        comuna = "Cerro Navia"
        email = "nicouwu@gmail.com"
        deportes_list = ["Balonmano"]
        modo_transporte = "Particular"
        celular = "+56 9 5500 1122"
        comentarios = ""
    if id == 3:
        nombre = "Josefina"
        region = "Región de Valparaíso"
        comuna = "Viña del Mar"
        email = "jose2002@hotmail.com"
        deportes_list = ["Fútbol", "Boxeo"]
        modo_transporte = "Locomoción colectiva"
        celular = "+56 9 7890 1234"
        comentarios = ""
    if id == 4:
        nombre = "Juan"
        region = "Región de Tarapacá"
        comuna = "Iquique"
        email = "juan3007@hotmail.com"
        deportes_list = ["Fútbol", "BMX Racing", "Esgrima"]
        modo_transporte = "Locomoción colectiva"
        celular = "+56 9 6655 7788"
        comentarios = ""
    if id == 5:
        nombre = "María"
        region = "Región de Los Lagos"
        comuna = "Puerto Montt"
        email = "mary@gmail.com"
        deportes_list = ["Salto ecuestre"]
        modo_transporte = "Particular"
        celular = "+56 9 2345 6789"
        comentarios = "Hola mundo"
        
    data.append({
        "nombre": nombre,
        "region": region,
        "comuna": comuna,
        "email": email,
        "deportes": deportes_list,
        "modo_transporte": modo_transporte,
        "numero": celular,
        "comentario": comentarios
    })

    return render_template("informacion/informacion-hincha.html", data=data)

@app.route("/verinfoartesano/<nombre>", methods=["GET"])
def verinfoartesano(nombre):

    data = []
    print(db.get_all_artesano(nombre))
    id, comuna_id, descripcion_artesania, nombre, email, celular = db.get_all_artesano(nombre)[0]

    # Se transforman los ids de las comunas a sus nombres
    comuna_data = db.get_comuna_byindex(comuna_id)
    comuna = comuna_data[0][0]+" |"

    # Obtenemos la region
    region_data_c = db.get_region_by_id(comuna_id)
    region_data = region_data_c[0][0]
    region = db.get_region_byregid(region_data)[0][0]

    # Se obtienen los tipos de artesanias el artesano
    tipo_artesania = ""
    artlist = db.get_artesanias_de_artesano(id)
    for i in artlist:
        art_nombre = db.get_artesania_byindex(i[0])
        tipo_artesania += art_nombre[0][0] + ", "
    tipo_artesania = tipo_artesania[:-2]

    # FOTOS #
    lista_fotos = db.get_fotos_artesano(id)
    cantidad_fotos = len(lista_fotos)

    if cantidad_fotos >= 1:
        fotos1 = f"uploads/{lista_fotos[0][1]}"
        foto1 = url_for('static', filename=fotos1)
        foto2, foto3 = "", ""
        if cantidad_fotos >= 2:
            fotos2 = f"uploads/{lista_fotos[1][1]}"
            foto2 = url_for('static', filename=fotos2)
            if cantidad_fotos == 3:
                fotos3 = f"uploads/{lista_fotos[2][1]}"
                foto3 = url_for('static', filename=fotos3)

    data.append({
        "nombre": nombre,
        "tipo_artesania": tipo_artesania,
        "descripcion": descripcion_artesania,
        "fotos1": foto1,
        "fotos2": foto2,
        "fotos3": foto3,
        "region": region,
        "comuna": comuna,
        "email": email,
        "numero": celular
    })
        
    return render_template("informacion/informacion-artesano.html", data=data)

@app.route("/listado_artesanos/<int:page>", methods=["GET"])
def listado_artesanos(page):
    # ?? No toma
    if page < 0:
        return redirect(url_for("listado_artesanos", page=0, data=data))
    else:
        pagenum = int(page)
        
    data = []
    for conf in db.get_list_artesanos(pagenum):
        id, comuna_id, descripcion_artesania, nombre, email, celular = conf

        # Se transforman los ids de las comunas a sus nombres
        comuna_data = db.get_comuna_byindex(comuna_id)
        comuna = comuna_data[0][0]
        
        # Se obtienen los tipos de artesanias el artesano
        tipo_artesania = ""
        artlist = db.get_artesanias_de_artesano(id)
        for i in artlist:
            art_nombre = db.get_artesania_byindex(i[0])
            tipo_artesania += art_nombre[0][0] + ", "
        tipo_artesania = tipo_artesania[:-2]

        # FOTOS #
        lista_fotos = db.get_fotos_artesano(id)
        cantidad_fotos = len(lista_fotos)

        if cantidad_fotos >= 1:
            fotos1 = f"uploads/{lista_fotos[0][1]}"
            foto1 = url_for('static', filename=fotos1)
            foto2, foto3 = "", ""
            if cantidad_fotos >= 2:
                fotos2 = f"uploads/{lista_fotos[1][1]}"
                foto2 = url_for('static', filename=fotos2)
                if cantidad_fotos == 3:
                    fotos3 = f"uploads/{lista_fotos[2][1]}"
                    foto3 = url_for('static', filename=fotos3)

        data.append({
            "nombre": nombre,
            "celular": celular,
            "comuna": comuna,
            "tipo_artesania": tipo_artesania,
            "fotos1": foto1,
            "fotos2": foto2,
            "fotos3": foto3
        })


    return render_template("listado/ver-artesanos.html", page=page, data=data)


if __name__ == '__main__':
    app.run(debug=True)
