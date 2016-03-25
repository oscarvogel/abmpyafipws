#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datos.py
#  
#  Copyright 2016 Jose Oscar Vogel <oscarvogel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

articulos = {
    '1': u'PRODUCTO 1',
    '2': u'PRODUCTO 2',
    }

TIPO_DOC_MAP= {80: u'CUIT', 96: u'DNI', 99: u'CF', 
               91: "CI Extranjera", 94: "Pasaporte"}
                
TIPO_CBTE_MAP = {1: u'Factura A', 2: u'Nota de Débito A', 
                 3: u'Nota de Crédito A', 4: 'Recibo A',
                 6: u'Factura B', 7: u'Nota de Débito B', 
                 8: u'Nota de Crédito B', 9: 'Recibo B',
                 11: u'Factura C', 12: u'Nota de Débito C', 
                 13: u'Nota de Crédito C', 15: 'Recibo C', 
                 51: u'Factura M', 52: u'Nota de Débito M',
                 53: u'Nota de Crédito M', 54: u'Recibo M',
                 }

CLASE_C = 11, 12, 13, 15
