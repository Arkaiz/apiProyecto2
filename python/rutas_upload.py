from __future__ import print_function
from __main__ import app
from flask import request, jsonify
import os
import json
import sys

@app.route('/upload', methods=['POST'])
def upload():
    try:
        f = request.files['fichero']
        user_input = request.form.get("nombre")
        
        # Usar el nombre del usuario como nombre final (incluyendo su extensión)
        new_filename = user_input
        
        # Ruta para guardar
        basepath = os.path.dirname(__file__)
        upload_dir = os.path.join(basepath, 'static')
        upload_path = os.path.join(upload_dir, new_filename)
        
        os.makedirs(upload_dir, exist_ok=True)
        f.save(upload_path)
        
        return jsonify({"status": "OK", "filename": new_filename}), 200
    except Exception as e:
        print(f"Error en upload: {str(e)}")
        return jsonify({"status": "ERROR", "message": str(e)}), 500
