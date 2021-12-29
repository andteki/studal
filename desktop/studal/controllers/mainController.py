from controllers.viewController import ViewController
import requests
from requests.api import request
from requests.models import Response

class MainController:

    def __init__( self ):

        self.viewCtrl = ViewController()

    def getAllStudent( self ):

        req = requests.get( "http://localhost:8000/api/students")
        print( req.status_code )
        print( req.headers[ "content-Type" ])
        print( req.text )
