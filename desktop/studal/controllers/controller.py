from views.mainForm import MainForm
from views.studentForm import StudentForm
from views.groupForm import GroupForm
from model.studalModel import Model
import wx
import sys

class Controller():

    def __init__( self ):
        
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
        self.mainFrm.manageStudentsBtn.Bind( wx.EVT_BUTTON, self.setManageStudentsForm )
        self.mainFrm.manageGroupBtn.Bind( wx.EVT_BUTTON, self.setManageGroupsForm )
        self.mainFrm.exitBtn.Bind( wx.EVT_BUTTON, self.closeApplication )

        # self.studentFrm.addStudentBtn.Bind( wx.EVT_BUTTON, self.addStudent )
        # self.studentFrm.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
        # self.studentFrm.deleteStudentBtn.Bind( wx.EVT_BUTTON, self.deleteteStudent )
        # self.studentFrm.cancelBtn.Bind( wx.EVT_BUTTON, self.clearStudentFormTextFields )
        # self.studentFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeStudentForm )

        # self.groupFrm.deleteGroupBtn.Bind( wx.EVT_BUTTON, self.deleteGroup )
        # self.groupFrm.addGroupBtn.Bind( wx.EVT_BUTTON, self.addGroup )
        # self.groupFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeGroupForm )



# ====================== start section mainform ============================ #

    def setComboBoxItems( self ):

        comboItems = self.model.getComboItems()
        self.mainFrm.groupCb.SetItems( comboItems )
        self.mainFrm.groupCb.SetValue( "Csoportok" )

    def setTableProperties( self ):

        columnNames = self.model.getTableCoulumnNames()
        for i in range( 0, len( columnNames )):
            
            self.mainFrm.studentTbl.SetColLabelValue( i, columnNames[ i ])
            

        width, heigth = self.mainFrm.studentTbl.GetSize()
        self.mainFrm.studentTbl.SetColSize( 0, ( width/4 ))
        self.mainFrm.studentTbl.SetColSize( 1, ( width/4 ))
        self.mainFrm.studentTbl.SetColSize( 2, ( width/6 ))
        self.mainFrm.studentTbl.SetColSize( 3, ( width/5 ))


    def getStudents( self, event ):
        
        self.setTableProperties()
        students = self.model.getAllStudentsData()
        for i in range ( 0, len( students )):
            j = 0
            if( i > j ):
                self.mainFrm.studentTbl.AppendRows()
            for data in students[ i ]:
                self.mainFrm.studentTbl.SetCellValue( i, j, data )
                j += 1


    
    def getSearchStudent( self, event ):
        
        self.mainFrm.statusLbl.SetLabel( "Keresés gomb" )

# ========================= end section mainform ============================== #

# ========================= start section studentform ========================= #

    def setManageStudentsForm( self, event ):
        
        comboItems = self.model.getComboItems()
        self.studentFrm.groupCb.SetItems( comboItems )
        self.studentFrm.groupCb.SetValue( "Csoportok" )
        self.studentFrm.Show()


# ========================= end section studentform =========================== #

# ========================= start section groupform =========================== #
    
    def setManageGroupsForm( self, event ):
        
        comboItems = self.model.getComboItems()
        self.groupFrm.groupCb.SetItems( comboItems )
        self.groupFrm.groupCb.SetValue( "Csoportok" )
        self.groupFrm.Show()

# ========================= end section groupform ============================= #

    def closeApplication( self, event ):
        sys.exit()