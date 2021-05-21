from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW

# MEDICAL CENTER MODELS
class Doctors(db.Model):
    # Doctor's table
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    specialty = db.Column(db.Text, nullable=False)

class Patients(db.Model):
    # Doctor's table
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

class Diseases(db.Model):
    # Doctor's table
    __tablename__ = "diseases"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

class Visits(db.Model):
    # Doctor's table
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

class Diagnosis(db.Model):
    # Doctor's table
    __tablename__ = "diagnosis"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.id'))
    disease_id = db.Column(db.Integer, db.ForeignKey('diseases.id'))


# CRAIGSKIST MODELS
class Region(db.Model):
    # Doctor's table
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

class Users(db.Model):
    # Doctor's table
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    preferred_region_id = db.Column(db.Integer, db.ForeignKey('region.id'))

class Posts(db.Model):
    # Doctor's table
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    post_location = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class Categories(db.Model):
    # Doctor's table
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Text, nullable=False)


# FOOTBALL LEAGUE MODELS
class Clubs(db.Model):
    # Doctor's table
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=False)

class Players(db.Model):
    # Doctor's table
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))

class Refs(db.Model):
    # Doctor's table
    __tablename__ = "refs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)

class Matches(db.Model):
    # Doctor's table
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    matchweek = db.Column(db.Text, nullable=False)
    home_club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
    away_club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))

class Goals(db.Model):
    # Doctor's table
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'))
