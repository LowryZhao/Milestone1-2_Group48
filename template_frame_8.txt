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
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutritional Food Analysis and Visualization", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap15 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer25.Add( self.m_bitmap15, 0, wx.ALIGN_LEFT, 5 )


		bSizer25.Add( ( 0, 0), 1, wx.LEFT, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Settings", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button20, 0, wx.ALL|wx.RIGHT, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button21, 0, wx.ALL|wx.RIGHT, 5 )


		bSizer24.Add( bSizer25, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nutrition Information Plan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer24.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, u"Nutrition Goals:\nxxxxxxxxxxxxxxxxxx\nNutrition Food Item Details:\nxxxxxx\nNutrition Plan Period:", wx.DefaultPosition, wx.Size( 200,90 ), 0 )
		bSizer24.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,20 ), wx.adv.DP_DEFAULT )
		bSizer24.Add( self.m_datePicker1, 0, wx.ALIGN_CENTER, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer24.Add( self.m_button22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button42, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline3.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticline3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer24.Add( self.m_staticline3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button41, 0, wx.ALIGN_CENTER, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_hyperlink21 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer26.Add( self.m_hyperlink21, 0, wx.ALL, 5 )

		self.m_hyperlink22 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer26.Add( self.m_hyperlink22, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer26, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button22.Bind( wx.EVT_BUTTON, self.save_as_csv )
		self.m_button42.Bind( wx.EVT_BUTTON, self.go_to_frame9 )
		self.m_button41.Bind( wx.EVT_BUTTON, self.return_to_frame2 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def save_as_csv( self, event ):
		event.Skip()

	def go_to_frame9( self, event ):
		event.Skip()

	def return_to_frame2( self, event ):
		event.Skip()


