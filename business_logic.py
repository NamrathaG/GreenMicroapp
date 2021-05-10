from database_ops import DatabaseOperation
from datetime import datetime

class BusinessLogic():
    def __init__(self):
        self.db = DatabaseOperation()

    def create_challenge(self, challenge):
        title = challenge['title']
        description = challenge["description"] if "description" in challenge.keys() else ""
        creator_email = challenge["user_email"]
        creator_name = creator_email.split("@")[0].replace("."," ")
        image_url= challenge['image_url']
        end_date = challenge["end_date"] if "end_date" in challenge.keys() else None

        if not self.db.user_exists(creator_email):
            self.db.create_user(creator_email, creator_name)
        start_date = datetime.now()
        self.db.create_challenge(title, description, creator_email, start_date, end_date, 1, image_url=image_url)

    def get_active_challenges(self):
        return self.db.get_active_challenges()
    
    
    def accept_challenge(self, body):
        user_id = body["user_id"]
        challenge_id = body["challenge_id"]
        self.db.add_challenge_acceptance(user_id, challenge_id)

    def get_users(self):
        return self.db.get_users()

    def get_accepted_challenges(self):
        return self.db.get_accepted_challenges()

