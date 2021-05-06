from database_ops import DatabaseOperation
from datetime import datetime

class BusinessLogic():
    def __init__(self):
        self.db = DatabaseOperation()

    def create_challange(self, challange):
        title = challange['title']
        description = challange["description"] if "description" in challange.keys() else ""
        creator_email = challange["user_email"]
        creator_name = creator_email.split("@")[0].replace("."," ")
        end_date = challange["end_date"] if "end_date" in challange.keys() else None

        if not self.db.user_exists(creator_email):
            self.db.create_user(creator_email, creator_name)
        start_date = datetime.now()
        self.db.create_challange(title, description, creator_email, start_date, end_date, 1)

    def get_active_challanges(self):
        return self.db.get_active_challanges()