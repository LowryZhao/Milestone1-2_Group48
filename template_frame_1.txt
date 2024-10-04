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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nutritional Food Analysis and Visualization", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 60,60 ), 0 )
		bSizer2.Add( self.m_bitmap10, 0, wx.ALIGN_LEFT, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.LEFT, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Settings", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.RIGHT, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.RIGHT, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcome!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), 0, wx.DefaultValidator, u"Enter Email Address or Phone Number" )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,30 ), wx.TE_PASSWORD, wx.DefaultValidator, u"Enter Your Password" )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Show Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetBackgroundColour( wx.Colour( 255, 51, 153 ) )

		bSizer1.Add( self.m_button3, 0, wx.ALIGN_CENTER, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Forgot Password?", u"http://www.wxformbuilder.org", wx.Point( -1,-1 ), wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink1.SetForegroundColour( wx.Colour( 51, 102, 153 ) )

		bSizer1.Add( self.m_hyperlink1, 0, wx.ALIGN_CENTER, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica" ) )
		self.m_staticline1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_hyperlink2 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Sign Up", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1.Add( self.m_hyperlink2, 0, wx.ALIGN_CENTER, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_hyperlink3 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_hyperlink3, 0, wx.ALL, 5 )

		self.m_hyperlink4 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		self.m_hyperlink4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer3.Add( self.m_hyperlink4, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.show_password )
		self.m_button3.Bind( wx.EVT_BUTTON, self.open_next_frame )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def show_password( self, event ):
		event.Skip()

	def open_next_frame( self, event ):
		event.Skip()


