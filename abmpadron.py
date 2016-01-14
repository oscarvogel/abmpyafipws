#!/usr/bin/python
# -*- coding: utf-8 -*-
"Aplicativo Factura Electronica Libre"

__author__ = "Jose Oscar Vogel (oscarvogel@gmail.com)"
__copyright__ = "Copyright (C) 2015- Jose Oscar Vogel"
__license__ = "GPL 3.0+"
__version__ = "0.7c"

import gui          # import gui2py package (shortcuts)
import os
import sys
import sqlite3
import datos
from pyafipws.padron import PadronAFIP
from ConfigParser import SafeConfigParser

# set default locale to handle correctly numeric format (maskedit):
import wx, locale
if sys.platform == "win32":
    locale.setlocale(locale.LC_ALL, 'Spanish_Argentina.1252')
elif sys.platform == "linux2":
    locale.setlocale(locale.LC_ALL, 'es_AR.utf8')
loc = wx.Locale(wx.LANGUAGE_DEFAULT, wx.LOCALE_LOAD_DEFAULT)

padron = PadronAFIP()
CONFIG_FILE = "rece.ini"
DB = None
GANANCIAS = {'NI':u'No Inscripto',
			'AC':u'Activo',
			'EX':u'Exento',
			'NC':u'No Corresponde',}

IMP_IVA = {'NI': 'No Inscripto',
           'AC': 'Activo',
           'EX': 'Exento',
           'NA': 'No alcanzado',
           'XN': 'Exento no alcanzado',
           'AN': 'Activo no alcanzado',
           'NC': 'No corresponde',}

MONOTRIBUTO = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

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
    panel['nro_doc'].mask = mask
    panel['nro_doc'].value = value

def on_nro_doc_change(evt):
    ctrl = panel['nro_doc']
    doc_nro = ctrl.value
    tipo_doc = panel['tipo_doc'].value
    cat_iva = None
    if doc_nro:
        doc_nro = doc_nro.replace("-", "")
        if padron.Buscar(doc_nro, tipo_doc):
            panel['nombre'].value = padron.denominacion
            panel['domicilio'].value = ""
            panel['ganancias'].value = padron.imp_ganancias
            panel['intsociedad'].value = False if padron.integrante_soc == 'N' else True
            panel['empleador'].value = False if padron.empleador == 'N' else True
            panel['monotributo'].value = padron.monotributo if padron.monotributo != 'NI' else None
            panel['impiva'].value = padron.imp_iva
            try:
                cat_iva = int(padron.cat_iva)
            except ValueError:
                cat_iva = None
            if cat_iva:
                pass
            elif padron.imp_iva in ('AC', 'S'):
                cat_iva = 1  # RI
            elif padron.imp_iva == 'EX':
                cat_iva = 4  # EX
            elif padron.monotributo:
                cat_iva = 6  # MT
            else:
                cat_iva = 5  # CF
            padron.ConsultarDomicilios(doc_nro, tipo_doc)
            # tomar el primer domicilio o consultar con la API de AFIP:
            for domicilio in padron.domicilios:
                panel['domicilio'].value = domicilio
                break
            else:
                if doc_nro and padron.Consultar(doc_nro) and padron.domicilios:
                    panel['domicilio'].value = padron.domicilios[0]
            panel['email'].value = padron.email or ""
    else:
        panel['nombre'].value = ""
        panel['domicilio'].value = ""
        panel['email'].value = ""
        panel['ganancias'].value = 'NI'
        panel['monotributo'].value = ""
        panel['intsociedad'].value = False
        panel['empleador'].value = False
        panel['impiva'].value = 'NI'
    panel['cat_iva'].value = cat_iva

def actualizar(evt):
    "Agregar o actualizar los datos del cliente"
    nro_doc = panel['nro_doc'].value.replace('-','')
    tipo_doc = panel['tipo_doc'].value
    denominacion = panel['nombre'].value
    cat_iva = panel['cat_iva'].value
    direccion = panel['domicilio'].value
    email = panel['email'].value
    imp_ganancias = panel['ganancias'].value
    imp_iva = panel['impiva'].value
    monotributo = panel['monotributo'].value if cat_iva == 6 else 'NI'
    integrante_soc = 'S' if panel['intsociedad'].value else 'N'
    empleador = 'S' if panel['empleador'].value else 'N'
	
    if padron.Guardar(tipo_doc, nro_doc, denominacion, cat_iva, 
                     direccion, email, imp_ganancias, imp_iva,
                     monotributo, integrante_soc, empleador):
        gui.alert(u"Se ha guardado la informacion correctamente")
    else:
        gui.alert(u"Se ha producido un errror y no se guardo la informacion")

def borrar(evt):
    "Borrar un dato del padron"
    nro_doc = panel['nro_doc'].value.replace('-','')
    tipo_doc = panel['tipo_doc'].value
    if not gui.confirm(u"¿Se borraran los datos del padron?", "Borrar"):
        return 
    else:
        sql = "delete from domicilio where nro_doc=? and tipo_doc=?"
        parametros = [nro_doc, tipo_doc]
        try:
            padron.cursor.execute(sql, parametros)
        except lite.Error, e:
            print "Error %s:" % e.args[0]
        
        sql = "delete from padron where nro_doc=? and tipo_doc=?"
        parametros = [nro_doc, tipo_doc]
        padron.cursor.execute(sql, parametros)

def limpiar(evt):
    "Limpia lo scampos para cargar un nuevo dato en el padron"
    panel['nro_doc'].value = ""
    panel['nombre'].value = ""
    panel['domicilio'].value = ""
    panel['cat_iva'].value = 1
    panel['email'].value = ""
    
def ExistePadron():
    try:
        padron.cursor.execute("select * from padron")
    except:
        padron.cursor.execute("CREATE TABLE padron ("
                        "nro_doc INTEGER, "
                        "denominacion VARCHAR(30), "
                        "imp_ganancias VARCHAR(2), "
                        "imp_iva VARCHAR(2), "
                        "monotributo VARCHAR(1), "
                        "integrante_soc VARCHAR(1), "
                        "empleador VARCHAR(1), "
                        "actividad_monotributo VARCHAR(2), "
                        "tipo_doc INTEGER, "
                        "cat_iva INTEGER DEFAULT NULL, "
                        "email VARCHAR(250), "
                        "PRIMARY KEY (tipo_doc, nro_doc)"
                      ");")
def ExisteDomicilio():
    try:
        padron.cursor.execute("select * from domicilio")
    except:
        padron.cursor.execute("CREATE TABLE domicilio ("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "tipo_doc INTEGER, "
                        "nro_doc INTEGER, "
                        "direccion TEXT, "
                        "FOREIGN KEY (tipo_doc, nro_doc) REFERENCES padron "
                      ");")

		
# --- gui2py designer generated code starts ---

with gui.Window(name='abmpadron', 
                title=u'Aplicativo Facturaci\xf3n Electr\xf3nica', 
                resizable=True, height='636px', left='181', top='52', 
                width='794px', image=''):
    gui.StatusBar(name='statusbar_15_91', 
                  text=u'Servicio Web Factura Electr\xf3nica mercado interno (WSFEv1)', )
    with gui.Panel(label=u'', name='ppal'):
        with gui.Panel(label=u'', name='record', 
				   image='', sizer_border=5, height='500', left='8', top='6', width='633',):
            nTop = '10'
            gui.Label(name='lblDoc', text=u'Documento:', width='96', top=nTop)
            gui.ComboBox(name='tipo_doc', text=u'CF', 
                         left='100', top='10', width='78', 
                         value=80, 
                         onchange=on_tipo_doc_change,
                         items=datos.TIPO_DOC_MAP, )
            gui.TextBox(mask='##-########-#', name='nro_doc', 
					width='110', 
					onblur=on_nro_doc_change,
					top=nTop, left='200')
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblDeno', text=u'Denominacion:', width='100', top=nTop,)
            gui.TextBox(name='nombre', 
					width='400', 
					value=u'',
					top=nTop, left='100'
					)

            nTop = str(int(nTop)+30)
            gui.Label(name='lblDom', text=u'Domicilio:', width='100', top=nTop,)
            gui.TextBox(name='domicilio', 
					width='400', 
					value=u'',
					top=nTop, left='100'
					)
           
            nTop = str(int(nTop)+30)
            gui.Label(name='label_182_163', height='25', width='50', 
				  text=u'Ganancias:', top=nTop)
            gui.ComboBox(name='ganancias', text=u'CF', 
					 width='150', 
					 items=GANANCIAS, 
					 top=nTop, left='100')
					 
            nTop = str(int(nTop)+30)
            gui.Label(name='label_530_167_1258', height='17', 
                      top=nTop, width='58', text=u'IVA:', )
            gui.ComboBox(name='cat_iva', text=u'Responsable Inscripto', 
                         left='100', top=nTop, width='190', editable=False,
                         items={1: u"Responsable Inscripto", 4: u"Exento", 
                                5: u"Consumidor Final", 6: u"Monotributo",
                                8: u"Proveedor del Exterior",
                                9: u"Cliente del Exterior",
                                10: u"IVA Liberado - Ley Nº 19.640",
                                12: u"Pequeño Contribuyente Eventual",
                                13: u"Monotributista Social",
                                14: u"Pequeño Contribuyente Eventual Social",
                                15: u"IVA No Alcanzado"}, 
                         )	
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblImpIVA', height='25', width='50', 
				  text=u'Imp IVA:', top=nTop)
            gui.ComboBox(name='impiva', 
					 width='150', 
					 items=IMP_IVA, 
					 top=nTop, left='100')
            gui.Label(name='lblMono', height='25', width='50', left='270',
				  text=u'Monotributo:', top=nTop)
            gui.ComboBox(name='monotributo', 
					 width='50', 
					 items=MONOTRIBUTO, 
					 top=nTop, left='350')
            gui.CheckBox(label=u'Empleador', name='empleador', left='420',
                         top=nTop, width='80', value=False, 
                         )
            gui.CheckBox(label=u'Int. Sociedad', name='intsociedad', left='500',
                         top=nTop, width='110', value=False, 
                         )
            
            nTop = str(int(nTop)+30)
            gui.Label(name='lblEmail', height='25', width='50', 
				  text=u'EMail:', top=nTop)
            gui.TextBox(name='email', left='100', top=nTop, 
                        width='400', value=u'', )

        nTopPanel = str(int(nTop)+30)
        nTop = str(int(nTop)+50)
        
        gui.Button(label=u'Crear', name='create', sizer_border=4, top=nTop, left='10', onclick=limpiar)
        gui.Button(label=u'Recuperar', name='retrieve', sizer_border=4, top=nTop, left='110')
        gui.Button(label=u'Actualizar', name='update', sizer_border=4, top=nTop, left='210', onclick=actualizar)
        gui.Button(label=u'Borrar', name='delete', sizer_border=4, top=nTop, left='310', onclick=borrar)
        gui.Button(label=u'Buscar', name='search', sizer_border=4, top=nTop, left='410')
        gui.Button(label=u'Salir', name='close', sizer_border=4, onclick='exit()', top=nTop, left='510')
        
        nTop = str(int(nTop)+50)
        gui.Image(name='image_507_571', height='36', left='17', top=nTop, 
			  width='238', filename='sistemas-agiles.png', )
        gui.Image(name='image_33_540', height='50', left='665', top=nTop,
			  width='100', filename='logo-pyafipws.png', )


# --- gui2py designer generated code ends ---

nTop = str(int(nTop)+50)
# obtener referencia a la ventana principal:
mywin = gui.get("abmpadron")
mywin.height = nTop
panel = mywin['ppal']['record']
panel.height = nTopPanel
#mywin['panel']['record'].set_sizer_grow_col(0, 1)

def main():
    
    ExistePadron()
    ExisteDomicilio()
    mywin.show()

if __name__ == "__main__":
    main()
    padron = PadronAFIP()
    #padron.Guardar("80", "30999157315", "MUNICIPALIDAD DE GARUHAPE", "4", "AV. LAS AMERICAS S/N", "munigaruhape@prico.com.ar")
    print padron.InstallDir
    ok = padron.Buscar("20233472035")
    if ok:
        print "Denominacion:", padron.denominacion
    else:
        print "No encontrado"
    gui.main_loop()
