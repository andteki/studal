import requests
from requests.api import request
from requests.models import Response


class Model:
    
    def __init__( self ):
        
        self.endpoint = "http://localhost:8000/api/"
        self.token = ""


    def getTableCoulumnNames( self ):

        columnNames = [ "Név", "Email", "Telefon", "Születés" ]
        return columnNames


    def getComboItems( self ):

        comboItems = [ "Szoftver", "Ifra", "Logisztika", "Vám" ]
        return comboItems
        

    def getStudentsData( self, text ):

        req = requests.get( self.endpoint + text )
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


    def login( self, loginData ):

        req = requests.post( self.endpoint + "login", data = loginData )
        statusCode = req.status_code

        if( statusCode == 200 ):

            loginDictionary = req.json()
            dataJson = loginDictionary[ "data" ]
            self.token = dataJson[ "token" ]

            return True

        else:
            return False


    def logout( self ):

        headers = { "Authorization" : "Bearer" + self.token }
        req = requests.post( self.endpoint + "logout", headers = headers )
        statusCode = req.status_code

        if( statusCode == 200 ):

            self.token = ""
            return True

        else:

            return False