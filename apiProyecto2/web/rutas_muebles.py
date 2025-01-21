from flask import request, session
import json
import decimal
from __main__ import app
import controlador_muebles

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/muebles",methods=["GET"])
def muebles():
    muebles,code= controlador_muebles.obtener_muebles()
    return json.dumps(muebles, cls = Encoder),code

@app.route("/muebles/<id>",methods=["GET"])
def muebles_por_id(id):
    muebles,code = controlador_muebles.obtener_muebles_por_id(id)
    return json.dumps(mueble, cls = Encoder),code

@app.route("/muebles",methods=["POST"])
def guardar_mueble():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        mueble_json = request.json
        ret,code=controlador_muebles.insertar_mueble(mueble_json["nombre"], mueble_json["descripcion"], float(mueble_json["precio"]), mueble_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/juegos/<id>", methods=["DELETE"])
def eliminar_mueble(id):
    ret,code=controlador_muebles.eliminar_mueble(id)
    return json.dumps(ret), code

@app.route("/muebles", methods=["PUT"])
def actualizar_mueble():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        mueble_json = request.json
        ret,code=controlador_muebles.actualizar_mueble(mueble_json["id"],mueble_json["nombre"], mueble_json["descripcion"], float(mueble_json["precio"]),mueble_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code
