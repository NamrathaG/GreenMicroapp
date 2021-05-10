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
    ####################################### User table
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

    def get_users(self):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute("SELECT EmailId,UserName from Users")
             
            row = cursor.fetchone()
            challenges=[]
            while row:
                challenge = {}
                challenge['emailId'] = row.EmailId
                challenge['userName'] = row.UserName

                challenges.append(challenge)
                row = cursor.fetchone()

            return json.dumps(challenges, indent=4, default=self.myconverter)
        except Exception as ex:
            print(str(ex))
            raise ex

    ################################ Challenges Table
    def create_challenge(self, title, description, creator_email, start_date, end_date=None, active=1, image_url=""):
        cursor = self.cnxn.cursor()
        try:
             cursor.execute("INSERT INTO Challenges(Title,Description,CreatorId,CreatedDate,EndDate,Active, ImageUrl) values(?,?,?,?,?,?,?);",title, description, creator_email, start_date, end_date, active, image_url)
             cursor.commit()
             return True
        except Exception as ex:
            print(str(ex))
            raise ex

    def get_active_challenges(self):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute("SELECT Id,Title,Description,ImageUrl,CreatorId,CreatedDate,EndDate,Active from Challenges")
             
            row = cursor.fetchone()
            challenges=[]
            while row:
                challenge = {}
                challenge['id'] = row.Id
                challenge['title'] = row.Title
                challenge['description'] = row.Description
                challenge['imageUrl'] = row.ImageUrl
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
 
 ################################## Challenges Accepted Table
    
    def add_challenge_acceptance(self, user_id, challenge_id):
        cursor = self.cnxn.cursor()
        try:
             cursor.execute("INSERT INTO ChallengesAccepted(UserId,ChallengeId,Completed,PhotoUrl,Comment,Reward) values(?,?,?,?,?,?);",user_id,challenge_id,0, "", "", "")
             cursor.commit()
             return True
        except Exception as ex:
            print(str(ex))
            raise ex

    def update_challenge_acceptance(self, user_id, challenge_id, completed = 0, photo_url = "", comment = "", reward = 0):
        cursor = self.cnxn.cursor()
        try:
             cursor.execute("UPDATE ChallengesAccepted SET Completed = %d ,PhotoUrl= %s,Comment = %s,Reward = %d WHERE UserId = %s AND ChallengeId = %d" % (completed, photo_url, comment, reward, user_id, challenge_id) )
             cursor.commit()
             return True
        except Exception as ex:
            print(str(ex))
            raise ex

    def get_accepted_challenges(self):
        cursor = self.cnxn.cursor()
        try:
            cursor.execute("SELECT Challenges.Title, Challenges.CreatorId, ChallengesAccepted.UserId,ChallengesAccepted.ChallengeId,ChallengesAccepted.Completed,ChallengesAccepted.PhotoUrl,ChallengesAccepted.Comment,ChallengesAccepted.Reward FROM ChallengesAccepted LEFT JOIN Challenges ON Challenges.Id = ChallengesAccepted.ChallengeId")
             
            row = cursor.fetchone()
            challenges=[]
            while row:
                challenge = {}
                challenge['title'] = row.Title
                challenge['creator'] = row.CreatorId
                challenge['userId'] = row.UserId
                challenge['challengeId'] = row.ChallengeId
                challenge['completed'] = row.Completed
                challenge['photoUrl'] = row.PhotoUrl
                challenge['comment'] = row.Comment
                challenge['reward'] = row.Reward

                challenges.append(challenge)
                row = cursor.fetchone()

            return json.dumps(challenges, indent=4, default=self.myconverter)
        except Exception as ex:
            print(str(ex))
            raise ex

    def myconverter(self,o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()
       
