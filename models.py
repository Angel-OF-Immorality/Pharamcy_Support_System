from app import app,db
from werkzeug.security import generate_password_hash,check_password_hash
class User(db.Model):
    username = db.Column(db.String(50),primary_key = True)
    email =db.Column(db.String(50),index=True , unique = True)
    password =db.Column(db.String(50),unique=True)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
class Patient(db.Model):
    patient_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    patient_name =db.Column(db.String(50))
    patient_email =db.Column(db.String(50))
    patient_address =db.Column(db.String(100))
    symptoms =db.Column(db.String(500))
    allergies=db.Column(db.String(500))
    diagnosis = db.Column(db.String(100))
    prescription =db.Column(db.String(100))    
        
    
