from __future__ import print_function
from __main__ import app
from flask import request, send_file
import os
import sys
import json
import subprocess

@app.route('/ver/<archivo>', methods=['GET'])
def ver(archivo):
    try:
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static', archivo)
        
        if not os.path.exists(upload_path):
            return json.dumps({"status": "ERROR", "mensaje": "Archivo no existe"}), 404
        
        # Enviar el archivo directamente (para imágenes/binarios)
        return send_file(upload_path, as_attachment=False)
    
    except Exception as e:
        print(f"Error al leer archivo: {str(e)}")
        return json.dumps({"status": "ERROR"}), 500
