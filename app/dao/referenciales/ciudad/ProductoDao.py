# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProductoDao:

    def getProductos(self):

        productoSQL = """
        SELECT id, nombre, round(costo) as costo, id_fabricante
        FROM productos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(productoSQL)
            # trae datos de la bd
            lista_productos = cur.fetchall()
            print(lista_productos)
            # retorno los datos
            lista_ordenada = []
            for item in lista_productos:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "costo": item[2],
                    "id_fabricante": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProductoById(self, id):

        productoSQL = """
        SELECT id, nombre, costo, id_fabricante
        FROM productos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(productoSQL, (id,))
            # trae datos de la bd
            productoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id": productoEncontrado[0],
                    "nombre": productoEncontrado[1],
                    "costo": productoEncontrado[2],
                    "id_fabricante": productoEncontrado[3]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProducto(self, nombre, costo):

        insertProductoSQL = """
        INSERT INTO productos(nombre, costo) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProductoSQL, (nombre, costo))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updateProducto(self, id, nombre, costo):

        updateProductoSQL = """
        UPDATE productos
        SET nombre=%s, costo=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProductoSQL, (costo, nombre, id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deleteProducto(self, id):

        deleteProductoSQL = """
        DELETE FROM productos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProductoSQL, (id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False