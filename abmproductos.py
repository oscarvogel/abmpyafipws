#!/usr/bin/python
# -*- coding: utf-8 -*-
"Aplicativo Factura Electronica Libre"

__author__ = "Jose Oscar Vogel (oscarvogel@gmail.com)"
__copyright__ = "Copyright (C) 2015- Jose Oscar Vogel"
__license__ = "GPL 3.0+"
__version__ = "0.1a"

import gui          # import gui2py package (shortcuts)
import locale

from pyafipws.padron import PadronAFIP
from utiles import Utiles

padron = PadronAFIP()
CONFIG_FILE = "rece.ini"
DB = None

utiles = Utiles()

locale.setlocale(locale.LC_ALL, '')

def ExisteProductos():
    try:
        padron.cursor.execute("select * from productos")
    except:
        padron.cursor.execute("CREATE TABLE productos ("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "detalle VARCHAR(150), "
                        "precio_uni real, "
                        "alicuota_iva real "
                        ");")

def limpiar(evt):
    panel['idProducto'].value = 0
    panel['detalle'].value = ""
    panel['precio'].value = 0.00
    panel['iva_id'].value = 1

def actualizar(evt):
    id_producto = panel['idProducto'].value
    detalle = panel['detalle'].value
    precio = panel['precio'].value
    iva_id = panel['iva_id'].value
    ok, fila = utiles.Buscar('productos', 'id', id_producto)
    if ok:
        sql = ("update productos "
		       " set detalle=?, "
		       " precio_uni=?, alicuota_iva=?"
		       " where id=?"
		       )
        params = [detalle, precio, iva_id, id_producto]
    else:
        sql = ("insert into productos ("
               " detalle, precio_uni, alicuota_iva )"
               " values(?, ?, ?)"
		       )
        params = [detalle, precio, iva_id]
    padron.cursor.execute(sql, params)
    padron.db.commit()

def borrar(evt):
    pass

def buscarproductos(evt):
    pass

def on_cierra(evt):
    mywin.close()

def on_idchange(evt):
    id_producto = panel['idProducto'].value
    ok, fila = utiles.Buscar('productos', 'id', id_producto)
    if ok:
        panel['detalle'].value = fila['detalle']
        panel['precio'].value = fila['precio_uni']
        panel['iva_id'].value = fila['alicuota_iva']

	
# --- gui2py designer generated code starts ---

with gui.Window(name='abmproductos', 
                title=u'Aplicativo Facturaci\xf3n Electr\xf3nica', 
                resizable=True, height='636px', left='181', top='52', 
                width='794px', image=''):
    gui.StatusBar(name='statusbar_15_91', 
                  text=u'Servicio Web Factura Electr\xf3nica mercado interno (WSFEv1)', )
    with gui.Panel(label=u'', name='ppal'):
        with gui.Panel(label=u'', name='record', 
				   image='', sizer_border=5, height='500', left='8', top='6', width='633',):
            nTop = '10'
            gui.Label(name='lblID', text=u'Código de Producto:', width='96', top=nTop)
            gui.TextBox(name='idProducto', 
					width='110', 
					onblur=on_idchange,
					top=nTop, 
					left='130',
					autoSelect=True)
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblDetalle', text=u'Detalle:', width='100', top=nTop,)
            gui.TextBox(name='detalle', 
					width='400', 
					value=u'',
					top=nTop, left='130'
					)
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblPrecio', text=u'Precio:', width='100', top=nTop,)
            gui.TextBox(mask='#{12}.#{2}', 
                    alignment='right',
                    name='precio', 
					width='110', 
					value=u'',
					top=nTop, left='130',
					)
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblIVA', text=u'Tipo IVA:', width='100', top=nTop,)
            gui.ComboBox(name=u'iva_id',text=u'IVA', 
                         left='130', top=nTop, width='190', editable=False,
                         items={1: "no gravado", 2: "exento", 
                                3: "0%", 4: "10.5%", 5: "21%" , 
                                6: "27%", 8: "5%", 9: "2.5%"},)
                         
        nTopPanel = str(int(nTop)+30)
        nTop = str(int(nTop)+50)
        
        gui.Button(label=u'Crear', name='create', sizer_border=4, top=nTop, left='10', onclick=limpiar)
        gui.Button(label=u'Recuperar', name='retrieve', sizer_border=4, top=nTop, left='110')
        gui.Button(label=u'Actualizar', name='update', sizer_border=4, top=nTop, left='210', onclick=actualizar)
        gui.Button(label=u'Borrar', name='delete', sizer_border=4, top=nTop, left='310', onclick=borrar)
        gui.Button(label=u'Buscar', name='search', sizer_border=4, top=nTop, left='410', onclick=buscarproductos)
        gui.Button(label=u'Salir', name='close', sizer_border=4, onclick=on_cierra, top=nTop, left='510')
        
        nTop = str(int(nTop)+50)
        gui.Image(name='image_507_571', height='36', left='17', top=nTop, 
			  width='238', filename='sistemas-agiles.png', )
        gui.Image(name='image_33_540', height='50', left='665', top=nTop,
			  width='100', filename='logo-pyafipws.png', )


# --- gui2py designer generated code ends ---


nTop = str(int(nTop)+50)
# obtener referencia a la ventana principal:
mywin = gui.get("abmproductos")
mywin.height = nTop
panel = mywin['ppal']['record']
panel.height = nTopPanel
#mywin['panel']['record'].set_sizer_grow_col(0, 1)

def main():
    
    ExisteProductos()
    mywin.show()

if __name__ == "__main__":
    main()
    gui.main_loop()

