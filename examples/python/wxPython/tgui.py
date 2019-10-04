# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 31 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 608,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizeMain = wx.BoxSizer( wx.VERTICAL )

		self.lblQuery = wx.StaticText( self, wx.ID_ANY, u"Insert your sql query:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblQuery.Wrap( -1 )

		bSizeMain.Add( self.lblQuery, 0, wx.ALL|wx.EXPAND, 5 )

		bSizerSearch = wx.BoxSizer( wx.HORIZONTAL )

		self.txtSql = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerSearch.Add( self.txtSql, 1, wx.ALL, 5 )

		self.btSearch = wx.Button( self, wx.ID_ANY, u"<b>run</b>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btSearch.SetLabelMarkup( u"<b>run</b>" )
		self.btSearch.SetDefault()
		bSizerSearch.Add( self.btSearch, 0, wx.ALL, 5 )


		bSizeMain.Add( bSizerSearch, 0, wx.EXPAND, 5 )

		self.grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid.CreateGrid( 0, 0 )
		self.grid.EnableEditing( True )
		self.grid.EnableGridLines( True )
		self.grid.EnableDragGridSize( False )
		self.grid.SetMargins( 0, 0 )

		# Columns
		self.grid.EnableDragColMove( False )
		self.grid.EnableDragColSize( True )
		self.grid.SetColLabelSize( 30 )
		self.grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid.EnableDragRowSize( True )
		self.grid.SetRowLabelSize( 80 )
		self.grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizeMain.Add( self.grid, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizeMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btSearch.Bind( wx.EVT_BUTTON, self.runClicked )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def runClicked( self, event ):
		event.Skip()


