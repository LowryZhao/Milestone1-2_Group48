# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutritional Food Analysis and Visualization", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer12.Add( self.m_bitmap11, 0, wx.ALIGN_LEFT, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.LEFT, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Settings", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button11, 0, wx.ALL|wx.RIGHT, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button12, 0, wx.ALL|wx.RIGHT, 5 )


		bSizer11.Add( bSizer12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nutrition Range Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer11.Add( self.m_staticText4, 0, wx.ALIGN_CENTER, 5 )

		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Select one nutrition", wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox4Choices, 0 )
		bSizer11.Add( self.m_comboBox4, 0, wx.ALIGN_CENTER, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"Enter min_values", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer11.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, u"Enter max_values", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer11.Add( self.m_textCtrl12, 0, wx.ALIGN_CENTER, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_listBox2Choices, 0 )
		bSizer11.Add( self.m_listBox2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Range Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer11.Add( self.m_button13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button34 = wx.Button( self, wx.ID_ANY, u"next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button34, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_hyperlink9 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer13.Add( self.m_hyperlink9, 0, wx.ALL, 5 )

		self.m_hyperlink10 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer13.Add( self.m_hyperlink10, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer13, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button13.Bind( wx.EVT_BUTTON, self.nutrition_range_filter )
		self.m_button34.Bind( wx.EVT_BUTTON, self.go_to_frame6 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def nutrition_range_filter( self, event ):
		event.Skip()

	def go_to_frame6( self, event ):
		event.Skip()


