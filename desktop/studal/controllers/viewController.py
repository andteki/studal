#from controllers.mainController import MainController
from views.mainForma import MainForm
import wx
import sys

class ViewController():

    def __init__( self ):

        self.mainFrm = MainForm( None, wx.ID_ANY, "" )
        self.mainFrm.SetTitle( "Studal" )
        self.mainFrm.Show()
        self.setEventHandlers()
        self.setComboBoxItems()

    def setEventHandlers( self ):
        
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


    def getStudents( self, event ):
        # super().getAllStudent()
        self.mainFrm.statusLbl.SetLabel( "Diákok gomb" )


    def getSearchStudent( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Keresés gomb" )


    def setNewStudent( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Új diák gomb" )


    def modifyStudent( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Diákok szerkesztése gomb" )


    def setNewGroup( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Új csoport gomb" )


    def modifyGroup( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Csoportok szerkesztése gomb" )
        

    def closeApplication( self, event ):
        sys.exit()