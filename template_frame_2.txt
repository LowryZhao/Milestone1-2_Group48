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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutritional Food Analysis and Visualization", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap9 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer5.Add( self.m_bitmap9, 0, wx.ALIGN_LEFT, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.LEFT, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL|wx.RIGHT, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL|wx.RIGHT, 5 )


		bSizer4.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 0, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nutrition Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Food Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button6.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Nutrition Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button7.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer6.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Nutrition Plan Development and Sharing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer6.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/healthy-plate.jpeg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,150 ), 0 )
		bSizer4.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_hyperlink5 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer7.Add( self.m_hyperlink5, 0, wx.ALL, 5 )

		self.m_hyperlink6 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer7.Add( self.m_hyperlink6, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer7, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.go_to_frame3 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.go_to_frame5 )
		self.m_button8.Bind( wx.EVT_BUTTON, self.go_to_frame7 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def go_to_frame3( self, event ):
		event.Skip()

	def go_to_frame5( self, event ):
		event.Skip()

	def go_to_frame7( self, event ):
		event.Skip()


