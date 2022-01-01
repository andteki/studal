import requests
from requests.api import request
from requests.models import Response


class Model:
    
    def __init__( self ):
        
        self.endpoint = "http://localhost:8000/api/"

    def getTableCoulumnNames( self ):

        columnNames = [ "Név", "Email", "Telefon", "Születés" ]
        return columnNames


    def getComboItems( self ):

        comboItems = [ "Szoftver", "Ifra", "Logisztika", "Vám" ]
        return comboItems
        

    def getAllStudentsData( self ):

        req = requests.get( self.endpoint + "students")
        statusCode = req.status_code
        students = []
        if( statusCode == 200 ):
            
            content = req.json()
            
            for stu in content:
                
                student = []
                student.append( stu[ "name" ])
                student.append( stu[ "email"] )
                student.append( stu[ "phone"] )
                student.append( stu[ "borndate"] )
                students.append( student )
        
        return students
