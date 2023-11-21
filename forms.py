from app import app
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Username',validators= [DataRequired()],render_kw= {"placeholder":"Username"})
    email = StringField('Email', validators =[DataRequired()],render_kw={"placeholder":"Email"})
    password = PasswordField('Password',validators =[DataRequired()], render_kw= {"placeholder": "Password"})
    submit = SubmitField('Register')
    

class LoginForm(FlaskForm):
    username = StringField('Username',validators =[DataRequired()],render_kw={"placeholder":"Username"})
    email =StringField('Email',validators =[DataRequired()],render_kw={"placeholder ":"Email"})
    password =PasswordField('Password', validators =[DataRequired()],render_kw ={"placeholder" :"Password"})
    submit = SubmitField('Login')
    
class AddRecord(FlaskForm):
    patient_name =StringField('Patient Name', validators =[DataRequired()],render_kw={"placeholder":"Name"})
    patient_email =StringField('Email', validators =[DataRequired()],render_kw={"placeholder" :"Email"})
    patient_address= StringField('Address', validators =[DataRequired()],render_kw={"placeholder" :"Address"})
    symptoms =StringField('Symptoms', validators =[DataRequired()],render_kw= {"placeholder":"Symptoms"})
    allergies =StringField('Symptoms', validators =[DataRequired()],render_kw= {"placeholder":"Allergies"})
    diagnosis =StringField('Diagnosis', validators =[DataRequired()],render_kw={"placeholder":"Diagnosis"})
    prescription = StringField('Prescription', validators =[DataRequired()],render_kw={"placeholder":"Prescription"})
    submit = SubmitField('Submit')
    