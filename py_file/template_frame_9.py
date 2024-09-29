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
## Class MyFrame9
###########################################################################

class MyFrame9(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap16 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer28.Add(self.m_bitmap16, 0, wx.ALIGN_LEFT, 5)

        bSizer28.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer28.Add(self.m_button23, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button24 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer28.Add(self.m_button24, 0, wx.ALL | wx.RIGHT, 5)

        bSizer27.Add(bSizer28, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information Plan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        self.m_staticText8.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer27.Add(self.m_staticText8, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer27.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY,
                                           u"  Are you interested in \nsharing your health goals \n       with someone?",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetForegroundColour(wx.Colour(255, 51, 153))

        bSizer27.Add(self.m_staticText9, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer27.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer29 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/gmail_icon.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(50, 20), 0)
        bSizer29.Add(self.m_bitmap4, 0, wx.ALL, 5)

        self.m_bitmap5 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/facebook_icon.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(50, 20), 0)
        bSizer29.Add(self.m_bitmap5, 0, wx.ALL, 5)

        self.m_bitmap6 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/wechat.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(50, 20), 0)
        bSizer29.Add(self.m_bitmap6, 0, wx.ALL, 5)

        bSizer27.Add(bSizer29, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button25 = wx.Button(self, wx.ID_ANY, u"Share", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button25.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer27.Add(self.m_button25, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_hyperlink23 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Others", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink23.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer27.Add(self.m_hyperlink23, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.m_staticline4.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica"))
        self.m_staticline4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer27.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        self.m_hyperlink24 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Download", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink24.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer27.Add(self.m_hyperlink24, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink25 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink25.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer30.Add(self.m_hyperlink25, 0, wx.ALL, 5)

        self.m_hyperlink26 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink26.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer30.Add(self.m_hyperlink26, 0, wx.ALL, 5)

        bSizer27.Add(bSizer30, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer27)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
