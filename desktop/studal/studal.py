import wx

from controllers.controller import Controller

class StudalApp( wx.App ):

    def OnInit( self ):
        
        Controller()
        return True

app = StudalApp( False )
app.MainLoop()