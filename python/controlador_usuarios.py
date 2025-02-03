from __future__ import print_function
from bd import obtener_conexion
from flask import session
import sys


def login_usuario(username, password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
                #cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s and clave= %s",(username,password))
                cursor.execute("SELECT perfil FROM usuarios WHERE usuario = '" + username +"' and clave= '" + password + "'")
                usuario = cursor.fetchone()
        conexion.close()
        if usuario is None:
            ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
        else:
            ret = {"status": "OK" }
            session["usuario"]=username
            session["perfil"]=usuario[0]
        code=200
    except:
        print("Excepcion al validar al usuario")   
        ret={"status":"ERROR"}
        code=500
    return ret,code    
    
def alta_usuario(username, password, perfil):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Verificar si el usuario YA EXISTE
            cursor.execute("SELECT usuario FROM usuarios WHERE usuario = '" + username + "'")
            usuario = cursor.fetchone()
            
            if usuario is None:
                # Insertar nuevo usuario
                cursor.execute(
                    "INSERT INTO usuarios(usuario, clave, perfil) VALUES ('" + username + "', '" + password + "', '" + perfil + "')"
                )
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret = {"status": "OK", "mensaje": "Usuario registrado correctamente"}  # Mensaje claro
                    code = 200
                else:
                    ret = {"status": "ERROR", "mensaje": "Error al registrar usuario"}
                    code = 500
            else:
                ret = {"status": "ERROR", "mensaje": "El usuario ya existe"}
                code = 200
        conexion.close()
    except Exception as e:
        print(f"Error en alta_usuario: {str(e)}")
        ret = {"status": "ERROR", "mensaje": "Error interno del servidor"}
        code = 500
    return ret, code
