from views.mainForm import MainForm
import wx
import sys

class ViewController:

    def __init__( self ):

        self.mainFrm = MainForm( None, wx.ID_ANY, "" )
        self.mainFrm.SetTitle( "Studal" )
        self.mainFrm.Show()
        self.eventHandlers()
        self.setComboBoxItems()

    def eventHandlers( self ):
        
        self.mainFrm.searchBtn.Bind( wx.EVT_BUTTON, self.getSearchStudent )
        self.mainFrm.fillStudentsBtn.Bind( wx.EVT_BUTTON, self.getStudents )
        self.mainFrm.newStudentBtn.Bind( wx.EVT_BUTTON, self.setNewStudent )
        self.mainFrm.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
        self.mainFrm.newGroupBtn.Bind( wx.EVT_BUTTON, self.setNewGroup )
        self.mainFrm.modifyGroupBtn.Bind( wx.EVT_BUTTON, self.modifyGroup )
        self.mainFrm.exitBtn.Bind( wx.EVT_BUTTON, self.closeApplication )

    def setComboBoxItems( self ):

        comboItems = [ "Szoftver", "Ifra", "Logisztika", "Vám" ]
        self.mainFrm.groupCb.SetItems( comboItems )
        self.mainFrm.groupCb.SetValue( "Csoportok" )
    def getStudents( self ):
        pass

    def getSearchStudent( self ):
        pass

    def setNewStudent( self ):
        pass

    def modifyStudent( self ):
        pass

    def setNewGroup( self ):
        pass

    def modifyGroup( self ):
        pass

    def closeApplication( self ):
        sys.exit()