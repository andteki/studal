import wx

from controllers.mainController import MainController

class StudalApp( wx.App ):

    def OnInit( self ):
        
        MainController()
        return True

app = StudalApp( False )
app.MainLoop()