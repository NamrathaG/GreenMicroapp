import pyodbc as po
import json
from datetime import datetime
from datetime import date
import os

class DatabaseOperation():
    def __init__(self):
        server = os.environ["DB_SERVER"]
        database = os.environ["DATABASE"]
        username = os.environ["DB_USERNAME"]
        password = os.environ["DB_PASSWORD"]

        self.cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +server+';DATABASE='+database+';UID='+username+';PWD=' + password)

    def user_exists(self,email):
        cursor = self.cnxn.cursor()
    
        # Fetch data into a cursor
        cursor.execute("SELECT * FROM Users WHERE EmailId=?;",email)

        row = cursor.fetchone()
        if row:
            return True
        else:
            return False
    
    def create_user(self, email, username):
        cursor = self.cnxn.cursor()
    
        # Fetch data into a cursor
        try:
            cursor.execute("Insert INTO Users(EmailId,UserName) values(?,?)",email, username)
            cursor.commit()
            return True
        except Exception as ex:
            print(str(ex))
            raise ex
    
    def create_challange(self, title, description, creator_email, start_date, end_date=None, active=1):
        cursor = self.cnxn.cursor()
        try:
             cursor.execute("INSERT INTO Challenges(Title,Description,CreatorId,CreatedDate,EndDate,Active) values(?,?,?,?,?,?);",title, description, creator_email, start_date, end_date, active)
             cursor.commit()
             return True
        except Exception as ex:
            print(str(ex))
            raise ex

    def get_active_challanges(self):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute("SELECT Id,Title,Description,CreatorId,CreatedDate,EndDate,Active from Challenges")
             
            row = cursor.fetchone()
            challenges=[]
            while row:
                challenge = {}
                challenge['id'] = row.Id
                challenge['title'] = row.Title
                challenge['description'] = row.Description
                challenge['creator'] = row.CreatorId
                challenge['createdDate'] = row.CreatedDate
                challenge['endDate'] = row.EndDate
                challenge['active'] = row.Active

                challenges.append(challenge)
                row = cursor.fetchone()

            return json.dumps(challenges, indent=4, default=self.myconverter)
        except Exception as ex:
            print(str(ex))
            raise ex
    
    def myconverter(self,o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()
       
