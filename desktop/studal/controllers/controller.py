from views.mainForm import MainForm
from views.studentForm import StudentForm
from views.groupForm import GroupForm
from model.studalModel import Model
import wx
import sys

class Controller():

    def __init__( self ):
        print("controller")
        self.model = Model()
        self.mainFrm = MainForm( None, wx.ID_ANY, "" )
        self.studentFrm = StudentForm( None, wx.ID_ANY, "" )
        self.groupFrm = GroupForm( None, wx.ID_ANY, "" )
        self.mainFrm.SetTitle( "Studal" )
        self.mainFrm.Show()
        self.setEventHandlers()
        self.setComboBoxItems()

    def setEventHandlers( self ):
        
        self.mainFrm.searchBtn.Bind( wx.EVT_BUTTON, self.getSearchStudent )
        self.mainFrm.fillStudentsBtn.Bind( wx.EVT_BUTTON, self.getStudents )
        self.mainFrm.manageStudentsBtn.Bind( wx.EVT_BUTTON, self.manageStudents )
        self.mainFrm.manageGroupBtn.Bind( wx.EVT_BUTTON, self.manageGroups )
        self.mainFrm.exitBtn.Bind( wx.EVT_BUTTON, self.closeApplication )

        # self.studentFrm.addStudentBtn.Bind( wx.EVT_BUTTON, self.addStudent )
        # self.studentFrm.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
        # self.studentFrm.deleteStudentBtn.Bind( wx.EVT_BUTTON, self.deleteteStudent )
        # self.studentFrm.cancelBtn.Bind( wx.EVT_BUTTON, self.clearStudentFormTextFields )
        # self.studentFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeStudentForm )

        # self.groupFrm.deleteGroupBtn.Bind( wx.EVT_BUTTON, self.deleteGroup )
        # self.groupFrm.addGroupBtn.Bind( wx.EVT_BUTTON, self.addGroup )
        # self.groupFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeGroupForm )

    def setComboBoxItems( self ):

        comboItems = [ "Szoftver", "Ifra", "Logisztika", "Vám" ]
        self.mainFrm.groupCb.SetItems( comboItems )
        self.mainFrm.groupCb.SetValue( "Csoportok" )

# ====================== start section mainform ============================ #

    def getStudents( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Diákok gomb" )


    def getSearchStudent( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Keresés gomb" )


    def manageStudents( self, event ):
        
        self.studentFrm.Show()


    def manageGroups( self, event ):
        
        self.groupFrm.Show()


# ========================= end section mainform ============================== #

# ========================= start section studentform ========================= #

# ========================= end section studentform =========================== #

# ========================= start section groupform =========================== #

# ========================= end section groupform ============================= #

    def closeApplication( self, event ):
        sys.exit()