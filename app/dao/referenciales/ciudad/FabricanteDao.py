# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class FabricanteDao:

    def getFabricantes(self):

        fabricanteSQL = """
        SELECT id, nombre, ruc, direccion, telefono
        FROM fabricantes
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(fabricanteSQL)
            # trae datos de la bd
            lista_fabricantes = cur.fetchall()
            print(lista_fabricantes)
            # retorno los datos
            lista_ordenada = []
            for item in lista_fabricantes:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "ruc": item[2],
                    "direccion": item[3],
                    "telefono": item[4]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getFabricanteById(self, id):

        fabricanteSQL = """
        SELECT id, nombre, ruc, direccion, telefono
        FROM fabricantes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(fabricanteSQL, (id,))
            # trae datos de la bd
            fabricanteEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id": fabricanteEncontrado[0],
                    "nombre": fabricanteEncontrado[1],
                    "ruc": fabricanteEncontrado[2],
                    "direccion": fabricanteEncontrado[3],
                    "telefono": fabricanteEncontrado[4]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarFabricante(self, nombre, ruc, direccion, telefono):

        insertFabricanteSQL = """
        INSERT INTO fabricantes(nombre, ruc, direccion, telefono) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertFabricanteSQL, (nombre, ruc, direccion, telefono))
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

    def updateFabricante(self, id, nombre, ruc, direccion, telefono):

        updateFabricanteSQL = """
        UPDATE fabricantes
        SET nombre=%s, ruc=%s, direccion=%s, telefono=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateFabricanteSQL, (telefono, direccion, ruc, nombre, id,))
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

    def deleteFabricante(self, id):

        deleteFabricanteSQL = """
        DELETE FROM fabricantes
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteFabricanteSQL, (id,))
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