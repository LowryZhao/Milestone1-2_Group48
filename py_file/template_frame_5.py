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

class MyFrame5(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap12 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer15.Add(self.m_bitmap12, 0, wx.ALIGN_LEFT, 5)

        bSizer15.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer15.Add(self.m_button13, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.m_button14, 0, wx.ALL | wx.RIGHT, 5)

        bSizer14.Add(bSizer15, 0, wx.ALL | wx.EXPAND, 5)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer14.Add(self.m_staticText5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        m_comboBox3Choices = [u"Pie Chart", u"Bar Chart", u"Pie Chart & Bar Chart"]
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, u"Pie Chart", wx.DefaultPosition, wx.Size(200, -1),
                                       m_comboBox3Choices, 0)
        self.m_comboBox3.SetSelection(0)
        bSizer14.Add(self.m_comboBox3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"Get Results", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button14.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer14.Add(self.m_button14, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink11 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer16.Add(self.m_hyperlink11, 0, wx.ALL, 5)

        self.m_hyperlink12 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink12.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer16.Add(self.m_hyperlink12, 0, wx.ALL, 5)

        bSizer14.Add(bSizer16, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer14)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button14.Bind(wx.EVT_BUTTON, self.go_to_frame6)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def go_to_frame6(self, event):
        event.Skip()
