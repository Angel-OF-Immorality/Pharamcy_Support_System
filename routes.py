from app import app,db
from flask import render_template,redirect,url_for,flash,request
from forms import RegisterForm, LoginForm,AddRecord
from models import User,Patient

@app.route('/',methods =['GET','POST'])
def index():
    return render_template("home.html")

@app.route('/register',methods =['GET','POST'])
def register():
    myform = RegisterForm()
    if myform.validate_on_submit():
        new_user = User(
            username= myform.username.data,
            email= myform.email.data,
            password= myform.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template("register.html",template_form = myform)

@app.route('/login',methods =['GET','POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        email =form.email.data
        password =form.password.data
        user = User.query.filter_by(username = username).first()
        if user and user.check_password(password):
            flash('Login successful','success')
            return redirect(url_for('main'))
        else:
            flash('Login failed. Please check your credentials','danger')
            
    
    return render_template("login.html", template_form = form)

@app.route('/main', methods =['GET','POST'])
def main():
    return render_template("main.html")

@app.route('/addrecord',methods =['GET','POST'])
def addrecord():
    form = AddRecord()
    if form.validate_on_submit():
        new_patient = Patient(
            patient_name =form.patient_name.data,
            patient_email =form.patient_email.data,
            patient_address = form.patient_address.data,
            symptoms =form.symptoms.data,
            diagnosis = form.diagnosis.data,
            prescription = form.prescription.data)
        
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('main'))
    
        
    return render_template("addrecord.html",template_form =form)

@app.route('/unique_patients')
def unique_patients():
    unique_patients = db.session.query(Patient.patient_name,Patient.patient_email,Patient.patient_address).distinct()
    return render_template('patients.html', unique_patients = unique_patients)

@app.route('/patient_record/<string:patient_name>')
def patient_record(patient_name):
    patient_record =Patient.query.filter_by(patient_name=patient_name).all()
    return render_template('patient_record.html',patient_name = patient_name,patient_record=patient_record)

@app.route('/edit_record/<int:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    record = Patient.query.get(record_id)

    if request.method == 'POST':
        record.symptoms = request.form['symptoms']
        record.diagnosis = request.form['diagnosis']
        record.prescription = request.form['prescription']

        db.session.commit()

        return redirect(url_for('patient_record', patient_name=record.patient_name))

    return render_template('edit_record.html', record=record)
