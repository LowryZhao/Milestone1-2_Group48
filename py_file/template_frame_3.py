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
## Class MyFrame3
###########################################################################

class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap10 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer9.Add(self.m_bitmap10, 0, wx.ALIGN_LEFT, 5)

        bSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button9 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer9.Add(self.m_button9, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_button10, 0, wx.ALL | wx.RIGHT, 5)

        bSizer8.Add(bSizer9, 0, wx.ALL | wx.EXPAND, 5)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer8.Add(self.m_staticText3, 0, wx.ALIGN_CENTER, 5)

        bSizer8.Add((0, 0), 1, wx.ALL, 5)

        self.m_searchCtrl1 = wx.SearchCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.Size(300, -1),
                                             0 | wx.BORDER_DEFAULT, wx.DefaultValidator, u"Search Food Name")
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(False)
        bSizer8.Add(self.m_searchCtrl1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer8.Add(self.m_button11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink7 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer10.Add(self.m_hyperlink7, 0, wx.ALL, 5)

        self.m_hyperlink8 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer10.Add(self.m_hyperlink8, 0, wx.ALL, 5)

        bSizer8.Add(bSizer10, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
