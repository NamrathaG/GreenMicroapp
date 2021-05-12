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
        badge = challenge['badge']

        if not self.db.user_exists(creator_email):
            self.db.create_user(creator_email, creator_name)
        start_date = datetime.now()
        self.db.create_challenge(title, description, creator_email, start_date, end_date, 1, image_url=image_url, badge=badge)
    
    def delete_challenge(self, id):
        challenge = self.db.get_challenge_by_id(id)

        if challenge:
            self.db.delete_challenge(id)
            return True, "Challenge with id %s deleted successfully!"%id
        else:
            error = "Challenge with id: %s does not exists"%id
            print(error)
            return False, error

    def update_challenge(self, id, body):
        challenge = self.db.get_challenge_by_id(id)
        if challenge:
            title = body["title"] if "title" in body.keys() else challenge['title']
            description = body["description"] if "description" in body.keys() else challenge['description']
            creator_email = body["user_email"] if "user_email" in body.keys() else challenge['creator']
            creator_name = creator_email.split("@")[0].replace("."," ")
            image_url= body['image_url'] if "image_url" in body.keys() else challenge['imageUrl']
            end_date = body["end_date"] if "end_date" in body.keys() else challenge['endDate']
            active = body['active'] if 'active' in body.keys() else challenge['active']

            self.db.update_challenge(id, title, description, end_date, active, image_url)
            return True, "Record Updated Successfully"
        else:
            error = "Challenge with id: %s does not exists"%id
            print(error)
            return False, error


    def get_active_challenges(self):
        return self.db.get_active_challenges()

    def get_challenge_by_id(self,id):
        return self.db.get_challenge_by_id(id)
    
    
    def accept_challenge(self, body):
        user_id = body["user_id"]
        challenge_id = body["challenge_id"]
        self.db.add_challenge_acceptance(user_id, challenge_id)

    def get_users(self):
        return self.db.get_users()

    def get_accepted_challenges(self):
        return self.db.get_accepted_challenges()

    
    def get_badges(self):
        return self.db.get_badges()

    def get_leaderboard(self):
        return self.db.get_leaderboard()

    def upload_challenge(self, payload):
        comment = payload['comment']
        photo_url = payload['photo_url']
        user_id = payload['user_id']
        challenge_id = int(payload['challenge_id'])

        status = self.db.update_challenge_acceptance(user_id, challenge_id, completed=1, photo_url=photo_url, comment=comment)
        
