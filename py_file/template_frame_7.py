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
## Class MyFrame7
###########################################################################

class MyFrame7(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap14 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer21.Add(self.m_bitmap14, 0, wx.ALIGN_LEFT, 5)

        bSizer21.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button17 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer21.Add(self.m_button17, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button18 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer21.Add(self.m_button18, 0, wx.ALL | wx.RIGHT, 5)

        bSizer20.Add(bSizer21, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information Report", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer20.Add(self.m_staticText6, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 120), 0)
        bSizer20.Add(self.m_textCtrl3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer20.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button19 = wx.Button(self, wx.ID_ANY, u"Create Nutrition Plan", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button19.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer20.Add(self.m_button19, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.m_staticline2.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica"))
        self.m_staticline2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer20.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink15 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Save", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink15.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer22.Add(self.m_hyperlink15, 0, wx.ALL, 5)

        self.m_hyperlink16 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Download", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink16.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer22.Add(self.m_hyperlink16, 0, wx.ALL, 5)

        self.m_hyperlink17 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Leave", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink17.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer22.Add(self.m_hyperlink17, 0, wx.ALL, 5)

        bSizer20.Add(bSizer22, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink18 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink18.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer23.Add(self.m_hyperlink18, 0, wx.ALL, 5)

        self.m_hyperlink19 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink19.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer23.Add(self.m_hyperlink19, 0, wx.ALL, 5)

        bSizer20.Add(bSizer23, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer20)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
