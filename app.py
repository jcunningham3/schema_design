from flask import Flask, render_template, request, session, flash, redirect
from models import db, connect_db, Doctors, Diseases, Patients, Visits, Diagnosis, Region, Categories, Users, Posts, Clubs, Players, Refs, Matches, Goals

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///multiple_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def homepage():
    return render_template('home.html')

# DOCTORS OFFICE SCHEMA GET/POST ROUTES--------------------------------------------------------------------------------------------
@app.route('/doctors')
def doctor_route():
    doctors = Doctors.query.all()
    diseases = Diseases.query.all()
    patients = Patients.query.all()
    visits = Visits.query.all()
    diagnosis = Diagnosis.query.all()
    return render_template('doctor.html', doctors=doctors,diseases=diseases,patients=patients,visits=visits,diagnosis=diagnosis)

@app.route('/doctors/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form['doctors_name']
    specialty = request.form['specialty']

    new_doctor = Doctors(name=name, specialty=specialty)
    db.session.add(new_doctor)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/doctors')

@app.route('/doctors/add_patient', methods=['POST'])
def add_patient():
    patient_name = request.form['patient_name']

    new_patient = Patients(name=patient_name)
    db.session.add(new_patient)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/doctors')

@app.route('/doctors/add_visit', methods=['POST'])
def add_visit():
    doctor_id = request.form['doctor_id']
    patient_id = request.form['patient_id']

    new_visit = Visits(doctor_id=doctor_id, patient_id=patient_id)
    db.session.add(new_visit)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/doctors')


# CRAIGSLSI SCHEMA POST GET/ROUTES--------------------------------------------------------------------------------------------
@app.route('/craigslist')
def craigslist_route():
    region = Region.query.all()
    users = Users.query.all()
    posts = Posts.query.all()
    categories = Categories.query.all()
    return render_template('craigslist.html', region=region,users=users,posts=posts,categories=categories)


# FOOTBALL SCHEMA GET/POST ROUTES--------------------------------------------------------------------------------------------
@app.route('/matches_schema')
def matches_route():
    clubs = Clubs.query.all()
    players = Players.query.all()
    refs = Refs.query.all()
    matches = Matches.query.all()
    goals = Goals.query.all()
    return render_template('football_match.html', clubs=clubs, players=players, refs=refs, matches=matches, goals=goals)

@app.route('/matches_schema/add_club', methods=['POST'])
def add_club():
    club_name = request.form['name']
    points = request.form['points']

    new_club = Clubs(name=club_name, points=points)
    db.session.add(new_club)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/matches_schema')

@app.route('/matches_schema/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    position = request.form['position']
    club_id = request.form['club_id']

    new_player = Players(name=player_name, position=position, club_id=club_id)
    db.session.add(new_player)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/matches_schema')

@app.route('/matches_schema/add_ref', methods=['POST'])
def add_ref():
    ref_name = request.form['ref_name']

    new_ref = Refs(name=ref_name)
    db.session.add(new_ref)
    db.session.commit()
    #flash(f"{new_club.name} added!!")
    return redirect('/matches_schema')
