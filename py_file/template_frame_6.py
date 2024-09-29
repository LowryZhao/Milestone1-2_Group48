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

class MyFrame6(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap13 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer18.Add(self.m_bitmap13, 0, wx.ALIGN_LEFT, 5)

        bSizer18.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer18.Add(self.m_button15, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button16 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.m_button16, 0, wx.ALL | wx.RIGHT, 5)

        bSizer17.Add(bSizer18, 0, wx.ALL | wx.EXPAND, 5)

        bSizer17.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information Visualization", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer17.Add(self.m_staticText6, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer17.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer35 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap18 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/Pie_Chart.jpeg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 200), 0)
        bSizer35.Add(self.m_bitmap18, 0, wx.ALL, 5)

        bSizer35.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bitmap19 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/bar chart.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 200), 0)
        bSizer35.Add(self.m_bitmap19, 0, wx.ALL, 5)

        bSizer17.Add(bSizer35, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button28 = wx.Button(self, wx.ID_ANY, u"Export Report", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button28.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer17.Add(self.m_button28, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer17.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink13 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink13.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer19.Add(self.m_hyperlink13, 0, wx.ALL, 5)

        self.m_hyperlink14 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink14.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer19.Add(self.m_hyperlink14, 0, wx.ALL, 5)

        bSizer17.Add(bSizer19, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer17)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
