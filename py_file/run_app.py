import wx
import wx.xrc
import wx.adv
import matplotlib.pyplot as plt

from template_frame_1 import MyFrame1 as MyFrame1
from template_frame_2 import MyFrame2 as MyFrame2
from template_frame_3 import MyFrame3 as MyFrame3
from template_frame_4 import MyFrame4 as MyFrame4
from template_frame_5 import MyFrame5 as MyFrame5
from template_frame_6 import MyFrame6 as MyFrame6
from template_frame_7 import MyFrame7 as MyFrame7


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap10 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer2.Add(self.m_bitmap10, 0, wx.ALIGN_LEFT, 5)

        bSizer2.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL | wx.RIGHT, 5)

        bSizer1.Add(bSizer2, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Welcome!", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer1.Add(self.m_staticText1, 0, wx.ALIGN_CENTER, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 30), 0,
                                       wx.DefaultValidator, u"Enter Email Address or Phone Number")
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        # Hide password function by adding command "wx.TE_PASSWORD".

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 30),
                                       wx.TE_PASSWORD, wx.DefaultValidator, u"Enter Your Password")
        bSizer1.Add(self.m_textCtrl2, 0, wx.ALIGN_CENTER, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer1.Add(self.m_button3, 0, wx.ALIGN_CENTER, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_hyperlink1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Forgot Password?", u"http://www.wxformbuilder.org",
                                                 wx.Point(-1, -1), wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink1.SetForegroundColour(wx.Colour(51, 102, 153))

        bSizer1.Add(self.m_hyperlink1, 0, wx.ALIGN_CENTER, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        self.m_staticline1.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Helvetica"))
        self.m_staticline1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_hyperlink2 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Sign Up", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer1.Add(self.m_hyperlink2, 0, wx.ALIGN_CENTER, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink3 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer3.Add(self.m_hyperlink3, 0, wx.ALL, 5)

        self.m_hyperlink4 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer3.Add(self.m_hyperlink4, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.open_next_frame)

    # Function 1 (Feature 1): Press "Login" button go to next frame.
    def open_next_frame(self, event):
        next_frame = MyFrame2(None)
        next_frame.Show()
        self.Hide()


class MyFrame2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap9 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer5.Add(self.m_bitmap9, 0, wx.ALIGN_LEFT, 5)

        bSizer5.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button4, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL | wx.RIGHT, 5)

        bSizer4.Add(bSizer5, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add((0, 0), 0, wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Food Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button6.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer6.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"Nutrition Filter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer6.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Nutrition Plan Development and Sharing", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.m_button8.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer6.Add(self.m_button8, 0, wx.ALL, 5)

        bSizer4.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/healthy-plate.jpeg", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(200, 150), 0)
        bSizer4.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink5 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer7.Add(self.m_hyperlink5, 0, wx.ALL, 5)

        self.m_hyperlink6 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer7.Add(self.m_hyperlink6, 0, wx.ALL, 5)

        bSizer4.Add(bSizer7, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.go_to_frame3)
        self.m_button7.Bind(wx.EVT_BUTTON, self.go_to_frame4)
        self.m_button8.Bind(wx.EVT_BUTTON, self.go_to_frame7)


    # Function 2 (Feature 2): Press "Food Search" button go to frame3.
    def go_to_frame3(self, event):
        next_frame_2 = MyFrame3(None)
        next_frame_2.Show()
        self.Hide()

    # Function 3 (Feature 3): Press "Nutrition Filter" button go to frame4.
    def go_to_frame4(self, event):
        next_frame_4 = MyFrame4(None)
        next_frame_4.Show()
        self.Close()

    # Function 4 (Feature 4): Press "Nutrition Plan Development and Sharing" button go to frame7.
    def go_to_frame7(self, event):
        next_frame_7 = MyFrame7(None)
        next_frame_7.Show()
        self.Close()

class MyFrame4(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Nutritional Food Analysis and Visualization",
                          pos=wx.DefaultPosition, size=wx.Size(500, 360),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap11 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Img/logo.png", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(60, 60), 0)
        bSizer12.Add(self.m_bitmap11, 0, wx.ALIGN_LEFT, 5)

        bSizer12.Add((0, 0), 1, wx.LEFT, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Settings", wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer12.Add(self.m_button11, 0, wx.ALL | wx.RIGHT, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"Sign Up/Login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button12, 0, wx.ALL | wx.RIGHT, 5)

        bSizer11.Add(bSizer12, 0, wx.ALL | wx.EXPAND, 5)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Nutrition Information", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Helvetica"))

        bSizer11.Add(self.m_staticText4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        m_comboBox1Choices = [u"Minimum", u"Maximum"]
        self.m_comboBox1 = wx.ComboBox(self, wx.ID_ANY, u"Choose Nutrition Range Filter", wx.DefaultPosition,
                                       wx.Size(200, 50), m_comboBox1Choices, 0)
        bSizer11.Add(self.m_comboBox1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        m_comboBox2Choices = [u"Low", u"Medium", u"High"]
        self.m_comboBox2 = wx.ComboBox(self, wx.ID_ANY, u"Choose Nutrition Level Filter", wx.DefaultPosition,
                                       wx.Size(200, 50), m_comboBox2Choices, 0)
        bSizer11.Add(self.m_comboBox2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button13.SetBackgroundColour(wx.Colour(255, 51, 153))

        bSizer11.Add(self.m_button13, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_hyperlink9 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Contact", u"http://www.wxformbuilder.org",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink9.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer13.Add(self.m_hyperlink9, 0, wx.ALL, 5)

        self.m_hyperlink10 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"IT Support", u"http://www.wxformbuilder.org",
                                                  wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        self.m_hyperlink10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer13.Add(self.m_hyperlink10, 0, wx.ALL, 5)

        bSizer11.Add(bSizer13, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button13.Bind(wx.EVT_BUTTON, self.go_to_frame5)

    def go_to_frame5(self, event):
        next_frame_5 = MyFrame5(None)
        next_frame_5.Show()
        self.Close()


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

    # Function 5 (Feature 5): Press "Get Results" button go to frame6.
    def go_to_frame6(self, event):
        next_frame_6 = MyFrame6(None)
        next_frame_6.Show()
        self.Close()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    # frame_2 = MyFrame2(None)
    frame.Show()
    app.MainLoop()
