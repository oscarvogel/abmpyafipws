#!/usr/bin/python
# -*- coding: utf-8 -*-
"Aplicativo Factura Electronica Libre"

__author__ = "Jose Oscar Vogel (oscarvogel@gmail.com)"
__copyright__ = "Copyright (C) 2015- Jose Oscar Vogel"
__license__ = "GPL 3.0+"
__version__ = "0.7c"


"Módulo con funciones auxiliares para el manejo de temas comunes"

from pyafipws.padron import PadronAFIP

class Utiles():
	
    def __init__(self):
        self.padron = PadronAFIP()
        
    def Buscar(self, Tabla='', idTabla='', ValorID=0):
        
        if Tabla == '':
            return False, None
            
        query = "select * from {} where {} = ?".format(Tabla, idTabla)
        params = [ValorID, ]
        self.padron.cursor.execute(query, params)
        
        fila = self.padron.cursor.fetchone()
        lRetorno = True if fila else False
        return lRetorno, fila
