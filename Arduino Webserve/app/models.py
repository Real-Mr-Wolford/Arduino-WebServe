from . import db
#from datetime import datetime, timezone

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) 
    message = db.Column(db.String(1000))

#class UserMessage(db.Model):
   # id = db.Column(db.Integer, primary_key = True)
   # message = db.Column(db.String(200), nullable = False)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
   
