#!/usr/bin/python
# -*- coding: utf-8 -*-
"Aplicativo Factura Electronica Libre"
"Busqueda en el padron de contribuyentes"

__author__ = "Jose Oscar Vogel (oscarvogel@gmail.com)"
__copyright__ = "Copyright (C) 2015- Jose Oscar Vogel"
__license__ = "GPL 3.0+"
__version__ = "0.1a"

import gui
import datos
from pyafipws.padron import PadronAFIP

def on_tipo_doc_change(evt):
    ctrl = evt.target
    value = ""
    if ctrl.value == 80:
        mask = '##-########-#'
    elif ctrl.value == 99:
        mask = '#'
        value = "0"
        #on_nro_doc_change(evt)
    else:
        mask = '########'
    panel['criterios']['nro_doc'].mask = mask
    panel['criterios']['nro_doc'].value = value
    
def on_busqueda(evt):
    padron = PadronAFIP()
    ctrl = evt.target
    listado = panel['listado']
    listado.items.clear()
    criterios = panel['criterios']
    tipo_doc = criterios['tipo_doc'].value
    nro_doc = criterios['nro_doc'].value.replace('-', '').strip()
    nombre = criterios['nombre_cliente'].value
    
    if ctrl.name.startswith('nro_doc'):
        sql = "select * from padron where tipo_doc = ? and nro_doc like '%" + nro_doc + "%'"
        params = [tipo_doc, ]
        padron.cursor.execute(sql, params)
    else:
        sql = "select * from padron where lower(denominacion) like '%" + nombre + "%'"
        padron.cursor.execute(sql)
        
    datos = padron.cursor.fetchall()
    
    items = []
    for dato in datos:
        items.append([str(dato['tipo_doc']), str(dato['nro_doc']), dato['denominacion']])
    
    listado.items = items
    
# --- gui2py designer generated code starts ---
with gui.Window(name='buscapadron', 
                title=u'Aplicativo Facturaci\xf3n Electr\xf3nica', 
                resizable=True, height='636px', left='181', top='52', 
                width='794px', image=''):
    with gui.Panel(label=u'', name='panelbusqueda', 
				   image='', sizer_border=5, height='500', left='8', top='6', width='633',):
        
        nTop = '10'
        with gui.Panel(label=u'Criterios de B\xfasqueda:', name='criterios', 
                       height='80', left='6', top=nTop, width='778', 
                       bgcolor=u'#F9F9F8', fgcolor=u'#4C4C4C', image='', ):
            nTop = str(int(nTop)+30)						   
            gui.Label(name='label_182_163', height='21', left='16', top='31', 
                      width='38', text=u'Cliente:', )
            gui.ComboBox(name='tipo_doc', text=u'CF', left='75', top='23', 
                         width='78', onchange=on_tipo_doc_change, 
                         items=datos.TIPO_DOC_MAP, 
                         selection=3, )
            gui.TextBox(mask='##-########-#', name='nro_doc', left='164', 
                        top='24', width='110', text=u'', 
                        value=u'', onchange=on_busqueda)
            gui.Label(name='label_268_164', height='31', left='295', top='28', 
                      width='61', text=u'Nombre:', )
            gui.TextBox(name='nombre_cliente', left='367', top='23', 
                        width='240', value=u'', onchange=on_busqueda)        
        
        nTop = str(int(nTop)+80)
        with gui.ListView(name='listado', height='353', left='7', top=nTop, 
                          width='775', item_count=0, sort_column=-1, ):
            gui.ListColumn(name=u'tipo_doc', text='Tipo Doc', width=50)
            gui.ListColumn(name=u'nro_doc', text='Nro Doc', width=100, 
                           represent="%s", align="right")
            gui.ListColumn(name=u'nombre_cliente', text='Cliente', width=150)
            							  
        gui.Button(label=u'Salir', name='close', sizer_border=4, 
                   top=nTop, left='510')
        
    
        gui.Image(name='imgsistema', height='36', left='17', top=nTop, 
			  width='238', filename='sistemas-agiles.png', )
        gui.Image(name='imgpyafip', height='50', left='665', top=nTop,
			  width='100', filename='logo-pyafipws.png', )
    
    gui.StatusBar(name='statusbar_15_91', 
                  text=u'Servicio Web Factura Electr\xf3nica mercado interno (WSFEv1)', )


# --- gui2py designer generated code ends ---

			  
mywin = gui.get("buscapadron")
panel = mywin['panelbusqueda']
panel['imgsistema'].top = str(int(mywin.height[:-2]) - 50)
panel['imgpyafip'].top = str(int(mywin.height[:-2]) - 80)

def main():
    mywin.show()

if __name__ == "__main__":
    main()
    gui.main_loop()
