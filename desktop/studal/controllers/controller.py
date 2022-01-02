from views.mainForm import MainForm
from views.studentForm import StudentForm
from views.groupForm import GroupForm
from views.loginForm import LoginForm
from model.studalModel import Model
import wx
import sys

class Controller():

    def __init__( self ):
        
        self.loginmode = 0
        self.model = Model()
        self.mainFrm = MainForm( None, wx.ID_ANY, "" )
        self.studentFrm = StudentForm( None, wx.ID_ANY, "" )
        self.groupFrm = GroupForm( None, wx.ID_ANY, "" )
        self.loginFrm = LoginForm( None, wx.ID_ANY, "" )
        self.mainFrm.SetTitle( "Studal" )
        self.mainFrm.Show()
        self.setEventHandlers()
        self.setComboBoxItems()

    def setEventHandlers( self ):
        
        self.mainFrm.searchBtn.Bind( wx.EVT_BUTTON, self.getSearchStudent )
        self.mainFrm.fillStudentsBtn.Bind( wx.EVT_BUTTON, self.getStudents )
        self.mainFrm.loginLogoutBtn.Bind( wx.EVT_BUTTON, self.loginLogout )
        self.mainFrm.manageStudentsBtn.Bind( wx.EVT_BUTTON, self.setManageStudentsForm )
        self.mainFrm.manageGroupBtn.Bind( wx.EVT_BUTTON, self.setManageGroupsForm )
        self.mainFrm.exitBtn.Bind( wx.EVT_BUTTON, self.closeApplication )
        self.mainFrm.loginLogoutBtn.Bind( wx.EVT_BUTTON, self.loginLogout )

        self.loginFrm.loginBtn.Bind( wx.EVT_BUTTON, self.authenticateToApi )
        self.loginFrm.cancelBtn.Bind( wx.EVT_BUTTON, self.clearTextFields )
        self.loginFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeLoginForm )


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

    def clearTextFields( self ):

        self.loginFrm.userNameTf.SetValue( "" )
        self.loginFrm.passwordTf.SetValue( "" )
        self.studentFrm.nameTf.SetValue( "" )
        self.studentFrm.emailTf.SetValue( "" )
        self.studentFrm.phoneTf.SetValue( "" )
        self.studentFrm.bornTf.SetValue( "" )
        self.groupFrm.groupTf.SetValue( "" )

    def getStudents( self, event ):
        
        text = "students"
        self.setTableProperties()
        students = self.model.getStudentsData( text )
        
        for i in range ( 0, len( students )):
            j = 0
            if( i > j ):
                self.mainFrm.studentTbl.AppendRows()
            for j in range( len( students[ i ])):
                self.mainFrm.studentTbl.SetCellValue( i, j, students[ i ][ j ])


    def getSearchStudent( self, event ):
        
        text = "students/search/" + self.mainFrm.searchTf.GetValue()
        self.setTableProperties()
        students = self.model.getStudentsData( text )
        self.mainFrm.studentTbl.ClearGrid()
        for i in range ( 0, len( students )):
            j = 0
            if( i > j ):
                self.mainFrm.studentTbl.AppendRows()
            for j in range( len( students[ i ])):
                self.mainFrm.studentTbl.SetCellValue( i, j, students[ i ][ j ])

    def loginLogout( self, event ):
        
        if( self.loginmode == 0 ):
        
            self.loginFrm.Show()

# ========================= end section mainform ============================== #

# ========================= start section loginform =========================== #

    def authenticateToApi( self, event ):

        if( self.loginmode == 0 ):
            loginData = {}
            loginData[ "name" ] = self.loginFrm.userNameTf.GetValue()
            loginData[ "password" ] = self.loginFrm.passwordTf.GetValue()
            success = self.model.login( loginData )

            if( success ):

                self.mainFrm.statusLbl.SetLabel( "Sikeres bejelentkezés" )
                self.mainFrm.loginLogoutBtn.SetLabel( "Kijelentkezés" )
                self.loginmode = 1

            else:

                self.mainFrm.statusLbl.SetLabel( "Azononosítási hiba" )

        elif( self.loginmode == 1 ):

            success = self.model.logout()

            if( success ):

                self.mainFrm.statusLbl.SetLabel( "Sikeres kijelentkezés" )
                self.loginmode = 0
                self.mainFrm.loginLogoutBtn.SetLabel( "Bejelentkezés" )

            else:

                self.mainFrm.statusLbl.SetLabel( "Kijelentkezési hiba" )


    def disposeLoginForm( self, event ):
        self.loginFrm.Close()
# ========================= end section loginform ============================== #

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