###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class PthrottleFrame ( wx.Frame ):
    
    def __init__( self, parent, title, size, data ):
        wx.Frame.__init__ ( self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition, size=size, style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.SetBackgroundColour((166, 166, 166))
        self.dataFrame = data

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer2.SetMinSize( wx.Size( -1,10 ) )
        self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Protothrottle", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0013e43a765677", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer2.Add( ( 0, 20), 0, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl3 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"2100", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer4.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer4.Add( ( 0, 20), 0, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


        bSizer4.Add( ( 0, 20), 0, wx.EXPAND, 5 )


        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Horn", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Horn = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Horn.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.Horn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Bell", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Bell = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Bell.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3.Add( self.Bell, 0, wx.ALL, 5 )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Brake", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31.Wrap( -1 )

        self.m_staticText31.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Brake = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Brake.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31.Add( self.Brake, 0, wx.ALL, 5 )


        bSizer31.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Brk Off", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41.Wrap( -1 )

        self.m_staticText41.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.BrakeOff = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.BrakeOff.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31.Add( self.BrakeOff, 0, wx.ALL, 5 )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31, 0, wx.EXPAND, 5 )

        bSizer311 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer311.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText311 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Aux", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText311.Wrap( -1 )

        self.m_staticText311.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer311.Add( self.m_staticText311, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Aux = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F11", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Aux.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer311.Add( self.Aux, 0, wx.ALL, 5 )


        bSizer311.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText411 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Eng On", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText411.Wrap( -1 )

        self.m_staticText411.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer311.Add( self.m_staticText411, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl211 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl211.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer311.Add( self.m_textCtrl211, 0, wx.ALL, 5 )


        bSizer311.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer311, 0, wx.EXPAND, 5 )

        bSizer312 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer312.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText312 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Eng Off", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText312.Wrap( -1 )

        self.m_staticText312.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer312.Add( self.m_staticText312, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.EngineStop = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.EngineStop.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer312.Add( self.EngineStop, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer312.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText412 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Th Unlock", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText412.Wrap( -1 )

        self.m_staticText412.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer312.Add( self.m_staticText412, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl212 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl212.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer312.Add( self.m_textCtrl212, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer312.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer312, 0, wx.EXPAND, 5 )

        bSizer3121 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer3121.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.RstaticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Rev swap", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.RstaticText.Wrap( -1 )

        self.RstaticText.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3121.Add( self.RstaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ReverseSwap = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.ReverseSwap.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3121.Add( self.ReverseSwap, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3121.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.CStaticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Center", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.CStaticText.Wrap( -1 )

        self.CStaticText.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3121.Add( self.CStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Center = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Center.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3121.Add( self.Center, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3121.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer3121, 0, wx.EXPAND, 5 )

        bSizer3122 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer3122.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText3122 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Alerter", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText3122.Wrap( -1 )

        self.m_staticText3122.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3122.Add( self.m_staticText3122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Alerter = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Alerter.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3122.Add( self.Alerter, 0, wx.ALL, 5 )


        bSizer3122.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText4122 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Compressor", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText4122.Wrap( -1 )

        self.m_staticText4122.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3122.Add( self.m_staticText4122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.Compressor = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.Compressor.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer3122.Add( self.Compressor, 0, wx.ALL, 5 )


        bSizer3122.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer3122, 0, wx.EXPAND, 5 )

        bSizer31221 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31221.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText41221 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Brk Test", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41221.Wrap( -1 )

        self.m_staticText41221.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31221.Add( self.m_staticText41221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.BrakeTest = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.BrakeTest.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31221.Add( self.BrakeTest, 0, wx.ALL, 5 )


        bSizer31221.Add( ( 20, 0), 0, wx.EXPAND, 5 )

        self.m_staticText412211 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText412211.Wrap( -1 )

        self.m_staticText412211.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31221.Add( self.m_staticText412211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer31221.Add( ( 70, 0), 0, wx.EXPAND, 5 )


        bSizer31221.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31221, 0, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer31222 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31222.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31221 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"F. Head", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31221.Wrap( -1 )

        self.m_staticText31221.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31222.Add( self.m_staticText31221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.FHead = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.FHead.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31222.Add( self.FHead, 0, wx.ALL, 5 )


        bSizer31222.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41222 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"F. Ditch", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41222.Wrap( -1 )

        self.m_staticText41222.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31222.Add( self.m_staticText41222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.FDitch = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.FDitch.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31222.Add( self.FDitch, 0, wx.ALL, 5 )


        bSizer31222.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31222, 0, wx.EXPAND, 5 )

        bSizer31223 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31223.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31222 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"F Dim #1", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31222.Wrap( -1 )

        self.m_staticText31222.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31223.Add( self.m_staticText31222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.FDim1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.FDim1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31223.Add( self.FDim1, 0, wx.ALL, 5 )


        bSizer31223.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41223 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"F Dim #2", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41223.Wrap( -1 )

        self.m_staticText41223.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31223.Add( self.m_staticText41223, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.FDim2 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.FDim2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31223.Add( self.FDim2, 0, wx.ALL, 5 )


        bSizer31223.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31223, 0, wx.EXPAND, 5 )

        bSizer31224 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31224.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31223 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"R. Head", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31223.Wrap( -1 )

        self.m_staticText31223.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31224.Add( self.m_staticText31223, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl12223 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl12223.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31224.Add( self.m_textCtrl12223, 0, wx.ALL, 5 )


        bSizer31224.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41224 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"R. Ditch", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41224.Wrap( -1 )

        self.m_staticText41224.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31224.Add( self.m_staticText41224, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl21224 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl21224.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31224.Add( self.m_textCtrl21224, 0, wx.ALL, 5 )


        bSizer31224.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31224, 0, wx.EXPAND, 5 )

        bSizer31225 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31225.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31224 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"R. Dim #1", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31224.Wrap( -1 )

        self.m_staticText31224.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31225.Add( self.m_staticText31224, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl12224 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl12224.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31225.Add( self.m_textCtrl12224, 0, wx.ALL, 5 )


        bSizer31225.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41225 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"R. Dim #2", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41225.Wrap( -1 )

        self.m_staticText41225.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31225.Add( self.m_staticText41225, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl21225 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl21225.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31225.Add( self.m_textCtrl21225, 0, wx.ALL, 5 )


        bSizer31225.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31225, 0, wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer31226 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31226.Add( ( 20, 0), 1, wx.EXPAND, 5 )

        self.m_staticText31225 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Up Button", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText31225.Wrap( -1 )

        self.m_staticText31225.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31226.Add( self.m_staticText31225, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl12225 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl12225.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31226.Add( self.m_textCtrl12225, 0, wx.ALL, 5 )


        bSizer31226.Add( ( 20, 40), 0, wx.EXPAND, 5 )

        self.m_staticText41226 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Dn Button", wx.DefaultPosition, wx.Size( 124,-1 ), 0 )
        self.m_staticText41226.Wrap( -1 )

        self.m_staticText41226.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31226.Add( self.m_staticText41226, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl21226 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_RIGHT )
        self.m_textCtrl21226.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer31226.Add( self.m_textCtrl21226, 0, wx.ALL, 5 )


        bSizer31226.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer31226, 0, wx.EXPAND, 5 )

        self.m_staticline5 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline5, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_button1.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer32.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        self.m_button3.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer32.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer32, 0, wx.EXPAND, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer2 )
        self.m_scrolledWindow1.Layout()
        bSizer2.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


