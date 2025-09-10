from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():

    @staticmethod
    def getAllAirports():
        db = DBConnect.get_connection()
        listaAeroporti = []
        cursor = db.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""
        cursor.execute(query)

        for row in cursor:
            listaAeroporti.append(Airport(**row))

        cursor.close()
        db.close()
        return listaAeroporti

    @staticmethod
    def getAllFlights():
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        listaVoli=[]
        query = """SELECT * FROM flights"""
        cursor.execute(query)
        for c in cursor:
            listaVoli.append(Flight(**c))

        db.close()
        cursor.close()
        return listaVoli

    @staticmethod
    def getPeso(a1, a2):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT * FROM flights WHERE (ORIGIN_AIRPORT_ID = %s AND DESTINATION_AIRPORT_ID=%s)
                                    OR (ORIGIN_AIRPORT_ID = %s AND DESTINATION_AIRPORT_ID=%s)"""
        cursor.execute(query, (a1, a2, a2, a1))
        peso=0
        for c in cursor:
            peso+=1
        db.close()
        cursor.close()
        return peso

