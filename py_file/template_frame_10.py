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
## Class MyFrame10
###########################################################################

class MyFrame10(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        bSizer32 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap17 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer32.Add(self.m_bitmap17, 0, wx.ALIGN_LEFT, 5)

        bSizer32.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button26 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer32.Add(self.m_button26, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button27 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer32.Add(self.m_button27, 0, wx.ALL | wx.RIGHT, 5)

        bSizer31.Add(bSizer32, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information Plan", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        self.m_staticText10.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer31.Add(self.m_staticText10, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Successfully Share!", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText11.Wrap(-1)

        self.m_staticText11.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))
        self.m_staticText11.SetForegroundColour(wx.Colour(255, 51, 153))

        bSizer31.Add(self.m_staticText11, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bitmap7 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/diet_plan.jpeg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(200, 150), 0)
        bSizer31.Add(self.m_bitmap7, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer31.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink27 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink27.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer33.Add(self.m_hyperlink27, 0, wx.ALL, 5)

        self.m_hyperlink28 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink28.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer33.Add(self.m_hyperlink28, 0, wx.ALL, 5)

        bSizer31.Add(bSizer33, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer31)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
