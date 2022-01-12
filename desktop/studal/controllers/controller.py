from views.mainForm import MainForm
from views.studentForm import StudentForm
from views.groupForm import GroupForm
from views.loginForm import LoginForm
from model.studalModel import Model
from model.student import Student
from model.comboItem import ComboItem
import wx
import sys

class Controller():

    def __init__( self ):
        
        self.loginmode = 0
        self.students = []
        self.comboItems = []
        self.model = Model()
        self.mainFrm = MainForm( None, wx.ID_ANY, "" )
        # self.studentFrm = StudentForm( None, wx.ID_ANY, "" )
        # self.groupFrm = GroupForm( None, wx.ID_ANY, "" )
        self.loginFrm = LoginForm( None, wx.ID_ANY, "" )
        self.mainFrm.SetTitle( "Studal" )
        self.mainFrm.Show()
        self.setEventHandlers()
        self.setComboBoxItems()

    def setEventHandlers( self ):
        
        self.mainFrm.searchBtn.Bind( wx.EVT_BUTTON, self.getSearchStudent )
        self.mainFrm.fillStudentsBtn.Bind( wx.EVT_BUTTON, self.getStudents )
        self.mainFrm.loginLogoutBtn.Bind( wx.EVT_BUTTON, self.loginLogout )
        self.mainFrm.saveStudentBtn.Bind( wx.EVT_BUTTON, self.saveStudent )
        self.mainFrm.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
        self.mainFrm.deleteStudentBtn.Bind( wx.EVT_BUTTON, self.deleteStudent )
        self.mainFrm.saveGroupBtn.Bind( wx.EVT_BUTTON, self.saveGroup )
        self.mainFrm.deleteGroupBtn.Bind( wx.EVT_BUTTON, self.deleteGroup )
        self.mainFrm.exitBtn.Bind( wx.EVT_BUTTON, self.closeApplication )

        self.loginFrm.loginBtn.Bind( wx.EVT_BUTTON, self.authenticateToApi )
        self.loginFrm.cancelBtn.Bind( wx.EVT_BUTTON, self.clearTextFields )
        self.loginFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeLoginForm )


        # self.studentFrm.addStudentBtn.Bind( wx.EVT_BUTTON, self.addStudentToApi )
        # self.studentFrm.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
        # self.studentFrm.deleteStudentBtn.Bind( wx.EVT_BUTTON, self.deleteteStudent )
        # self.studentFrm.cancelBtn.Bind( wx.EVT_BUTTON, self.clearStudentFormTextFields )
        # self.studentFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeStudentForm )

        # self.groupFrm.deleteGroupBtn.Bind( wx.EVT_BUTTON, self.deleteGroup )
        # self.groupFrm.addGroupBtn.Bind( wx.EVT_BUTTON, self.addGroup )
        # self.groupFrm.exitBtn.Bind( wx.EVT_BUTTON, self.disposeGroupForm )



# ====================== start section mainform ============================ #

    def setComboBoxItems( self ):
        
        content = self.model.getComboItems()
        
        for item in content:

            cItem = ComboItem()
            cItem.id = str( item[ "id" ])
            cItem.group = item[ "classgroup" ]
            self.comboItems.append( cItem )

        cItems = []
        for item in self.comboItems:

            cItems.append( item.group )

        self.mainFrm.groupCb.SetItems( cItems )
        self.mainFrm.groupCb.SetValue( "Csoportok" )

    def setTableProperties( self ):

        columnNames = self.model.getTableCoulumnNames()
        for i in range( 0, len( columnNames )):
            
            self.mainFrm.studentTbl.SetColLabelValue( i, columnNames[ i ])
            
        width, heigth = self.mainFrm.studentTbl.GetSize()
        self.mainFrm.studentTbl.SetColSize( 0, ( width/4 ))
        self.mainFrm.studentTbl.SetColSize( 1, ( width/4 ))
        self.mainFrm.studentTbl.SetColSize( 2, ( width/6 ))
        self.mainFrm.studentTbl.SetColSize( 3, ( width/6 ))

    def clearTextFields( self, event ):

        self.loginFrm.userNameTf.SetValue( "" )
        self.loginFrm.passwordTf.SetValue( "" )
        # self.studentFrm.nameTf.SetValue( "" )
        # self.studentFrm.emailTf.SetValue( "" )
        # self.studentFrm.phoneTf.SetValue( "" )
        # self.studentFrm.bornTf.SetValue( "" )
        # self.groupFrm.groupTf.SetValue( "" )

    def convertResponseToList( self, content ):

        self.students = []
        for stu in content:
            student = Student()
            student.id = str( stu[ "id" ])
            student.name = stu[ "name" ]
            student.email = stu[ "email" ]
            student.phone = stu[ "phone" ]
            student.borndate = stu[ "borndate" ]
            
            self.students.append( student )

    def getStudents( self, event ):
        
        comboId = 0
        for combo in self.comboItems:
            if( combo.group == self.mainFrm.groupCb.GetValue() ):
                comboId = combo.id

        text = "students/groups/" + comboId
        self.setTableProperties()
        content = self.model.getStudentsData( text )
        self.convertResponseToList( content )

        row = 0
        for student in self.students:
            
            self.mainFrm.studentTbl.SetCellValue( row, 0, student.name )
            self.mainFrm.studentTbl.SetCellValue( row, 1, student.email )
            self.mainFrm.studentTbl.SetCellValue( row, 2, student.phone )
            self.mainFrm.studentTbl.SetCellValue( row, 3, student.borndate )
            self.mainFrm.studentTbl.AppendRows()
            row += 1

    
    def getSearchStudent( self, event ):
        
        text = "students/search/" + self.mainFrm.searchTf.GetValue()
        self.setTableProperties()
        content = self.model.getStudentsData( text )
        self.mainFrm.studentTbl.ClearGrid()

        row = 0
        for student in self.students:
            
            self.mainFrm.studentTbl.SetCellValue( row, 0, student.name )
            self.mainFrm.studentTbl.SetCellValue( row, 1, student.email )
            self.mainFrm.studentTbl.SetCellValue( row, 2, student.phone )
            self.mainFrm.studentTbl.SetCellValue( row, 3, student.borndate )
            self.mainFrm.studentTbl.AppendRows()
            row += 1

    
    def loginLogout( self, event ):
        
        if( self.loginmode == 0 ):
        
            self.loginFrm.Show()

        else:
            
            success = self.model.logout()

            if( success ):

                self.mainFrm.statusLbl.SetLabel( "Sikeres kijelentkezés" )
                self.loginmode = 0
                self.mainFrm.loginLogoutBtn.SetLabel( "Bejelentkezés" )

            else:

                self.mainFrm.statusLbl.SetLabel( "Kijelentkezési hiba" )

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
                self.disposeLoginForm( event )
                self.clearTextFields( event )

            else:

                self.mainFrm.statusLbl.SetLabel( "Azononosítási hiba" )


    def disposeLoginForm( self, event ):
        self.loginFrm.Hide()

# ========================= end section loginform ============================== #

# ========================= start section studentform ========================= #

    # def setManageStudentsForm( self, event ):
        
    #     comboItems = self.model.getComboItems()
    #     self.studentFrm.groupCb.SetItems( comboItems )
    #     self.studentFrm.groupCb.SetValue( "Csoportok" )
    #     self.studentFrm.Show()

    # def addStudentToApi( self, event ):
        
    #     studentData = {}
    #     studentData[ "name" ] = self.studentFrm.nameTf.GetValue()
    #     studentData[ "email" ] = self.studentFrm.emailTf.GetValue()
    #     studentData[ "phone" ] = self.studentFrm.phoneTf.GetValue()
    #     studentData[ "borndate" ] = self.studentFrm.bornTf.GetValue()

    #     success = self.model.addStudent( studentData )
    #     if( success ):
    #         self.mainFrm.statusLbl.SetLabel( "Sikeres kiírás" )
    #         self.clearTextFields( event )

    #     else:
    #         self.mainFrm.statusLbl.SetLabel( "Kiírási hiba" )

    def saveStudent( self, event  ):

        studentData = {}
        comboId = 0
        for combo in self.comboItems:
            if( combo.group == self.mainFrm.groupCb.GetValue() ):
                comboId = combo.id

        row = self.mainFrm.studentTbl.GetSelectedRows()
        studentData[ "name" ] = self.mainFrm.studentTbl.GetCellValue( row[ 0 ], 0 )
        studentData[ "email" ] = self.mainFrm.studentTbl.GetCellValue( row[ 0 ], 1 )
        studentData[ "phone" ] = self.mainFrm.studentTbl.GetCellValue( row[ 0 ], 2 )
        studentData[ "borndate" ] = self.mainFrm.studentTbl.GetCellValue( row[ 0 ], 3 )
        studentData[ "classgroup_id" ] = comboId
        
        success = self.model.addStudent( studentData )
        if( success ):
            self.mainFrm.statusLbl.SetLabel( "Sikeres kiírás ")

        else:
            self.mainFrm.statusLbl.SetLabel( "Írási hiba" )

    def modifyStudent( self ):
        pass

    def deleteStudent( self ):
        pass

    def saveGroup( self ):
        pass

    def deleteGroup( self ):
        pass

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