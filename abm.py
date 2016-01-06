# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

import wx.lib.agw.flatnotebook as FNB

import gettext
_ = gettext.gettext

###########################################################################
## Class Ppal
###########################################################################

class Ppal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 720,487 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bookStyle = FNB.FNB_NODRAG
		self.Paginas = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, FNB.FNB_TABS_BORDER_SIMPLE )
		self.pagBusqueda = wx.Panel( self.Paginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.pagBusqueda, wx.ID_ANY, _(u"Busqueda"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer8.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.txtBusqueda = wx.TextCtrl( self.pagBusqueda, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.txtBusqueda, 1, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_grid1 = wx.grid.Grid( self.pagBusqueda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer7.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAgrega = wx.BitmapButton( self.pagBusqueda, wx.ID_ANY, wx.Bitmap( u"imagenes/NUEVO_D.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnAgrega.SetBitmapDisabled( wx.Bitmap( u"imagenes/NUEVO_D.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnAgrega.SetBitmapSelected( wx.Bitmap( u"imagenes/NUEVO.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnAgrega.SetBitmapFocus( wx.Bitmap( u"imagenes/NUEVO.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnAgrega.SetBitmapHover( wx.Bitmap( u"imagenes/NUEVO.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnAgrega.SetToolTipString( _(u"Agregar un registro") )
		
		bSizer6.Add( self.btnAgrega, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnEditar = wx.BitmapButton( self.pagBusqueda, wx.ID_ANY, wx.Bitmap( u"imagenes/edit_b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnEditar.SetBitmapDisabled( wx.Bitmap( u"imagenes/edit_b.png", wx.BITMAP_TYPE_ANY ) )
		self.btnEditar.SetBitmapSelected( wx.Bitmap( u"imagenes/edit.png", wx.BITMAP_TYPE_ANY ) )
		self.btnEditar.SetBitmapFocus( wx.Bitmap( u"imagenes/edit.png", wx.BITMAP_TYPE_ANY ) )
		self.btnEditar.SetBitmapHover( wx.Bitmap( u"imagenes/edit.png", wx.BITMAP_TYPE_ANY ) )
		self.btnEditar.SetToolTipString( _(u"Editar el registro seleccionado") )
		
		bSizer6.Add( self.btnEditar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnBorrar = wx.BitmapButton( self.pagBusqueda, wx.ID_ANY, wx.Bitmap( u"imagenes/BORRAR_D.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnBorrar.SetBitmapDisabled( wx.Bitmap( u"imagenes/BORRAR_D.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnBorrar.SetBitmapSelected( wx.Bitmap( u"imagenes/BORRAR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnBorrar.SetBitmapFocus( wx.Bitmap( u"imagenes/BORRAR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnBorrar.SetBitmapHover( wx.Bitmap( u"imagenes/BORRAR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnBorrar.SetToolTipString( _(u"Eliminar el registro seleccionado") )
		
		bSizer6.Add( self.btnBorrar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnSalir = wx.BitmapButton( self.pagBusqueda, wx.ID_ANY, wx.Bitmap( u"imagenes/SALIR_D.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnSalir.SetBitmapDisabled( wx.Bitmap( u"imagenes/SALIR_D.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapSelected( wx.Bitmap( u"imagenes/SALIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapFocus( wx.Bitmap( u"imagenes/SALIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapHover( wx.Bitmap( u"imagenes/SALIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetToolTipString( _(u"Salir del ABM") )
		
		bSizer6.Add( self.btnSalir, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		self.pagBusqueda.SetSizer( bSizer7 )
		self.pagBusqueda.Layout()
		bSizer7.Fit( self.pagBusqueda )
		self.Paginas.AddPage( self.pagBusqueda, _(u"Busqueda"), False, 0 )
		self.pagEdicion = wx.Panel( self.Paginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		self.Paginas.AddPage( self.pagEdicion, _(u"Modificar datos"), True, 0 )
		
		bSizer5.Add( self.Paginas, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtBusqueda.Bind( wx.EVT_CHAR, self.txtBusquedaOnChar )
		self.btnAgrega.Bind( wx.EVT_BUTTON, self.btnAgregaOnButtonClick )
		self.btnEditar.Bind( wx.EVT_BUTTON, self.btnEditarOnButtonClick )
		self.btnBorrar.Bind( wx.EVT_BUTTON, self.btnBorrarOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )

	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtBusquedaOnChar( self, event ):
		event.Skip()
	
	def btnAgregaOnButtonClick( self, event ):
		event.Skip()
	
	def btnEditarOnButtonClick( self, event ):
		event.Skip()
	
	def btnBorrarOnButtonClick( self, event ):
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		event.Skip()
		
	

