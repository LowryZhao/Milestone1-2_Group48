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
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutritional Food Analysis and Visualization", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer35.Add( self.m_bitmap18, 0, wx.ALIGN_LEFT, 5 )


		bSizer35.Add( ( 0, 0), 1, wx.LEFT, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"Settings", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer35.Add( self.m_button30, 0, wx.ALL|wx.RIGHT, 5 )

		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_button31, 0, wx.ALL|wx.RIGHT, 5 )


		bSizer34.Add( bSizer35, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nutrition Level Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer34.Add( self.m_staticText12, 0, wx.ALIGN_CENTER, 5 )

		m_comboBox3Choices = [ wx.EmptyString ]
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Choose Nutrient", wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox3Choices, 0 )
		bSizer34.Add( self.m_comboBox3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Choose Level", wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBox2Choices, 0 )
		bSizer34.Add( self.m_comboBox2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_listBox4Choices, 0 )
		bSizer34.Add( self.m_listBox4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Level Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer34.Add( self.m_button32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button38 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button38, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_hyperlink29 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer36.Add( self.m_hyperlink29, 0, wx.ALL, 5 )

		self.m_hyperlink30 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer36.Add( self.m_hyperlink30, 0, wx.ALL, 5 )


		bSizer34.Add( bSizer36, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( bSizer34 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.nutrition_level_filter )
		self.m_button38.Bind( wx.EVT_BUTTON, self.return_to_frame2 )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def nutrition_level_filter( self, event ):
		event.Skip()

	def return_to_frame2( self, event ):
		event.Skip()


