from __future__ import print_function
from bd import obtener_conexion
import sys

def calculariva(importe):
    return importe * 0.21

def insertar_mueble(nombre, descripcion, precio, precioIVA,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO muebles(nombre, descripcion, precio, precioIVA, foto) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, descripcion, precio, precioIVA, foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un mueble", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_mueble_a_json(mueble):
    d = {}
    d['id'] = mueble[0]
    d['nombre'] = mueble[1]
    d['descripcion'] = mueble[2]
    d['precio'] = mueble[3]
    d['precioIVA'] = mueble[4]
    d['foto'] = mueble[5]
    return d

def obtener_muebles():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, precioIVA, foto FROM muebles")
            muebles = cursor.fetchall()
            mueblesjson=[]
            if muebles:
                for mueble in muebles:
                    mueblesjson.append(convertir_mueble_a_json(mueble))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los muebles", file=sys.stdout)
        mueblesjson=[]
        code=500
    return mueblesjson,code

def obtener_mueble_por_id(id):
    mueblejson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, precioIVA,foto FROM muebles WHERE id = %s", (id,))
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM muebles WHERE id =" + id)
            mueble = cursor.fetchone()
            if mueble is not None:
                mueblejson = convertir_mueble_a_json(mueble)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un mueble", file=sys.stdout)
        code=500
    return mueblejson,code


def eliminar_mueble(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM muebles WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un mueble", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_mueble(id, nombre, descripcion, precio, precioIVA,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE muebles SET nombre = %s, descripcion = %s, precio = %s, precioIVA = %s,foto=%s WHERE id = %s",
                       (nombre, descripcion, precio, precioIVA, foto, id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un mueble", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
