from models import db, Doctors, Diseases, Patients, Visits, Diagnosis, Region, Categories, Users, Posts, Clubs, Players, Refs, Matches, Goals
from app import app

# create all tables
db.drop_all()
db.create_all()
